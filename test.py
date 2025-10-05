from huda.cleaning import standardize_country
from huda.opening import open_csv

df = open_csv("testdata/test.csv")


print(df)

standardized = standardize_country(df, column="country", output="name")
standardized.write_csv("testdata/std_countries.csv")
print(standardized)