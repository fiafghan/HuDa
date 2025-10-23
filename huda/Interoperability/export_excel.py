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


def export_excel(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    path: str,
    sheet_name: str = "Sheet1",
    include_header: bool = True
) -> Dict[str, Any]:
    """
    Export to Excel (placeholder intent)
    """
    df = _to_polars(data)
    return {
        "type": "export_excel",
        "path": path,
        "options": {"sheet_name": sheet_name, "include_header": include_header},
        "preview": {"rows": min(5, df.height), "columns": df.columns},
    }
