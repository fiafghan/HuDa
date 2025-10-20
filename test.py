import polars as pl
import json
from pathlib import Path
from huda.geospatial import choropleth_maps_by_region

# Load CSV (با polars)
df = pl.read_csv("testdata/prov.csv")

# Load GeoJSON
with open("testdata/afg_provinces.geojson", "r", encoding="utf-8") as f:
    gj = json.load(f)

# Create map
m = choropleth_maps_by_region(
    data=df,
    geojson=gj,
    region_key="province",
    value_col="severity",
    legend_name="Severity (Example Data)",
)

# Save to HTML
output = Path("testdata/choropleth_afg.html")
m.save(output)

print(f"✅ Map saved to {output.absolute()}")





