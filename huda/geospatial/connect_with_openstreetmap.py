import folium
import pandas as pd
import polars as pl
import requests
from typing import Optional, Dict, Any, Union, List, Tuple


OVERPASS_API = "https://overpass-api.de/api/interpreter"


def connect_with_openstreetmap(
    bbox: Tuple[float, float, float, float],
    tags: Dict[str, str] = {"amenity": "hospital"},
    tiles: str = "OpenStreetMap",
    zoom_start: int = 8,
) -> folium.Map:
    """
    Connect to OpenStreetMap (Overpass API) and plot features (e.g., hospitals, schools).

    Parameters:
    - bbox: (south, west, north, east) bounding box in WGS84.
      Example for Kabul approximate bbox: (34.3, 69.0, 34.8, 69.4)
    - tags: key/value mapping to filter features, e.g., {"amenity": "hospital"} or
      {"amenity": "school"}.
    - tiles, zoom_start: map options.

    Returns:
    - folium.Map with fetched OSM features plotted as markers.

    Afghanistan example:
    ```python
    from huda.geospatial import connect_with_openstreetmap

    # Hospitals around Kabul
    m = connect_with_openstreetmap(bbox=(34.3, 69.0, 34.8, 69.4), tags={"amenity": "hospital"})
    m.save("osm_kabul_hospitals.html")
    ```
    """
    south, west, north, east = bbox

    tag_filters = "".join([f"[\"{k}\"=\"{v}\"]" for k, v in tags.items()])
    query = f"""
    [out:json][timeout:25];
    (
      node{tag_filters}({south},{west},{north},{east});
      way{tag_filters}({south},{west},{north},{east});
      relation{tag_filters}({south},{west},{north},{east});
    );
    out center;
    """.format(tag_filters=tag_filters, south=south, west=west, north=north, east=east)

    resp = requests.post(OVERPASS_API, data={"data": query})
    resp.raise_for_status()
    data = resp.json()

    m = folium.Map(location=[(south + north) / 2.0, (west + east) / 2.0], tiles=tiles, zoom_start=zoom_start)

    for el in data.get("elements", []):
        if "lat" in el and "lon" in el:
            lat, lon = el["lat"], el["lon"]
        elif "center" in el:
            c = el["center"]
            lat, lon = c.get("lat"), c.get("lon")
        else:
            continue
        name = el.get("tags", {}).get("name", ")")
        popup_txt = name or ", ".join([f"{k}={v}" for k, v in el.get("tags", {}).items()])
        folium.Marker([lat, lon], popup=popup_txt).add_to(m)

    return m
