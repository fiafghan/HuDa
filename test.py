from huda.cleaning import translate_categories
from huda.opening import open_csv

df = open_csv("testdata/test.csv")


print(df)

transed = translate_categories(df, columns=['recieved', 'sector'])
transed.write_csv("testdata/trans_categ.csv")
print(transed)