from huda.opening import open_csv
from huda.validation_and_quality import date_range_validation
import polars as pl

df = open_csv("testdata/date_range.csv")

print (df)

cov = date_range_validation(
            df,
            date_columns=['survey_date', 'report_date']
    )

print (cov)


