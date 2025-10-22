import polars as pl
import pandas as pd
from typing import Union, Optional, List
import io


def people_displaced_per_1000(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    displaced_col: str,
    population_col: str,
    group_by: Optional[List[str]] = None
) -> pl.DataFrame:
    """
    People Displaced per 1000
    =========================

    What
    ----
    Displaced people per 1,000 population.

    When
    ----
    Displacement monitoring and comparisons across areas.

    Why
    ---
    Normalize displacement counts for comparability.

    Parameters
    ----------
    data : str | pd.DataFrame | pl.DataFrame | io.BytesIO
        Input dataset.
    displaced_col : str
        Number of displaced people.
    population_col : str
        Population denominator.
    group_by : list[str] | None
        Optional grouping.

    Returns
    -------
    pl.DataFrame
        Placeholder displaced per 1000 column.
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

    disp = pl.col(displaced_col).cast(pl.Float64)
    pop = pl.col(population_col).cast(pl.Float64)
    rate = (disp / pl.when(pop == 0).then(None).otherwise(pop)) * 1000.0
    return df.with_columns(rate.alias("displaced_per_1000_placeholder"))
