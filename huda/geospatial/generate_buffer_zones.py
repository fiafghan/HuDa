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
    Draw Buffer Zones Around Points (Afghanistan)
    --------------------------------------------

    What this does:
    - Draws a circle (buffer) around each point. You choose the size in meters.

    When to use:
    - To show service coverage (for example, a 50 km area around a hospital).

    Why it is useful:
    - Easy way to communicate reach and access on a simple map.

    Where to use (Afghan example):
    - 50 km around Kabul and Herat sites from a survey.

    How to use (example):
    ```python
    import polars as pl
    from huda.geospatial import generate_buffer_zones

    df = pl.DataFrame({
        "latitude": [34.5553, 34.3482],
        "longitude": [69.2075, 62.1997],
        "site": ["Kabul", "Herat"],
    })

    m = generate_buffer_zones(df, radius_meters=50_000, popup_col="site")
    m.save("buffers_50km_afg.html")
    ```

    Output:
    - Interactive HTML map with blue circles around each point.
    """
    # Convert to Pandas if we got a Polars DataFrame
    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data

    # Build the base map centered on Afghanistan
    m = folium.Map(location=[center_lat, center_lon], tiles=tiles, zoom_start=zoom_start)

    # For each point, add a circle with the chosen radius
    for _, r in df.dropna(subset=[lat_col, lon_col]).iterrows():
        popup = folium.Popup(str(r[popup_col]), parse_html=True) if popup_col and popup_col in df.columns else None
        folium.Circle(
            location=[r[lat_col], r[lon_col]],  # center of the circle
            radius=radius_meters,               # radius in meters
            color="#2b8cbe",                   # blue outline
            fill=True,                           # fill circle
            fill_opacity=0.2,                    # transparent fill
            popup=popup,                         # optional label
        ).add_to(m)

    # Return the map for saving to HTML
    return m
