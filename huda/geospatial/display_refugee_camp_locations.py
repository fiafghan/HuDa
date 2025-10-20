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
    Show Refugee/IDP Camp Locations (Afghanistan)
    --------------------------------------------

    What this does:
    - Puts a marker on the map for each camp location.
    - Can show the camp name in a popup.

    When to use:
    - To display IDP/refugee camps from your assessment or partner data.

    Why it is useful:
    - Easy to see where camps are located and share as HTML.

    Where to use (Afghan example):
    - Kabul IDP camps, Herat camps, etc.

    How to use (example):
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

    Output:
    - Interactive HTML map with red house icons for camps and optional names.
    """
    # Convert Polars to Pandas if needed for Folium
    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data

    # Create base map centered on Afghanistan
    m = folium.Map(location=[center_lat, center_lon], tiles=tiles, zoom_start=zoom_start)

    # Use a red 'home' icon for camps
    icon = folium.Icon(color="red", icon="home", prefix="fa")

    # Add a marker for each camp with valid coordinates
    for _, r in df.dropna(subset=[lat_col, lon_col]).iterrows():
        popup = None  # default no popup
        if name_col and name_col in df.columns:  # if a name column exists
            popup = folium.Popup(str(r[name_col]), parse_html=True)  # show the camp name
        folium.Marker([r[lat_col], r[lon_col]], icon=icon, popup=popup).add_to(m)  # add marker

    # Return the map to be saved as HTML
    return m
