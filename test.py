from huda.opening import open_csv
from huda.validation_and_quality import country_code_validation
import polars as pl

df = open_csv("testdata/country_code.csv")

print (df)

cov = country_code_validation(
    data=df,
    country_column="country",
    )

print (cov)


