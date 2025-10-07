from huda.opening import open_csv
from huda.transformation import aggregate_data_by_region

df = open_csv("testdata/sample_afghanistan_regions.csv")

print (df)

agg = aggregate_data_by_region(df, region_col="Region", agg_method="mean")

print (agg)

df = agg.write_csv("testdata/agg.csv")
