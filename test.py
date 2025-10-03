from huda.excel import open_excel

df = open_excel("testdata/one.xlsx", sheet_name="Sheet1")
    
print (df)