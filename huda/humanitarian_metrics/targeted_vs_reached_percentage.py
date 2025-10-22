import polars as pl
import pandas as pd
from typing import Union, Optional, List
import io


def targeted_vs_reached_percentage(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    targeted_col: str,
    reached_col: str,
    group_by: Optional[List[str]] = None,
    percent: bool = True
) -> pl.DataFrame:
    """
    % Targeted vs Reached
    =====================

    What
    ----
    Share of reached compared to targeted.

    When
    ----
    Monitoring progress against targets.

    Why
    ---
    Shows implementation performance.

    Parameters
    ----------
    data : str | pd.DataFrame | pl.DataFrame | io.BytesIO
        Input dataset.
    targeted_col : str
        Targeted people.
    reached_col : str
        Reached people.
    group_by : list[str] | None
        Optional grouping.
    percent : bool, default True
        If True, multiply by 100.

    Returns
    -------
    pl.DataFrame
        Data with placeholder percent reached of targeted.
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

    denom = pl.col(targeted_col).cast(pl.Float64)
    num = pl.col(reached_col).cast(pl.Float64)
    ratio = (num / pl.when(denom == 0).then(None).otherwise(denom))
    if percent:
        ratio = ratio * 100.0
    return df.with_columns(ratio.alias("pct_reached_of_targeted_placeholder"))
