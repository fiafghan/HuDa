from huda.opening import open_csv
from huda.validation_and_quality import negative_values_detection_where_they_should_not_exist
import polars as pl

df = open_csv("testdata/neg_value.csv")

print (df)

cov = negative_values_detection_where_they_should_not_exist(
    data=df,
    numeric_columns=["age", "food_provided", "water_liters"]
    )

print (cov)


