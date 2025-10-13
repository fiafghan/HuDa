from huda.opening import open_csv
from huda.validation_and_quality import mandatory_fields_check
import polars as pl

df = open_csv("testdata/mandatory_fields_check.csv")

print (df)

cov = mandatory_fields_check(
    data=df,
    mandatory_fields=["gender", "age", "sector"]
    )

print (cov)


