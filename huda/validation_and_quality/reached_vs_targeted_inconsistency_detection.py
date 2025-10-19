import polars as pl
import pandas as pd
from typing import Union, List, Optional, Dict, Tuple
import io


def reached_vs_targeted_inconsistency_detection(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    reached_cols: Optional[List[str]] = None,
    targeted_cols: Optional[List[str]] = None,
) -> pl.DataFrame:
    """
    Detect rows where "reached" exceeds "targeted" in humanitarian datasets.

    What this does:
    - Flags records where any reached value is greater than the corresponding targeted value.
    - Works with one or multiple pairs of columns.
    - Auto-detects columns when not provided (by name patterns like 'reached' and 'targeted').

    When to use:
    - During validation before reporting or dashboarding.
    - After data cleaning and merging, to catch logic errors.

    Why important:
    - Prevents publishing impossible coverage numbers (reached > targeted).
    - Highlights potential data entry or aggregation mistakes.

    Where to apply:
    - Afghanistan survey datasets (e.g., WASH, Health, Food Security) where activities have
      targeted vs reached figures by province, district, or partner.

    Simple example (Afghanistan):
    - Suppose a WASH partner targets 1,000 households in Kabul but reports 1,200 reached.
      This function will flag that row.

    Parameters:
    - data: CSV path, pandas.DataFrame, polars.DataFrame, or file bytes (CSV)
    - reached_cols: List of column names containing reached values. Optional.
    - targeted_cols: List of column names containing targeted values. Optional.
      If both are omitted, the function will try to infer pairs by column names.

    Returns:
    - A Polars DataFrame of inconsistent rows with:
      - the original columns
      - boolean columns per pair (e.g., 'reached_gt_targeted_<i>')
      - 'inconsistency_count' showing how many pairs failed in that row

    Usage:
    ```python
    import polars as pl
    from huda.validation_and_quality import reached_vs_targeted_inconsistency_detection

    df = pl.DataFrame({
        "province": ["Kabul", "Herat", "Balkh"],
        "targeted": [1000, 800, 600],
        "reached": [1200, 700, 600],
    })

    flagged = reached_vs_targeted_inconsistency_detection(df, reached_cols=["reached"], targeted_cols=["targeted"])
    print(flagged)
    ```
    """
    # 1) Normalize input to Polars DataFrame
    if isinstance(data, str):
        df = pl.read_csv(data)
    elif isinstance(data, io.BytesIO):
        df = pl.read_csv(data)
    elif isinstance(data, pd.DataFrame):
        df = pl.from_pandas(data)
    elif isinstance(data, pl.DataFrame):
        df = data
    else:
        raise TypeError("Unsupported data type")

    # 2) Infer columns if not provided
    cols_lower = {c.lower(): c for c in df.columns}
    if reached_cols is None or targeted_cols is None:
        # naive inference by name patterns
        r_candidates = [c for c in df.columns if "reached" in c.lower()]
        t_candidates = [c for c in df.columns if "target" in c.lower()]
        # If nothing inferred and user passed one side, keep that
        reached_cols = reached_cols or r_candidates
        targeted_cols = targeted_cols or t_candidates

    if not reached_cols or not targeted_cols:
        raise ValueError("Could not determine reached/targeted columns. Provide 'reached_cols' and 'targeted_cols', or ensure columns include these keywords.")

    if len(reached_cols) != len(targeted_cols):
        raise ValueError("'reached_cols' and 'targeted_cols' must be lists of the same length (pair-wise comparison).")

    # 3) Build per-pair inconsistency flags
    flag_cols = []
    for i, (r_col, t_col) in enumerate(zip(reached_cols, targeted_cols), start=1):
        if r_col not in df.columns or t_col not in df.columns:
            raise ValueError(f"Column pair missing in dataframe: '{r_col}', '{t_col}'")
        flag_name = f"reached_gt_targeted_{i}"
        # Cast to numeric where possible; if not numeric, comparison will yield null -> treat as False
        flag_expr = (pl.col(r_col).cast(pl.Float64, strict=False) > pl.col(t_col).cast(pl.Float64, strict=False)).alias(flag_name)
        flag_cols.append(flag_expr)

    df_flagged = df.with_columns(flag_cols)

    # 4) Count number of inconsistencies per row and filter
    df_flagged = df_flagged.with_columns(
        pl.sum_horizontal([pl.col(expr.meta.output_name()) for expr in flag_cols]).cast(pl.Int64).alias("inconsistency_count")
    )

    result = df_flagged.filter(pl.col("inconsistency_count") > 0)
    return result
