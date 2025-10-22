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


def bar_chart(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    category_col: str,
    value_col: str,
    orientation: str = "vertical",
    stacked: bool = False,
    color_col: Optional[str] = None,
    title: Optional[str] = None
) -> Dict[str, Any]:
    """
    Bar Chart (placeholder spec)
    ----------------------------

    Parameters
    ----------
    data : str | pd.DataFrame | pl.DataFrame | io.BytesIO
    category_col : str
    value_col : str
    orientation : str, default "vertical"
    stacked : bool, default False
    color_col : str | None
    title : str | None

    Returns
    -------
    dict
        Minimal placeholder chart spec.
    """
    df = _to_polars(data)
    return {
        "type": "bar",
        "title": title or "Bar Chart",
        "encoding": {
            "x": category_col if orientation == "vertical" else value_col,
            "y": value_col if orientation == "vertical" else category_col,
            "color": color_col,
            "stacked": stacked,
        },
        "data_preview_rows": min(5, df.height),
    }
