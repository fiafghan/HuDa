from huda.opening import open_csv
from huda.transformation import averages_weighted_population
import polars as pl

df = open_csv("testdata/avg_weighted.csv")

print (df)

cov = averages_weighted_population(
           data = df,
           needs_columns=['food_needs', 'water_needs', 'shelter_needs'],
           provided_columns=['food_provided', 'water_provided', 'shelter_provided'],
           population_column="population"
    )

print (cov)


