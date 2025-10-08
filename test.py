from huda.opening import open_csv
from huda.transformation import adults_children_male_female_ratios
import polars as pl

df = open_csv("testdata/demographics.csv")

print (df)

dem = adults_children_male_female_ratios(df, numerator_columns=['male'], denominator_columns=['female'])

print (dem)


