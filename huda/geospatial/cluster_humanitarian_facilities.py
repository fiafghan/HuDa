"""
Cluster Humanitarian Facilities (Simple Map for Afghanistan)
===========================================================

What this does:
- This function shows many facilities on one map and groups nearby ones into clusters.
- This helps when there are many points in a city (for example, Kabul) and markers overlap.

When to use it:
- When you have many locations like hospitals, schools, or distribution points.
- When you want a clean map that is easy to read and share.

Why it is useful:
- Clustering reduces visual clutter and makes the map faster and clearer.

Where to use (Afghanistan examples):
- Kabul health facilities list.
- Herat schools around the city.
- Balkh clinics from a survey.

How to use (example):
```python
import polars as pl
from huda.geospatial import cluster_humanitarian_facilities

df = pl.DataFrame({
    "latitude": [34.5553, 34.556, 34.557, 34.3482, 36.7280],
    "longitude": [69.2075, 69.208, 69.209, 62.1997, 66.8960],
    "facility": ["Kabul Hospital A", "Kabul Hospital B", "Clinic C", "Herat School", "Balkh School"],
})

m = cluster_humanitarian_facilities(df, name_col="facility")
m.save("facilities_cluster_afg.html")
```

Output:
- An interactive HTML map where markers are grouped in clusters.
- Clicking a cluster zooms in and shows individual facilities with optional names.
"""

# import polars for optional input as Polars DataFrame
import polars as pl  # We accept Polars input and convert to Pandas for Folium
# import pandas for Folium compatibility
import pandas as pd  # Folium works with Pandas DataFrame under the hood
# import folium for interactive maps
import folium  # Folium builds Leaflet maps in HTML
# import MarkerCluster plugin to group many markers
from folium.plugins import MarkerCluster  # Adds clustering behavior to markers
# import typing hints
from typing import Union, Optional  # For type hints and optional parameters


def cluster_humanitarian_facilities(
    data: Union[pd.DataFrame, pl.DataFrame],  # Data with latitude/longitude (Pandas or Polars)
    lat_col: str = "latitude",               # Column name for latitude
    lon_col: str = "longitude",              # Column name for longitude
    name_col: Optional[str] = None,           # Optional column shown in popup (like facility name)
    tiles: str = "CartoDB positron",         # Base map tiles (clean background)
    zoom_start: int = 6,                      # Initial zoom level (country-level)
    center_lat: float = 33.9391,              # Default center latitude (Afghanistan)
    center_lon: float = 67.7100,              # Default center longitude (Afghanistan)
) -> folium.Map:                             # Returns a Folium Map object
    """
    Create a clustered facilities map from a table of latitude/longitude.

    Parameters:
    - data: Pandas or Polars DataFrame with columns for latitude/longitude and optional name.
    - lat_col, lon_col: Column names for coordinates in decimal degrees (WGS84).
    - name_col: Optional text to show in a popup for each facility (e.g., hospital name).
    - tiles: Map background style.
    - zoom_start: Starting zoom (6 is good for country view).
    - center_lat, center_lon: Map center (defaults to Afghanistan).

    Returns:
    - folium.Map with clustered markers you can save as HTML.
    """
    # If the input is Polars, convert to Pandas for Folium
    if isinstance(data, pl.DataFrame):  # Check if data is a Polars DataFrame
        df = data.to_pandas()           # Convert to a Pandas DataFrame
    else:
        df = data                       # Otherwise keep the Pandas DataFrame

    # Create a base map centered over Afghanistan with the chosen tiles and zoom
    m = folium.Map(location=[center_lat, center_lon], tiles=tiles, zoom_start=zoom_start)

    # Add a cluster layer to group nearby markers automatically
    cluster = MarkerCluster().add_to(m)

    # Loop over each row that has valid latitude and longitude
    for _, r in df.dropna(subset=[lat_col, lon_col]).iterrows():  # Skip rows with missing coords
        popup = None                                             # Default no popup
        if name_col and name_col in df.columns:                  # If a name column is provided and exists
            popup = folium.Popup(str(r[name_col]), parse_html=True)  # Build a popup with the facility name
        # Add a marker for this facility into the cluster group
        folium.Marker([r[lat_col], r[lon_col]], popup=popup).add_to(cluster)

    # Return the finished map so the caller can save it
    return m
