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


def export_shapefile(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    path: str,
    geometry_col: str = "geometry",
    crs_epsg: int = 4326
) -> Dict[str, Any]:
    """
    Export to ESRI Shapefile (placeholder intent)
    """
    df = _to_polars(data)
    return {
        "type": "export_shapefile",
        "path": path,
        "options": {"geometry_col": geometry_col, "crs_epsg": crs_epsg},
        "preview": {"rows": min(5, df.height), "columns": df.columns},
    }


essential_geojson_keys = ["type", "features"]

def export_geojson(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    path: str,
    geometry_col: str = "geometry",
    crs_epsg: int = 4326
) -> Dict[str, Any]:
    """
    Export to GeoJSON (placeholder intent)
    """
    df = _to_polars(data)
    return {
        "type": "export_geojson",
        "path": path,
        "options": {"geometry_col": geometry_col, "crs_epsg": crs_epsg},
        "preview": {"rows": min(5, df.height), "columns": df.columns},
    }
