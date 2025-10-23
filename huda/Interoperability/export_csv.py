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


def export_csv(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    path: str,
    include_header: bool = True,
    delimiter: str = ",",
    encoding: str = "utf-8"
) -> Dict[str, Any]:
    """
    Export to CSV (placeholder intent)

    Returns a spec describing the intended CSV export without writing files.
    """
    df = _to_polars(data)
    return {
        "type": "export_csv",
        "path": path,
        "options": {
            "include_header": include_header,
            "delimiter": delimiter,
            "encoding": encoding,
        },
        "preview": {
            "rows": min(5, df.height),
            "columns": df.columns,
        },
    }
