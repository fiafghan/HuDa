from huda.opening import open_csv
from huda.cleaning import auto_text_cleaner

df = open_csv("testdata/auto_txt_cleaner.csv")

print (df)

auto_text_clean = auto_text_cleaner(df, columns=["respondent_name", 'feedback'])

print (auto_text_clean)