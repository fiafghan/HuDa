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
    Heatmap for Crisis Intensity in Afghanistan
    ------------------------------------------

    What this does:
    - Draws a heatmap from points. Brighter areas mean higher values or more points.

    When to use:
    - To see hotspots of need or incidents (for example, more people in need in Kabul).

    Why it is useful:
    - Quickly shows where the situation is most intense.

    Where to use (Afghan example):
    - Points from assessments in Kabul, Herat, Balkh with a "people_in_need" column.

    How to use (example):
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

    Output:
    - Interactive heatmap. Areas with bigger numbers look hotter/brighter.
    """
    # Convert Polars to Pandas if needed
    if isinstance(data, pl.DataFrame):      # check for Polars input
        df = data.to_pandas()               # convert to Pandas DataFrame
    else:
        df = data                          # already Pandas

    # Create a dark base map centered on Afghanistan
    m = folium.Map(location=[center_lat, center_lon], tiles=tiles, zoom_start=zoom_start)

    # Build list of points with optional weights
    points = []
    if weight_col and weight_col in df.columns:  # if a weight column is provided
        for _, r in df.dropna(subset=[lat_col, lon_col, weight_col]).iterrows():
            points.append([r[lat_col], r[lon_col], float(r[weight_col])])  # lat, lon, weight
    else:
        for _, r in df.dropna(subset=[lat_col, lon_col]).iterrows():
            points.append([r[lat_col], r[lon_col], 1.0])  # equal weight for each point

    # Add heatmap layer to the map
    HeatMap(points, radius=radius, blur=blur, min_opacity=min_opacity).add_to(m)
    # Return the map for saving as HTML
    return m
