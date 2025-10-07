from huda.opening import open_csv
from huda.cleaning import geocode

df = open_csv("testdata/geocode.csv")

print (df)

geocoded = geocode(df)

print (geocoded)