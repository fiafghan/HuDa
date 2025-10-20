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
    Create a choropleth map by country/region using a GeoJSON boundary layer.

    Parameters:
    - data: pandas or polars DataFrame containing a region identifier and a value column.
    - geojson: GeoJSON dict or path to a .geojson file with the regions.
    - region_key: column in data that matches a GeoJSON property (e.g., "ADM1_EN", "iso3").
    - value_col: numeric column to visualize.
    - map_center: initial map center (default Afghanistan centroid).
    - zoom_start: initial zoom level.
    - legend_name: legend title.
    - key_on: property path in GeoJSON to join on (e.g., "feature.properties.ADM1_EN").
      If None, tries "feature.properties." + region_key.
    - fill_color: color scale.
    - tiles: base tiles provider.

    Returns:
    - folium.Map with a choropleth layer.

    Example (Afghanistan provinces):
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
    """
    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data

    m = folium.Map(location=list(map_center), zoom_start=zoom_start, tiles=tiles)

    if key_on is None:
        key_on = f"feature.properties.{region_key}"

    folium.Choropleth(
        geo_data=geojson,
        name="choropleth",
        data=df,
        columns=[region_key, value_col],
        key_on=key_on,
        fill_color=fill_color,
        fill_opacity=0.5,
        line_opacity=0.2,
        legend_name=legend_name or value_col,
        nan_fill_color="lightgray",
    ).add_to(m)

    folium.LayerControl().add_to(m)

    return m
