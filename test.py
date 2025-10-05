from huda.cleaning import fill_constant
from huda.opening import open_csv

df = open_csv("testdata/test.csv")

filled_constant = fill_constant(df, "Missing")
print(filled_constant)