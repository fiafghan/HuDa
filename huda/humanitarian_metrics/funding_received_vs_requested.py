import polars as pl
import pandas as pd
from typing import Union, Optional, List
import io


def funding_received_vs_requested(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    received_col: str,
    requested_col: str,
    group_by: Optional[List[str]] = None,
    percent: bool = True
) -> pl.DataFrame:
    """
    Funding Received vs Requested
    =============================

    What
    ----
    Compare funding received against requested.

    When
    ----
    Donor reporting, appeals, and advocacy.

    Why
    ---
    Show funding gaps and progress.

    Parameters
    ----------
    data : str | pd.DataFrame | pl.DataFrame | io.BytesIO
        Input dataset.
    received_col : str
        Amount received.
    requested_col : str
        Amount requested.
    group_by : list[str] | None
        Optional grouping (e.g., cluster, donor).
    percent : bool, default True
        If True, add percent received.

    Returns
    -------
    pl.DataFrame
        With placeholder percent and gap columns.
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

    received = pl.col(received_col).cast(pl.Float64)
    requested = pl.col(requested_col).cast(pl.Float64)
    pct = received / pl.when(requested == 0).then(None).otherwise(requested)
    if percent:
        pct = pct * 100.0
    gap = requested - received
    return df.with_columns([
        pct.alias("pct_received_placeholder"),
        gap.alias("funding_gap_placeholder")
    ])
