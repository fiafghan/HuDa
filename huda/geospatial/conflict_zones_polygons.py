import folium
from typing import Union, Dict, Any, Optional


def conflict_zones_polygons(
    geojson: Union[Dict[str, Any], str],
    level_property: str = "conflict_level",
    map_center: tuple[float, float] = (33.9391, 67.7100),
    zoom_start: int = 6,
    tiles: str = "CartoDB positron",
) -> folium.Map:
    """
    Conflict Zones Map (Afghanistan)
    -------------------------------

    What this does:
    - Draws polygons for conflict-affected areas and colors them by level (low/medium/high).

    When to use:
    - To present conflict intensity by district or province from a GeoJSON layer.

    Why it is useful:
    - Clear picture of where the conflict impacts are stronger.

    Where to use (Afghan example):
    - District polygons with a property like `level` = low/medium/high.

    How to use (example):
    ```python
    import json
    from huda.geospatial import conflict_zones_polygons

    with open("afg_conflict.geojson", "r") as f:
        gj = json.load(f)

    m = conflict_zones_polygons(gj, level_property="level")
    m.save("conflict_afg.html")
    ```

    Output:
    - Interactive map with colored polygons and a tooltip showing conflict level.
    """
    # Create base map over Afghanistan
    m = folium.Map(location=list(map_center), zoom_start=zoom_start, tiles=tiles)

    # Style polygons based on conflict level text
    def style_function(feature):
        lvl = str(feature["properties"].get(level_property, "")).lower()  # read conflict level
        color = "#9ecae1"  # default light blue
        if "high" in lvl:
            color = "#cb181d"   # red for high
        elif "medium" in lvl or "moderate" in lvl:
            color = "#fb6a4a"   # orange for medium
        elif "low" in lvl:
            color = "#fcae91"   # light orange for low
        return {"fillColor": color, "color": color, "weight": 1, "fillOpacity": 0.5}

    # Add polygons to the map with optional tooltip
    folium.GeoJson(
        data=geojson,
        style_function=style_function,
        name="Conflict Zones",
        tooltip=folium.GeoJsonTooltip(fields=[level_property], aliases=["Conflict level"]) if level_property else None,
    ).add_to(m)

    # Layer control to toggle
    folium.LayerControl().add_to(m)
    return m
