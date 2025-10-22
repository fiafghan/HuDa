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


def bubble_chart(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    x_col: str,
    y_col: str,
    size_col: str,
    color_col: Optional[str] = None,
    title: Optional[str] = None
) -> Dict[str, Any]:
    """Bubble Chart (placeholder spec)."""
    df = _to_polars(data)
    return {
        "type": "bubble",
        "title": title or "Bubble Chart",
        "encoding": {"x": x_col, "y": y_col, "size": size_col, "color": color_col},
        "data_preview_rows": min(5, df.height),
    }
