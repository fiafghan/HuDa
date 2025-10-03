from huda.csv import open_csv


df = open_csv("testdata/test.csv",
initial_filters={
    "country":"Afghanistan",
    "year":2025,
    "sector":"Food"
})
    
print (df)