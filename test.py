from huda.opening import open_csv
from huda.transformation import percentage_calculation
import polars as pl

df = open_csv("testdata/percentage.csv")

print (df)

percent = percentage_calculation(df, numerator_columns=['population', 'students', 'vaccinated'], denominator_column="population")

print (percent)


