from huda.opening import open_csv
from huda.transformation import needs_coverage_calculation
import polars as pl

df = open_csv("testdata/needs_coverage.csv")

print (df)

cov = needs_coverage_calculation(
            data=df,
            needs_columns=["food_needs_persons", "water_needs_liters", "shelter_needs_hh"],
            provided_columns=["food_provided_persons", "water_provided_liters", "shelter_provided_hh"],
            group_by_cols=["location", "date"]
    )

print (cov)


