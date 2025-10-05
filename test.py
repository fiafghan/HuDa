from huda.cleaning import combine_datasets
from huda.opening import open_csv

df1 = open_csv("testdata/test.csv")
df2 = open_csv("testdata/test1.csv")

combined_datasets = combine_datasets(df1, df2, on="country", how="left")
combined_datasets.write_csv("testdata/combined_dataset_left.csv")
print(combined_datasets)