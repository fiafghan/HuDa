import polars as pl
import pandas as pd
from typing import Union, Optional, Dict, Any
import io


def _to_polars(data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO]) -> pl.DataFrame:
    if isinstance(data, str):
        return pl.read_csv(data)
    if isinstance(data, io.BytesIO):
        return pl.read_csv(data)
    if isinstance(data, pd.DataFrame):
        return pl.from_pandas(data)
    if isinstance(data, pl.DataFrame):
        return data
    raise TypeError("Unsupported data type")


def histogram(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    value_col: str,
    bins: Optional[int] = 10,
    title: Optional[str] = None
) -> Dict[str, Any]:
    """Histogram (placeholder spec)."""
    df = _to_polars(data)
    return {
        "type": "histogram",
        "title": title or "Histogram",
        "encoding": {"value": value_col, "bins": bins},
        "data_preview_rows": min(5, df.height),
    }
