from huda.opening import open_csv
from huda.transformation import pivot_unpivot
import polars as pl

df = open_csv("testdata/unpivot.csv")

print (df)

piv = pivot_unpivot(df, index=['province'], values=['beneficiaries_jan', 'beneficiaries_feb', 'beneficiaries_mar'], operation="unpivot", columns="mont")

print (piv)


