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
    Simple Points Map for Afghanistan
    ---------------------------------

    What this does:
    - Shows each row as a point on an interactive map using latitude/longitude.
    - Can show a small popup with site name or any other column.

    When to use:
    - To quickly see survey locations, clinics, schools, or distribution points on a map.

    Why it is useful:
    - Fast quality check for coordinates and easy to share as HTML with colleagues.

    Where to use (Afghan example):
    - Kabul, Herat, Balkh survey points from a household assessment.

    How to use (example):
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

    Output:
    - Interactive HTML map with markers. Clicking shows the popup text (if given).
    """
    # If data is a Polars DataFrame, convert it to Pandas for Folium compatibility
    if isinstance(data, pl.DataFrame):  # check if input is polars
        df = data.to_pandas()           # convert to pandas
    else:
        df = data                       # already pandas

    # Create the base map centered over Afghanistan with the chosen tiles and zoom
    m = folium.Map(location=[center_lat, center_lon], tiles=tiles, zoom_start=zoom_start)

    # Loop over all rows that have non-missing latitude and longitude
    for _, row in df.dropna(subset=[lat_col, lon_col]).iterrows():
        # Prepare popup text if a popup column was provided and exists
        popup = None
        if popup_col and popup_col in df.columns:
            popup = folium.Popup(str(row[popup_col]), parse_html=True)
        # Add a marker for this point onto the map
        folium.Marker(location=[row[lat_col], row[lon_col]], popup=popup).add_to(m)

    # Return the map object so the caller can save it to HTML
    return m
