import polars as pl
import pandas as pd
from typing import Union, Optional, List
import io


def idps_refugees_affected_percentage(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    idps_col: Optional[str] = None,
    refugees_col: Optional[str] = None,
    population_col: Optional[str] = None,
    total_affected_col: Optional[str] = None,
    percent: bool = True
) -> pl.DataFrame:
    """
    % of IDPs/Refugees Affected
    ===========================

    What
    ----
    Percent of affected IDPs/refugees relative to population or total affected.

    When
    ----
    Displacement-focused reporting and planning.

    Why
    ---
    Track vulnerability among displaced populations.

    Parameters
    ----------
    data : str | pd.DataFrame | pl.DataFrame | io.BytesIO
        Input dataset.
    idps_col : str | None
        Count of IDPs affected.
    refugees_col : str | None
        Count of refugees affected.
    population_col : str | None
        Population denominator (optional).
    total_affected_col : str | None
        Alternative denominator: total affected if population unknown.
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

    idps = pl.col(idps_col).cast(pl.Float64) if idps_col else pl.lit(0.0)
    refs = pl.col(refugees_col).cast(pl.Float64) if refugees_col else pl.lit(0.0)
    num = idps + refs
    if population_col:
        denom = pl.col(population_col).cast(pl.Float64)
    elif total_affected_col:
        denom = pl.col(total_affected_col).cast(pl.Float64)
    else:
        denom = pl.lit(None)
    ratio = (num / pl.when(denom == 0).then(None).otherwise(denom))
    if percent:
        ratio = ratio * 100.0
    return df.with_columns(ratio.alias("pct_idps_refugees_affected_placeholder"))
