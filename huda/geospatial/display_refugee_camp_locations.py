import polars as pl
import pandas as pd
import folium
from typing import Union, Optional


def display_refugee_camp_locations(
    data: Union[pd.DataFrame, pl.DataFrame],
    lat_col: str = "latitude",
    lon_col: str = "longitude",
    name_col: Optional[str] = "camp_name",
    tiles: str = "OpenStreetMap",
    zoom_start: int = 6,
    center_lat: float = 33.9391,
    center_lon: float = 67.7100,
) -> folium.Map:
    """
    Display refugee/IDP camp locations on an interactive map.

    Parameters:
    - data: pandas or polars DataFrame containing camp locations.
    - lat_col, lon_col: coordinates.
    - name_col: optional popup name (e.g., "Shahr-e-Naw IDP Camp").

    Example (Afghanistan):
    ```python
    import polars as pl
    from huda.geospatial import display_refugee_camp_locations

    df = pl.DataFrame({
        "latitude": [34.5, 34.35],
        "longitude": [69.2, 62.2],
        "camp_name": ["Kabul IDP Camp", "Herat Camp"],
    })

    m = display_refugee_camp_locations(df)
    m.save("camps_afg.html")
    ```
    """
    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data

    m = folium.Map(location=[center_lat, center_lon], tiles=tiles, zoom_start=zoom_start)

    icon = folium.Icon(color="red", icon="home", prefix="fa")

    for _, r in df.dropna(subset=[lat_col, lon_col]).iterrows():
        popup = None
        if name_col and name_col in df.columns:
            popup = folium.Popup(str(r[name_col]), parse_html=True)
        folium.Marker([r[lat_col], r[lon_col]], icon=icon, popup=popup).add_to(m)

    return m
