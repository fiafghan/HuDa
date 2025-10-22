import polars as pl
import pandas as pd
from typing import Union, Optional, List
import io


def health_facility_density_per_10k(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    facility_count_col: str,
    population_col: str,
    group_by: Optional[List[str]] = None
) -> pl.DataFrame:
    """
    Health Facility Density per 10k
    ===============================

    What
    ----
    Facilities per 10,000 population.

    When
    ----
    Service availability comparisons across areas.

    Why
    ---
    Normalize counts by population for comparability.

    Parameters
    ----------
    data : str | pd.DataFrame | pl.DataFrame | io.BytesIO
        Input dataset.
    facility_count_col : str
        Column with number of facilities.
    population_col : str
        Column with population.
    group_by : list[str] | None
        Optional grouping.

    Returns
    -------
    pl.DataFrame
        With placeholder density column per 10k.
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

    fac = pl.col(facility_count_col).cast(pl.Float64)
    pop = pl.col(population_col).cast(pl.Float64)
    density = (fac / pl.when(pop == 0).then(None).otherwise(pop)) * 10000.0
    return df.with_columns(density.alias("health_facilities_per_10k_placeholder"))
