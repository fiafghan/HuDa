from huda.cleaning import fill_mode
from huda.csv import open_csv

df = open_csv("testdata/test.csv")

moded_df = fill_mode(df = df, column="population")
print(moded_df)