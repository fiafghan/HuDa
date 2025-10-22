from huda.opening import open_geojson
from huda.geospatial import visualize_hazard_areas

gdf, df = open_geojson("testdata/hazard.geojson")

m = visualize_hazard_areas(gdf, hazard_property="hazard_type")
m.save("testdata/hazard.html")