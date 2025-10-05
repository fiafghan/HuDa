from huda.cleaning import standardize_numbers
from huda.opening import open_csv

df = open_csv("testdata/test.csv")


print(df)

std_numbers = standardize_numbers(df)
std_numbers.write_csv("testdata/std_numbers.csv")
print(std_numbers)