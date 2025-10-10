from huda.opening import open_csv
from huda.transformation import severity_index_calculation
import polars as pl

df = open_csv("testdata/severity.csv")

print (df)

gr = severity_index_calculation(
        data=df,
        indicator_columns=["affected_people", "food_insecurity_score", "water_access_score", "displacement_count"],
        reverse_indicators=["water_access_score"] # Tell the function to flip 'water_access_pct'
    )

print (gr)


