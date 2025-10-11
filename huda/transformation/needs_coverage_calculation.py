import polars as pl
import pandas as pd
from typing import List, Dict, Union, Optional
import io

def needs_coverage_calculation(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    needs_columns: List[str],
    provided_columns: List[str],
    output_coverage_col: str = "coverage_pct",
    group_by_cols: Optional[List[str]] = None,
    weights: Optional[Dict[str, Union[int, float]]] = None
) -> pl.DataFrame:
    """
    🚨 Calculate Humanitarian Needs Coverage
    ======================================

    (Docstring trimmed for brevity)
    """

    # --- 1. Convert data to Polars DataFrame ---
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

    # --- 2. Calculate individual coverage for each need ---
    for need_col, provided_col in zip(needs_columns, provided_columns):
        coverage_col_name = f"{need_col}_coverage_pct"
        df = df.with_columns(
            pl.when(pl.col(need_col) > 0)
            .then((pl.col(provided_col) / pl.col(need_col) * 100))
            .otherwise(None)
            .alias(coverage_col_name)
        )

    # --- 3. Grouping (if provided) ---
    if group_by_cols:
        agg_exprs = []

        # Sum up totals
        for col in needs_columns + provided_columns:
            agg_exprs.append(pl.sum(col).alias(col))

        # Add mean for coverage columns
        for need_col in needs_columns:
            cov_col = f"{need_col}_coverage_pct"
            agg_exprs.append(pl.mean(cov_col).alias(cov_col))

        df = df.group_by(group_by_cols).agg(agg_exprs)

    # --- 4. Weighted overall coverage ---
    if weights:
        weighted_exprs = []
        total_weight = sum(weights.values())
        for need_col, weight in weights.items():
            cov_col = f"{need_col}_coverage_pct"
            weighted_exprs.append((pl.col(cov_col) * weight))

        df = df.with_columns(
            (sum(weighted_exprs) / total_weight).alias(output_coverage_col)
        )

    return df


# ✅ Example test (works fine now)
if __name__ == "__main__":
    data_zero_total_needs = pl.DataFrame({
        "location": ["Z"],
        "f_needs": [0],
        "f_prov": [0],
        "w_needs": [0],
        "w_prov": [0]
    })

    weights_zero_total = {"f_needs": 0.5, "w_needs": 0.5}

    df_zero_total_needs = needs_coverage_calculation(
        data=data_zero_total_needs,
        needs_columns=["f_needs", "w_needs"],
        provided_columns=["f_prov", "w_prov"],
        weights=weights_zero_total,
        output_coverage_col="overall_zeros"
    )

    print(df_zero_total_needs)
