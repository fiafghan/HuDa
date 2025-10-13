from huda.opening import open_csv
from huda.transformation import z_score_calculation
import polars as pl

df = open_csv("testdata/zscore.csv")

print (df)

cov = z_score_calculation(
    data=df,
    column="amount",
    threshold=3.0,
    )

print (cov)


