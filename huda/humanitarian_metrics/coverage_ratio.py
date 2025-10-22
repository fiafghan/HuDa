import polars as pl
import pandas as pd
from typing import Union, Optional, List
import io


def coverage_ratio(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    reached_col: str,
    targeted_col: str,
    group_by: Optional[List[str]] = None
) -> pl.DataFrame:
    """
    Coverage Ratio (Reached/Targeted)
    =================================

    What
    ----
    Compute coverage as reached divided by targeted.

    When
    ----
    Monitoring and endline reporting.

    Why
    ---
    Indicates how much of the target has been covered.

    Parameters
    ----------
    data : str | pd.DataFrame | pl.DataFrame | io.BytesIO
        Input dataset.
    reached_col : str
        People reached.
    targeted_col : str
        People targeted.
    group_by : list[str] | None
        Optional grouping.

    Returns
    -------
    pl.DataFrame
        Data with placeholder coverage ratio column.
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
    return df.with_columns(ratio.alias("coverage_ratio_placeholder"))
