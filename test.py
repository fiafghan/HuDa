from huda.sql import open_sql

df = open_sql("testdata/humanitarian_data.db")

print (df)