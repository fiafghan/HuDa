import polars as pl
import pandas as pd
import folium
from typing import Union, Optional, Dict, Any


def choropleth_maps_by_region(
    data: Union[pd.DataFrame, pl.DataFrame],
    geojson: Union[Dict[str, Any], str],
    region_key: str,
    value_col: str,
    map_center: tuple[float, float] = (33.9391, 67.7100),
    zoom_start: int = 5,
    legend_name: Optional[str] = None,
    key_on: Optional[str] = None,
    fill_color: str = "YlOrRd",
    tiles: str = "CartoDB positron",
) -> folium.Map:
    """
    Choropleth Map by Afghan Provinces or Districts
    -----------------------------------------------

    What this does:
    - Colors each region (province/district) using your numeric value (e.g., severity).

    When to use:
    - To compare regions side-by-side (for example, severity by province in Afghanistan).

    Why it is useful:
    - Makes patterns by region easy to see (hotspots vs low values).

    Where to use (Afghan example):
    - Provinces Kabul, Herat, Balkh using a GeoJSON boundary file.

    How to use (example):
    ```python
    from huda.geospatial import choropleth_maps_by_region
    import polars as pl, json

    df = pl.DataFrame({
        "province": ["Kabul", "Herat", "Balkh"],
        "severity": [0.7, 0.4, 0.6],
    })

    with open("afg_provinces.geojson", "r") as f:
        gj = json.load(f)

    m = choropleth_maps_by_region(df, gj, region_key="province", value_col="severity",
                                  legend_name="Severity")
    m.save("choropleth_afg.html")
    ```

    Output:
    - Interactive map with colored regions and a legend.
    """
    # Convert Polars to Pandas if needed (Folium works with Pandas)
    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data

    # Create base map over Afghanistan
    m = folium.Map(location=list(map_center), zoom_start=zoom_start, tiles=tiles)

    # If key_on not given, join on a property with the same name as your region_key
    if key_on is None:
        key_on = f"feature.properties.{region_key}"

    # Add a choropleth (colored polygons) layer using your data and GeoJSON
    folium.Choropleth(
        geo_data=geojson,                  # GeoJSON with regions
        name="choropleth",                # Layer name
        data=df,                           # DataFrame with values
        columns=[region_key, value_col],   # Join columns [region, value]
        key_on=key_on,                     # GeoJSON property path to match region_key
        fill_color=fill_color,             # Color palette
        fill_opacity=0.5,                  # Polygon fill opacity
        line_opacity=0.2,                  # Border opacity
        legend_name=legend_name or value_col,  # Legend title
        nan_fill_color="lightgray",       # Color for missing regions
    ).add_to(m)

    # Allow toggling layers
    folium.LayerControl().add_to(m)

    # Return map to save as HTML
    return m
