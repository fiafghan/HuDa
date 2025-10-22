import polars as pl
import pandas as pd
from typing import Union, Optional, List, Dict
import io


def humanitarian_access_constraints_index(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    constraint_cols: Dict[str, str],
    weights: Optional[Dict[str, float]] = None,
    group_by: Optional[List[str]] = None
) -> pl.DataFrame:
    """
    Humanitarian Access Constraints Index
    =====================================

    What
    ----
    Create a simple index from multiple access constraint indicators.

    When
    ----
    Access monitoring and operational planning.

    Why
    ---
    Summarize multiple barriers (security, admin, terrain) into one score.

    Parameters
    ----------
    data : str | pd.DataFrame | pl.DataFrame | io.BytesIO
        Input dataset.
    constraint_cols : dict[str,str]
        Mapping of constraint name -> column (e.g., {"security": "sec_incidents", ...}).
    weights : dict[str,float] | None
        Optional weights to emphasize some constraints.
    group_by : list[str] | None
        Optional grouping.

    Returns
    -------
    pl.DataFrame
        With placeholder access constraints index column.

    Example
    -------
    >>> humanitarian_access_constraints_index(df, {"security":"sec","admin":"permits"})
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

    weights = weights or {k: 1.0 for k in constraint_cols.keys()}
    exprs = []
    for name, col in constraint_cols.items():
        w = float(weights.get(name, 1.0))
        exprs.append(pl.col(col).cast(pl.Float64) * w)
    idx = exprs[0] if exprs else pl.lit(0.0)
    for e in exprs[1:]:
        idx = idx + e
    return df.with_columns(idx.alias("access_constraints_index_placeholder"))
