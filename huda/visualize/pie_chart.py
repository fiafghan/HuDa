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


def pie_chart(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    category_col: str,
    value_col: str,
    title: Optional[str] = None
) -> Dict[str, Any]:
    df = _to_polars(data)
    return {
        "type": "pie",
        "title": title or "Pie Chart",
        "encoding": {"category": category_col, "value": value_col},
        "data_preview_rows": min(5, df.height),
    }
