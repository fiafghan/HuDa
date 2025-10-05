from huda.cleaning import normalize_columns
from huda.opening import open_csv

df = open_csv("testdata/test.csv")

normalized_columns = normalize_columns(df)
print(normalized_columns)