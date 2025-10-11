from huda.opening import open_csv
from huda.transformation import gender_group_standardization
import polars as pl

df = open_csv("testdata/gnd_stand.csv")

print (df)

cov = gender_group_standardization(
    data = df, 
    gender_column="gender"
    )

print (cov)


