from huda.stata import open_stata

df = open_stata("testdata/sample_stata.dta")

print(df)