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


def export_stata(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    path: str,
    version: int = 118
) -> Dict[str, Any]:
    """
    Export to Stata (.dta) (placeholder intent)
    """
    df = _to_polars(data)
    return {
        "type": "export_stata",
        "path": path,
        "options": {"version": version},
        "preview": {"rows": min(5, df.height), "columns": df.columns},
    }


def export_spss(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    path: str
) -> Dict[str, Any]:
    """
    Export to SPSS (.sav) (placeholder intent)
    """
    df = _to_polars(data)
    return {
        "type": "export_spss",
        "path": path,
        "options": {},
        "preview": {"rows": min(5, df.height), "columns": df.columns},
    }
