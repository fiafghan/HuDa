from huda.parquet import open_parquet

df = open_parquet("testdata/sample_afghanistan.parquet")

print(df)