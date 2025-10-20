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
    Overlay multiple numeric indicators as colored circle markers with layer control.

    Parameters:
    - data: pandas or polars DataFrame with coordinates and indicator columns.
    - indicators: mapping of {layer_name: column_name} to visualize per layer.
    - color_fn: optional function that accepts a pandas Series of values and returns a color hex.
      If None, a default simple color scale will be used per layer.

    Example (Afghanistan):
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
    """
    if indicators is None:
        indicators = {}

    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data

    m = folium.Map(location=[center_lat, center_lon], tiles=tiles, zoom_start=zoom_start)

    def default_color_scale(v: float, vmin: float, vmax: float) -> str:
        # simple red-green scale
        if v is None:
            return "#808080"
        if vmax == vmin:
            return "#2b8cbe"
        t = (float(v) - vmin) / (vmax - vmin)
        r = int(255 * t)
        g = int(255 * (1 - t))
        return f"#{r:02x}{g:02x}55"

    for layer_name, col in indicators.items():
        if col not in df.columns:
            continue
        group = folium.FeatureGroup(name=layer_name, show=True)
        series = df[col]
        vmin, vmax = pd.to_numeric(series, errors="coerce").min(), pd.to_numeric(series, errors="coerce").max()
        for _, r in df.dropna(subset=[lat_col, lon_col]).iterrows():
            val = r.get(col, None)
            color = color_fn(series) if callable(color_fn) else default_color_scale(val, vmin, vmax)
            folium.CircleMarker(
                location=[r[lat_col], r[lon_col]],
                radius=6,
                color=color,
                fill=True,
                fill_opacity=0.8,
                popup=folium.Popup(f"{layer_name}: {val}", parse_html=True),
            ).add_to(group)
        group.add_to(m)

    folium.LayerControl().add_to(m)
    return m
