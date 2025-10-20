import polars as pl
from huda.geospatial import conflict_zones_polygons
from huda.opening import open_geojson


gdf,df = open_geojson("testdata/afg_conflict.geojson")


m = conflict_zones_polygons(gdf)
m.save("testdata/conflict_afg.html")



