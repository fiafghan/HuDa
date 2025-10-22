import polars as pl
import pandas as pd
from typing import Union, Optional, List, Dict
import io


def food_consumption_score(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    food_group_cols: Dict[str, str],
    weights: Optional[Dict[str, float]] = None,
    group_by: Optional[List[str]] = None
) -> pl.DataFrame:
    """
    Food Consumption Score (FCS)
    ============================

    What
    ----
    Compute a simple FCS-like score using food group frequencies and weights.

    When
    ----
    Food security assessments using household surveys.

    Why
    ---
    Summarize dietary diversity and frequency.

    Parameters
    ----------
    data : str | pd.DataFrame | pl.DataFrame | io.BytesIO
        Input dataset.
    food_group_cols : dict[str,str]
        Mapping of group name -> column name (e.g., {"cereals": "cereals_days", ...}).
    weights : dict[str,float] | None
        Optional weights per group; default simple placeholder weights.
    group_by : list[str] | None
        Optional grouping.

    Returns
    -------
    pl.DataFrame
        With placeholder FCS column.
    """
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

    weights = weights or {k: 1.0 for k in food_group_cols.keys()}
    exprs = []
    for grp, col in food_group_cols.items():
        w = float(weights.get(grp, 1.0))
        exprs.append((pl.col(col).cast(pl.Float64) * w))
    score = exprs[0]
    for e in exprs[1:]:
        score = score + e
    return df.with_columns(score.alias("fcs_placeholder"))
