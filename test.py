from huda.opening import open_csv
from huda.transformation import age_group_standardization
import polars as pl

df = open_csv("testdata/age_standardization.csv")

print (df)

cov = age_group_standardization(
          data = df,
           age_column="age",
            age_bins=[0, 6, 15, 25, 60, 120],
            age_labels = ["0-5", "6-14", "15-24", "25-59", "60+"]

    )

print (cov)


