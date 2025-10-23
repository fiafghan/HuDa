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


def export_sql_database(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    connection_uri: str,
    table_name: str,
    if_exists: str = "replace"
) -> Dict[str, Any]:
    """
    Export to SQL Database (placeholder intent)

    connection_uri example: postgresql://user:pass@host:5432/db
    if_exists: 'fail' | 'replace' | 'append'
    """
    df = _to_polars(data)
    return {
        "type": "export_sql",
        "connection_uri": connection_uri,
        "table_name": table_name,
        "options": {"if_exists": if_exists},
        "preview": {"rows": min(5, df.height), "columns": df.columns},
    }
