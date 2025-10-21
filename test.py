from huda.geospatial import heatmap_crisis_intensity
import polars as pl

df = pl.DataFrame({
    "latitude": [34.5553, 34.3482, 36.7280],
    "longitude": [69.2075, 62.1997, 66.8960],
    "people_in_need": [500000, 1200, 2200],
})

m = heatmap_crisis_intensity(df, weight_col="people_in_need")
m.save("testdata/heatmap_afg.html")