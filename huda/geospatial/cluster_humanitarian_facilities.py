import polars as pl
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from typing import Union, Optional


def cluster_humanitarian_facilities(
    data: Union[pd.DataFrame, pl.DataFrame],
    lat_col: str = "latitude",
    lon_col: str = "longitude",
    name_col: Optional[str] = None,
    tiles: str = "CartoDB positron",
    zoom_start: int = 6,
    center_lat: float = 33.9391,
    center_lon: float = 67.7100,
) -> folium.Map:
    """
    Cluster humanitarian facilities (e.g., hospitals, schools) to avoid marker clutter.

    Parameters:
    - data: pandas or polars DataFrame with facility coordinates.
    - name_col: optional facility name to show in popup.

    Example (Afghanistan facilities):
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
    """
    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data

    m = folium.Map(location=[center_lat, center_lon], tiles=tiles, zoom_start=zoom_start)
    cluster = MarkerCluster().add_to(m)

    for _, r in df.dropna(subset=[lat_col, lon_col]).iterrows():
        popup = None
        if name_col and name_col in df.columns:
            popup = folium.Popup(str(r[name_col]), parse_html=True)
        folium.Marker([r[lat_col], r[lon_col]], popup=popup).add_to(cluster)

    return m
