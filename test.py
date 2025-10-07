from huda.opening import open_csv
from huda.transformation import population_based_normalization
import polars as pl

df = open_csv("testdata/popu_norm.csv")

print (df)

agg = population_based_normalization(df, value_columns=['patients', 'students'], population_column='population', per=1000)

print (agg)


