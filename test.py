from huda.opening import open_csv
from huda.transformation import monthly_yearly_growth
import polars as pl

df = open_csv("testdata/growth.csv")

print (df)

gr = monthly_yearly_growth(df, value_column="beneficiaries", date_column="date", period="monthly")

print (gr)


