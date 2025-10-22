import polars as pl
import pandas as pd
from typing import Union, Optional, List
import io


def crude_mortality_rate(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    deaths_col: str,
    population_col: str,
    period_days: Optional[int] = None,
    per: int = 10000
) -> pl.DataFrame:
    """
    Crude Mortality Rate (CMR)
    ==========================

    What
    ----
    Deaths per population, scaled per N (optionally normalized by time period).

    When
    ----
    Health/emergency monitoring and comparisons across areas.

    Why
    ---
    Standardized indicator for severity.

    Parameters
    ----------
    data : str | pd.DataFrame | pl.DataFrame | io.BytesIO
        Input dataset.
    deaths_col : str
        Death counts over the reference period.
    population_col : str
        Population at risk.
    period_days : int | None
        If provided, normalize to per-day rate multiplied by 10k (basic placeholder).
    per : int, default 10000
        Scale factor (e.g., per 10,000).

    Returns
    -------
    pl.DataFrame
        Placeholder column with crude mortality rate.
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

    deaths = pl.col(deaths_col).cast(pl.Float64)
    pop = pl.col(population_col).cast(pl.Float64)
    base = (deaths / pl.when(pop == 0).then(None).otherwise(pop))
    if period_days and period_days > 0:
        base = base / float(period_days)
    cmr = base * float(per)
    return df.with_columns(cmr.alias("cmr_placeholder"))
