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
    OpenStreetMap Features (Hospitals, Schools) for Afghanistan
    -----------------------------------------------------------

    What this does:
    - Connects to OpenStreetMap using Overpass API.
    - Downloads features (like hospitals or schools) in a bounding box, and shows them on a map.

    When to use:
    - To quickly see facilities from OSM in an area (e.g., Kabul city hospitals).

    Why it is useful:
    - Free, up-to-date facility points that you can overlay on your analysis.

    Where to use (Afghan example):
    - BBOX around Kabul and tag {"amenity": "hospital"} to get hospitals.

    How to use (example):
    ```python
    from huda.geospatial import connect_with_openstreetmap

    # Hospitals around Kabul
    m = connect_with_openstreetmap(bbox=(34.3, 69.0, 34.8, 69.4), tags={"amenity": "hospital"})
    m.save("osm_kabul_hospitals.html")
    ```

    Output:
    - Interactive map with markers from OSM, each marker shows a name or tags.
    """
    # Unpack the bounding box into variables
    south, west, north, east = bbox

    # Build Overpass tag filters like ["amenity"="hospital"]["something"="value"]
    tag_filters = "".join([f"[\"{k}\"=\"{v}\"]" for k, v in tags.items()])

    # Build Overpass QL query to fetch nodes/ways/relations with those tags within bbox
    query = f"""
    [out:json][timeout:25];
    (
      node{tag_filters}({south},{west},{north},{east});
      way{tag_filters}({south},{west},{north},{east});
      relation{tag_filters}({south},{west},{north},{east});
    );
    out center;
    """.format(tag_filters=tag_filters, south=south, west=west, north=north, east=east)

    # Send the request to Overpass and parse JSON
    resp = requests.post(OVERPASS_API, data={"data": query})
    resp.raise_for_status()
    data = resp.json()

    # Create base map centered at the bbox center
    m = folium.Map(location=[(south + north) / 2.0, (west + east) / 2.0], tiles=tiles, zoom_start=zoom_start)

    # Loop over elements and plot points
    for el in data.get("elements", []):
        if "lat" in el and "lon" in el:             # node with direct coordinates
            lat, lon = el["lat"], el["lon"]
        elif "center" in el:                         # way/relation with a computed center
            c = el["center"]
            lat, lon = c.get("lat"), c.get("lon")
        else:
            continue                                  # skip if we can't plot it
        name = el.get("tags", {}).get("name", "")   # try to get a readable name
        popup_txt = name or ", ".join([f"{k}={v}" for k, v in el.get("tags", {}).items()])  # fallback to tags
        folium.Marker([lat, lon], popup=popup_txt).add_to(m)  # add marker

    # Return the map for saving as HTML
    return m
