from huda.cleaning import standardize_dates
from huda.opening import open_csv

df = open_csv("testdata/test.csv")


print(df)

standardized = standardize_dates(df, column="date")
standardized.write_csv("testdata/standardized_dates.csv")
print(standardized)