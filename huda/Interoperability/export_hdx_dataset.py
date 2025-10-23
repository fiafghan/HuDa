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


def export_hdx_dataset(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    dataset_name: str,
    organization: str,
    license_name: str = "cc-by",
    private: bool = False
) -> Dict[str, Any]:
    """
    Export to HDX-compatible dataset (placeholder intent)

    Returns a spec that could be used by an HDX uploader.
    """
    df = _to_polars(data)
    return {
        "type": "export_hdx",
        "dataset_name": dataset_name,
        "organization": organization,
        "options": {"license": license_name, "private": private},
        "preview": {"rows": min(5, df.height), "columns": df.columns},
    }
