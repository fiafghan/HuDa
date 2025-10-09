from huda.opening import open_csv
from huda.transformation import average_rolling
import polars as pl

df = open_csv("testdata/rolling.csv")

print (df)

roll = average_rolling(df, value_columns = ['beneficiaries', 'food_baskets'], window = 3)

print (roll)


