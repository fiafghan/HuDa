import polars as pl
import pandas as pd
import folium
from typing import Union, Optional
import io


def plot_data_on_map(
    data: Union[pd.DataFrame, pl.DataFrame],
    lat_col: str = "latitude",
    lon_col: str = "longitude",
    popup_col: Optional[str] = None,
    tiles: str = "OpenStreetMap",
    zoom_start: int = 6,
    center_lat: float = 33.9391,
    center_lon: float = 67.7100,
) -> folium.Map:
    """
    Plot point data on an interactive web map (Leaflet via Folium).

    What this does:
    - Places markers at each latitude/longitude.
    - Optional popups with any column.

    When to use:
    - Visualize survey sites, facility locations, or monitoring points in Afghanistan.

    Why important:
    - Quick visual QA of geocoded data. Easy to share as HTML.

    Where to apply:
    - Household assessments in Kabul/Herat/Balkh, health facility lists, distribution points.

    Parameters:
    - data: pandas or polars DataFrame with coordinates.
    - lat_col, lon_col: column names for latitude and longitude.
    - popup_col: optional column to show in marker popup (e.g., site name).
    - tiles: base tiles provider (e.g., "OpenStreetMap", "CartoDB positron").
    - zoom_start: initial zoom level.
    - center_lat, center_lon: map center (defaults to Afghanistan centroid).

    Returns:
    - folium.Map that you can save via map_obj.save("map.html").

    Afghanistan example:
    ```python
    import polars as pl
    from huda.geospatial import plot_data_on_map

    df = pl.DataFrame({
        "latitude": [34.5553, 34.3482, 36.7280],
        "longitude": [69.2075, 62.1997, 66.8960],
        "site": ["Kabul Site", "Herat Clinic", "Balkh School"],
    })

    m = plot_data_on_map(df, popup_col="site")
    m.save("afghanistan_points.html")
    ```
    """
    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data

    m = folium.Map(location=[center_lat, center_lon], tiles=tiles, zoom_start=zoom_start)

    for _, row in df.dropna(subset=[lat_col, lon_col]).iterrows():
        popup = None
        if popup_col and popup_col in df.columns:
            popup = folium.Popup(str(row[popup_col]), parse_html=True)
        folium.Marker(location=[row[lat_col], row[lon_col]], popup=popup).add_to(m)

    return m
