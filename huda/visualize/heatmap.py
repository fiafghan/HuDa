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


def heatmap(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    x_col: str,
    y_col: str,
    value_col: str,
    title: Optional[str] = None,
    scale: str = "sequential"
) -> Dict[str, Any]:
    """Heatmap (placeholder spec)."""
    df = _to_polars(data)
    return {
        "type": "heatmap",
        "title": title or "Heatmap",
        "encoding": {"x": x_col, "y": y_col, "value": value_col, "scale": scale},
        "data_preview_rows": min(5, df.height),
    }
