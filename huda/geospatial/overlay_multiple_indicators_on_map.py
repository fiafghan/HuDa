import polars as pl
import pandas as pd
import folium
from typing import Union, Optional, Dict, Callable


def overlay_multiple_indicators_on_map(
    data: Union[pd.DataFrame, pl.DataFrame],
    lat_col: str = "latitude",
    lon_col: str = "longitude",
    indicators: Dict[str, str] = None,
    color_fn: Optional[Callable[[pd.Series], str]] = None,
    tiles: str = "CartoDB positron",
    zoom_start: int = 6,
    center_lat: float = 33.9391,
    center_lon: float = 67.7100,
) -> folium.Map:
    """
    Overlay Multiple Indicators (Simple Afghan Map)
    ----------------------------------------------

    What this does:
    - Adds multiple layers of colored circle markers to one map, one layer for each indicator.
    - You can turn layers on/off using the layer control.

    When to use:
    - To compare two or more indicators on the same map (e.g., need index and coverage).

    Why it is useful:
    - Quick visual comparison across indicators at the same locations.

    Where to use (Afghan example):
    - Household assessment points in Kabul, Herat, Balkh with columns like `need_index` and `coverage`.

    How to use (example):
    ```python
    from huda.geospatial import overlay_multiple_indicators_on_map
    import polars as pl

    df = pl.DataFrame({
        "latitude": [34.5553, 34.3482, 36.7280],
        "longitude": [69.2075, 62.1997, 66.8960],
        "need_index": [0.8, 0.3, 0.6],
        "coverage": [40, 75, 55],
    })

    m = overlay_multiple_indicators_on_map(
        df,
        indicators={"Need Index": "need_index", "Coverage %": "coverage"}
    )
    m.save("overlay_indicators_afg.html")
    ```

    Output:
    - Interactive map with a layer per indicator and a legend-like layer control.
    """
    if indicators is None:
        indicators = {}  # default to empty dict if not provided

    if isinstance(data, pl.DataFrame):   # if polars is given
        df = data.to_pandas()            # convert to pandas
    else:
        df = data                        # already pandas

    m = folium.Map(location=[center_lat, center_lon], tiles=tiles, zoom_start=zoom_start)  # base map

    def default_color_scale(v: float, vmin: float, vmax: float) -> str:
        # simple red-green scale
        if v is None:
            return "#808080"  # gray when no value
        if vmax == vmin:
            return "#2b8cbe"  # blue if no range
        t = (float(v) - vmin) / (vmax - vmin)  # normalize 0..1
        r = int(255 * t)
        g = int(255 * (1 - t))
        return f"#{r:02x}{g:02x}55"  # build hex color

    for layer_name, col in indicators.items():
        if col not in df.columns:  # skip missing columns
            continue
        group = folium.FeatureGroup(name=layer_name, show=True)  # one layer per indicator
        series = df[col]  # the indicator series
        vmin, vmax = pd.to_numeric(series, errors="coerce").min(), pd.to_numeric(series, errors="coerce").max()  # min/max
        for _, r in df.dropna(subset=[lat_col, lon_col]).iterrows():  # loop valid points
            val = r.get(col, None)  # value for this indicator
            color = color_fn(series) if callable(color_fn) else default_color_scale(val, vmin, vmax)  # color choice
            folium.CircleMarker(
                location=[r[lat_col], r[lon_col]],  # point location
                radius=6,                            # marker size
                color=color,                          # outline color
                fill=True,                            # fill circle
                fill_opacity=0.8,                     # fill opacity
                popup=folium.Popup(f"{layer_name}: {val}", parse_html=True),  # show value in popup
            ).add_to(group)
        group.add_to(m)  # add the whole layer to the map

    folium.LayerControl().add_to(m)  # allow toggling layers
    return m  # return the final map
