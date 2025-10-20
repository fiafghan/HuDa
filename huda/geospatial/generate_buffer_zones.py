import polars as pl
import pandas as pd
import folium
from typing import Union, Optional


def generate_buffer_zones(
    data: Union[pd.DataFrame, pl.DataFrame],
    lat_col: str = "latitude",
    lon_col: str = "longitude",
    radius_meters: float = 50000.0,
    tiles: str = "CartoDB positron",
    zoom_start: int = 6,
    center_lat: float = 33.9391,
    center_lon: float = 67.7100,
    popup_col: Optional[str] = None,
) -> folium.Map:
    """
    Generate circular buffer zones (meters) around points, e.g., 50km radius.

    Parameters:
    - data: pandas or polars DataFrame with coordinates.
    - radius_meters: buffer radius (e.g., 50_000 for 50km).
    - popup_col: optional popup label column.

    Example (Afghanistan 50km buffers):
    ```python
    import polars as pl
    from huda.geospatial import generate_buffer_zones

    df = pl.DataFrame({
        "latitude": [34.5553, 34.3482],
        "longitude": [69.2075, 62.1997],
        "site": ["Kabul", "Herat"],
    })

    m = generate_buffer_zones(df, radius_meters=50000, popup_col="site")
    m.save("buffers_50km_afg.html")
    ```
    """
    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data

    m = folium.Map(location=[center_lat, center_lon], tiles=tiles, zoom_start=zoom_start)

    for _, r in df.dropna(subset=[lat_col, lon_col]).iterrows():
        popup = folium.Popup(str(r[popup_col]), parse_html=True) if popup_col and popup_col in df.columns else None
        folium.Circle(
            location=[r[lat_col], r[lon_col]],
            radius=radius_meters,
            color="#2b8cbe",
            fill=True,
            fill_opacity=0.2,
            popup=popup,
        ).add_to(m)

    return m
