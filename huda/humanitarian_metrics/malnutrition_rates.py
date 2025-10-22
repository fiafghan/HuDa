import polars as pl
import pandas as pd
from typing import Union, Optional, List
import io


def malnutrition_rates(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    gam_col: Optional[str] = None,
    sam_col: Optional[str] = None,
    mam_col: Optional[str] = None,
    population_u5_col: Optional[str] = None,
    percent: bool = True
) -> pl.DataFrame:
    """
    Malnutrition Rates (GAM, SAM, MAM)
    ==================================

    What
    ----
    Compute simple rates for GAM, SAM, and MAM using U5 population.

    When
    ----
    Nutrition surveillance and assessments.

    Why
    ---
    Track malnutrition burden among under-5.

    Parameters
    ----------
    data : str | pd.DataFrame | pl.DataFrame | io.BytesIO
        Input dataset.
    gam_col : str | None
        Number of GAM cases.
    sam_col : str | None
        Number of SAM cases.
    mam_col : str | None
        Number of MAM cases.
    population_u5_col : str | None
        Under-5 population.
    percent : bool, default True
        Express as percent if True.

    Returns
    -------
    pl.DataFrame
        Placeholder rates for GAM/SAM/MAM.
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

    denom = pl.col(population_u5_col).cast(pl.Float64) if population_u5_col else pl.lit(None)
    def rate(col: Optional[str]):
        if not col:
            return pl.lit(None)
        r = pl.col(col).cast(pl.Float64) / pl.when(denom == 0).then(None).otherwise(denom)
        return r * 100.0 if percent else r

    return df.with_columns([
        rate(gam_col).alias("gam_rate_placeholder"),
        rate(sam_col).alias("sam_rate_placeholder"),
        rate(mam_col).alias("mam_rate_placeholder"),
    ])
