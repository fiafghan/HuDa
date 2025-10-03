from huda.geojson import open_geojson

gdf, df = open_geojson("testdata/test.geojson")

print(gdf)
print(df)