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
    Show conflict-affected zones (polygons) with styling by conflict level.

    Parameters:
    - geojson: GeoJSON dict or path to a .geojson file with polygons and conflict attributes.
    - level_property: GeoJSON property indicating conflict level (e.g., low/medium/high).
    - map_center, zoom_start, tiles: base map options.

    Example (Afghanistan conflict polygons):
    ```python
    import json
    from huda.geospatial import conflict_zones_polygons

    with open("afg_conflict.geojson", "r") as f:
        gj = json.load(f)

    m = conflict_zones_polygons(gj, level_property="level")
    m.save("conflict_afg.html")
    ```
    """
    m = folium.Map(location=list(map_center), zoom_start=zoom_start, tiles=tiles)

    def style_function(feature):
        lvl = str(feature["properties"].get(level_property, "")).lower()
        color = "#9ecae1"  # default
        if "high" in lvl:
            color = "#cb181d"
        elif "medium" in lvl or "moderate" in lvl:
            color = "#fb6a4a"
        elif "low" in lvl:
            color = "#fcae91"
        return {"fillColor": color, "color": color, "weight": 1, "fillOpacity": 0.5}

    folium.GeoJson(
        data=geojson,
        style_function=style_function,
        name="Conflict Zones",
        tooltip=folium.GeoJsonTooltip(fields=[level_property], aliases=["Conflict level"]) if level_property else None,
    ).add_to(m)

    folium.LayerControl().add_to(m)
    return m
