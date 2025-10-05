from huda.cleaning import handle_outliers
from huda.opening import open_csv

df = open_csv("testdata/test.csv")


print(df)

hd_outliers = handle_outliers(df, columns='population')
hd_outliers.write_csv("testdata/hd_outliers.csv")
print(hd_outliers)