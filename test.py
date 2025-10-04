from huda.cleaning import drop_missing
from huda.csv import open_csv

df = open_csv("testdata/test.csv")

cleaned_df = drop_missing(df)
cleaned_df = cleaned_df.write_csv("testdata/cleaned_data.csv")
print(cleaned_df)