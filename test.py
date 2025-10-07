from huda.opening import open_csv
from huda.cleaning import admin_boundaries

df = open_csv("testdata/geocode.csv")

print (df)

geocoded = admin_boundaries(df, country_col="count", adm1_col="prov", adm2_col="dist")

print (geocoded)