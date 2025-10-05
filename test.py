from huda.cleaning import duplicate
from huda.opening import open_csv

df = open_csv("testdata/test.csv")


print(df)

removed_duplicates = duplicate(df, keep="last", columns=["year", "sector"])
removed_duplicates.write_csv("testdata/removed_duplicates.csv")
print(removed_duplicates)