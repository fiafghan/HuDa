import polars as pl
import pandas as pd
from typing import Union, Optional, List
import io


def children_affected_percentage(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    children_affected_col: str,
    population_col: str,
    group_by: Optional[List[str]] = None,
    percent: bool = True
) -> pl.DataFrame:
    """
    % of Children Affected
    ======================

    What
    ----
    Percent of affected children relative to population.

    When
    ----
    Protection/Child-focused reporting.

    Why
    ---
    Highlights child-specific needs.

    Parameters
    ----------
    data : str | pd.DataFrame | pl.DataFrame | io.BytesIO
        Input dataset.
    children_affected_col : str
        Count of affected children.
    population_col : str
        Total population (or child population if available).
    group_by : list[str] | None
        Optional grouping.
    percent : bool, default True
        If True, multiply by 100.

    Returns
    -------
    pl.DataFrame
        With placeholder percent column.
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

    denom = pl.col(population_col).cast(pl.Float64)
    num = pl.col(children_affected_col).cast(pl.Float64)
    ratio = (num / pl.when(denom == 0).then(None).otherwise(denom))
    if percent:
        ratio = ratio * 100.0
    return df.with_columns(ratio.alias("pct_children_affected_placeholder"))
