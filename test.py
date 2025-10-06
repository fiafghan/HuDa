from huda.cleaning import outlier_isolation
from huda.opening import open_csv

df = open_csv("testdata/test.csv")


print(df)

hd_outliers = outlier_isolation(df, columns=['age', 'year'])
hd_outliers.write_csv("testdata/outlier_isolation.csv")
print(hd_outliers)