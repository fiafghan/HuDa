from huda.opening import open_csv
from huda.transformation import categorical_code_to_label
import polars as pl

df = open_csv("testdata/categ.csv")

print (df)

cov = categorical_code_to_label(
    data=df,
    code_column="sector",
    mapping={
        1:"food",
        2:"health",
        3:"sanitization"
    }
    )

print (cov)


