import polars as pl
import pandas as pd
from typing import Union, Optional, List
import io


def under_five_mortality_rate(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    under5_deaths_col: str,
    population_u5_col: str,
    period_days: Optional[int] = None,
    per: int = 10000
) -> pl.DataFrame:
    """
    Under-five Mortality Rate (U5MR)
    ================================

    What
    ----
    Under-5 deaths per population, scaled per N (optionally normalized by time period).

    When
    ----
    Health and emergency monitoring.

    Why
    ---
    Standardized severity indicator for children.

    Parameters
    ----------
    data : str | pd.DataFrame | pl.DataFrame | io.BytesIO
        Input dataset.
    under5_deaths_col : str
        Under-5 death counts for the period.
    population_u5_col : str
        Under-5 population at risk.
    period_days : int | None
        If provided, normalize to per-day rate before scaling.
    per : int, default 10000
        Scale factor.

    Returns
    -------
    pl.DataFrame
        Placeholder U5MR column.
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

    deaths = pl.col(under5_deaths_col).cast(pl.Float64)
    pop = pl.col(population_u5_col).cast(pl.Float64)
    base = (deaths / pl.when(pop == 0).then(None).otherwise(pop))
    if period_days and period_days > 0:
        base = base / float(period_days)
    u5mr = base * float(per)
    return df.with_columns(u5mr.alias("u5mr_placeholder"))
