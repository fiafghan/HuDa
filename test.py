from huda.opening import open_csv
from huda.transformation import adults_children_ratios
import polars as pl

df = open_csv("testdata/demographics.csv")

print (df)

dem = adults_children_ratios(df, numerator_columns=['children'], denominator_columns=['adults'])

print (dem)


