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


def export_json(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    path: str,
    orient: str = "records",
    indent: Optional[int] = 2
) -> Dict[str, Any]:
    """
    Export to JSON (placeholder intent)
    """
    df = _to_polars(data)
    return {
        "type": "export_json",
        "path": path,
        "options": {"orient": orient, "indent": indent},
        "preview": {
            "rows": min(3, df.height),
            "columns": df.columns,
        },
    }
