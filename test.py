from huda.opening import open_csv
from huda.transformation import time_based_data_aggregration
import polars as pl

df = open_csv("testdata/agg_time.csv")

print (df)

agg = time_based_data_aggregration(df, frequency="monthly", date_column_name="date",aggregation_method="sum")

print (agg)


