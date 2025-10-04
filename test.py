from huda.cleaning import fill_median
from huda.csv import open_csv

df = open_csv("testdata/test.csv")

meaned_df = fill_median(df, column="population")
meaned_df.write_csv("testdata/test1.csv")
print(meaned_df)