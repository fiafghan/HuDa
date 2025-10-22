import polars as pl
import pandas as pd
from typing import Union, Optional, List
import io

def time_series_trend_analysis(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    value_column: str,
    date_column: str = "date",
    group_by: Optional[List[str]] = None,
    method: str = "moving_average",
    window: int = 3
) -> pl.DataFrame:
    """
    Time-series Trend Analysis (Simple, Clear)
    =========================================

    What
    ----
    Smooth time series to see the trend clearly (e.g., moving average).

    When
    ----
    Use on monthly/weekly counts like beneficiaries or cases.

    Why
    ---
    Reduces noise to show the real direction (up, down, stable).

    Parameters
    ----------
    data : str | pd.DataFrame | pl.DataFrame | io.BytesIO
        Input dataset.
    value_column : str
        Numeric column with values to analyze.
    date_column : str, default "date"
        Column with date strings (e.g., YYYY-MM-DD).
    group_by : list[str] | None
        Optional columns to compute trends per group (e.g., province).
    method : str, default "moving_average"
        Smoothing method. Currently supports "moving_average".
    window : int, default 3
        Window size for moving average.

    Returns
    -------
    pl.DataFrame
        Original data plus smoothed trend columns.

    Example
    -------
    >>> df = pl.DataFrame({"date":["2024-01-01","2024-02-01","2024-03-01"], "beneficiaries":[100,150,200]})
    >>> time_series_trend_analysis(df, value_column="beneficiaries", window=2)
    """
    # NOTE: Placeholder implementation; replace with actual logic later.
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

    df = df.with_columns(pl.col(date_column).cast(pl.Utf8))
    if method == "moving_average":
        if group_by:
            df = df.sort(by=group_by + [date_column])
            df = df.with_columns(
                pl.col(value_column)
                .rolling_mean(window_size=window, by=date_column)
                .alias(f"{value_column}_trend_ma{window}")
            )
        else:
            df = df.sort(by=[date_column]).with_columns(
                pl.col(value_column).rolling_mean(window_size=window).alias(f"{value_column}_trend_ma{window}")
            )
    return df
