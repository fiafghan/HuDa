import polars as pl
import pandas as pd
from typing import Union, Optional, List
import io


def population_in_need_percentage(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    in_need_col: str,
    population_col: str,
    group_by: Optional[List[str]] = None,
    percent: bool = True
) -> pl.DataFrame:
    """
    Percentage of Population in Need
    =================================

    What
    ----
    Calculate the percent of people in need out of total population.

    When
    ----
    Situation overview and severity classification by area.

    Why
    ---
    Shows scale of need relative to population.

    Parameters
    ----------
    data : str | pd.DataFrame | pl.DataFrame | io.BytesIO
        Input dataset.
    in_need_col : str
        Column with number of people in need.
    population_col : str
        Column with total population.
    group_by : list[str] | None
        Optional columns to compute per group (e.g., province).
    percent : bool, default True
        If True, multiply by 100 to express as percent.

    Returns
    -------
    pl.DataFrame
        Original data with a placeholder percent column.

    Example
    -------
    >>> population_in_need_percentage(df, in_need_col="in_need", population_col="population")
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
    num = pl.col(in_need_col).cast(pl.Float64)
    ratio = (num / pl.when(denom == 0).then(None).otherwise(denom))
    if percent:
        ratio = ratio * 100.0
    return df.with_columns(ratio.alias("pin_pct_placeholder"))
