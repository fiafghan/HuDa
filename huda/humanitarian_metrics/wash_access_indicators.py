import polars as pl
import pandas as pd
from typing import Union, Optional, List
import io


def wash_access_indicators(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    improved_water_col: Optional[str] = None,
    improved_sanitation_col: Optional[str] = None,
    population_col: Optional[str] = None,
    percent: bool = True
) -> pl.DataFrame:
    """
    WASH Access Indicators
    ======================

    What
    ----
    Compute simple access rates for improved water/sanitation.

    When
    ----
    WASH assessments and monitoring.

    Why
    ---
    Track access to basic services.

    Parameters
    ----------
    data : str | pd.DataFrame | pl.DataFrame | io.BytesIO
        Input dataset.
    improved_water_col : str | None
        People with access to improved water.
    improved_sanitation_col : str | None
        People with access to improved sanitation.
    population_col : str | None
        Population denominator.
    percent : bool, default True
        If True, express as percent.

    Returns
    -------
    pl.DataFrame
        Placeholder water/sanitation access rates.
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

    denom = pl.col(population_col).cast(pl.Float64) if population_col else pl.lit(None)
    water = (pl.col(improved_water_col).cast(pl.Float64) / pl.when(denom == 0).then(None).otherwise(denom)) if improved_water_col else pl.lit(None)
    san = (pl.col(improved_sanitation_col).cast(pl.Float64) / pl.when(denom == 0).then(None).otherwise(denom)) if improved_sanitation_col else pl.lit(None)
    if percent:
        water = water * 100.0 if water is not None else water
        san = san * 100.0 if san is not None else san
    return df.with_columns([
        water.alias("pct_improved_water_placeholder") if improved_water_col else pl.lit(None).alias("pct_improved_water_placeholder"),
        san.alias("pct_improved_sanitation_placeholder") if improved_sanitation_col else pl.lit(None).alias("pct_improved_sanitation_placeholder"),
    ])
