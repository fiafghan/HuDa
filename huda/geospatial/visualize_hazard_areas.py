import folium
from typing import Union, Dict, Any, Optional


def visualize_hazard_areas(
    geojson: Union[Dict[str, Any], str],
    hazard_property: str = "hazard_type",
    map_center: tuple[float, float] = (33.9391, 67.7100),
    zoom_start: int = 6,
    tiles: str = "CartoDB positron",
) -> folium.Map:
    """
    Visualize flood/drought-affected polygons as an interactive layer.

    Parameters:
    - geojson: GeoJSON dict or path to a .geojson file with polygons and a hazard attribute (e.g., flood/drought).
    - hazard_property: GeoJSON property that indicates hazard category.
    - map_center, zoom_start, tiles: base map options.

    Returns:
    - folium.Map with styled polygons per hazard.

    Example (Afghanistan flood/drought polygons):
    ```python
    import json
    from huda.geospatial import visualize_hazard_areas

    with open("afg_hazards.geojson", "r") as f:
        gj = json.load(f)

    m = visualize_hazard_areas(gj, hazard_property="hazard")
    m.save("hazards_afg.html")
    ```
    """
    m = folium.Map(location=list(map_center), zoom_start=zoom_start, tiles=tiles)

    def style_function(feature):
        h = str(feature["properties"].get(hazard_property, "")).lower()
        color = "#3182bd"  # default
        if "flood" in h:
            color = "#2c7fb8"
        elif "drought" in h:
            color = "#d95f0e"
        elif "landslide" in h:
            color = "#756bb1"
        return {"fillColor": color, "color": color, "weight": 1, "fillOpacity": 0.5}

    folium.GeoJson(
        data=geojson,
        style_function=style_function,
        name="Hazard Areas",
        tooltip=folium.GeoJsonTooltip(fields=[hazard_property], aliases=["Hazard"]) if hazard_property else None,
    ).add_to(m)

    folium.LayerControl().add_to(m)
    return m
