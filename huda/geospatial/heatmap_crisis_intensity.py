import polars as pl
import pandas as pd
import folium
from folium.plugins import HeatMap
from typing import Union, Optional


def heatmap_crisis_intensity(
    data: Union[pd.DataFrame, pl.DataFrame],
    lat_col: str = "latitude",
    lon_col: str = "longitude",
    weight_col: Optional[str] = None,
    radius: int = 15,
    blur: int = 20,
    min_opacity: float = 0.3,
    tiles: str = "CartoDB dark_matter",
    zoom_start: int = 6,
    center_lat: float = 33.9391,
    center_lon: float = 67.7100,
) -> folium.Map:
    """
    Create a heatmap of crisis intensity using point data.

    Parameters:
    - data: pandas or polars DataFrame with coordinates and optional weights.
    - lat_col, lon_col: column names for latitude and longitude.
    - weight_col: optional column for heat intensity (e.g., number_in_need).
    - radius, blur, min_opacity: visual tuning parameters.
    - tiles: base map.

    Example (Afghanistan):
    ```python
    from huda.geospatial import heatmap_crisis_intensity
    import polars as pl

    df = pl.DataFrame({
        "latitude": [34.5553, 34.3482, 36.7280],
        "longitude": [69.2075, 62.1997, 66.8960],
        "people_in_need": [5000, 1200, 2200],
    })

    m = heatmap_crisis_intensity(df, weight_col="people_in_need")
    m.save("heatmap_afg.html")
    ```
    """
    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data

    m = folium.Map(location=[center_lat, center_lon], tiles=tiles, zoom_start=zoom_start)

    points = []
    if weight_col and weight_col in df.columns:
        for _, r in df.dropna(subset=[lat_col, lon_col, weight_col]).iterrows():
            points.append([r[lat_col], r[lon_col], float(r[weight_col])])
    else:
        for _, r in df.dropna(subset=[lat_col, lon_col]).iterrows():
            points.append([r[lat_col], r[lon_col], 1.0])

    HeatMap(points, radius=radius, blur=blur, min_opacity=min_opacity).add_to(m)
    return m
