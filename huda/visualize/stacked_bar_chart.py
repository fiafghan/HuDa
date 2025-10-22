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


def stacked_bar_chart(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    category_col: str,
    value_col: str,
    stack_col: str,
    title: Optional[str] = None
) -> Dict[str, Any]:
    """Stacked Bar Chart (placeholder spec)."""
    df = _to_polars(data)
    return {
        "type": "bar",
        "title": title or "Stacked Bar Chart",
        "encoding": {
            "x": category_col,
            "y": value_col,
            "stack": stack_col,
            "stacked": True,
        },
        "data_preview_rows": min(5, df.height),
    }
