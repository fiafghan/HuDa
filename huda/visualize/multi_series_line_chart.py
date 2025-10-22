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


def multi_series_line_chart(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    x_col: str,
    y_col: str,
    series_col: str,
    title: Optional[str] = None
) -> Dict[str, Any]:
    """Multi-series Line Chart (placeholder spec)."""
    df = _to_polars(data)
    return {
        "type": "line",
        "title": title or "Multi-series Line Chart",
        "encoding": {"x": x_col, "y": y_col, "series": series_col},
        "data_preview_rows": min(5, df.height),
    }
