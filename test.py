from huda.cleaning import backward_fill
from huda.csv import open_csv

df = open_csv("testdata/test.csv")

backward_filled = backward_fill(df, "population")
print(backward_filled)