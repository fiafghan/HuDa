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
    Hazard Areas Map (Flood/Drought) for Afghanistan
    -----------------------------------------------

    What this does:
    - Draws polygons (areas) for hazards like flood, drought, landslide.
    - Colors them differently so you can see hazard types.

    When to use:
    - To visualize areas affected by hazards from your GeoJSON layer.

    Why it is useful:
    - Helps planners and analysts quickly see hazard coverage.

    Where to use (Afghan example):
    - Flood polygons around Kabul River, drought-affected districts in the west.

    How to use (example):
    ```python
    import json
    from huda.geospatial import visualize_hazard_areas

    with open("afg_hazards.geojson", "r") as f:
        gj = json.load(f)

    m = visualize_hazard_areas(gj, hazard_property="hazard")
    m.save("hazards_afg.html")
    ```

    Output:
    - Interactive HTML map with colored hazard polygons and tooltips showing the hazard type.
    """
    # Create a map centered on Afghanistan
    m = folium.Map(location=list(map_center), zoom_start=zoom_start, tiles=tiles)

    # Style polygons based on hazard type text
    def style_function(feature):
        h = str(feature["properties"].get(hazard_property, "")).lower()  # read hazard text
        color = "#3182bd"  # default color
        if "flood" in h:
            color = "#2c7fb8"  # blue
        elif "drought" in h:
            color = "#d95f0e"  # orange
        elif "landslide" in h:
            color = "#756bb1"  # purple
        return {"fillColor": color, "color": color, "weight": 1, "fillOpacity": 0.5}

    # Add polygons to the map with tooltips
    folium.GeoJson(
        data=geojson,  # the GeoJSON data or path
        style_function=style_function,  # color by hazard
        name="Hazard Areas",  # layer name
        tooltip=folium.GeoJsonTooltip(fields=[hazard_property], aliases=["Hazard"]) if hazard_property else None,
    ).add_to(m)

    # Add a layer control to toggle
    folium.LayerControl().add_to(m)
    # Return the final map
    return m
