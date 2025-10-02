import pandas as pd

def open_excel(file_path, sheet_name=0):
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        print ("Excel file opened successfully!")
        print (f"Rows: {len(df)}, Columns: {len(df.columns)}")
        return df
    except FileNotFoundError:
        print("Opps! File not found. check the file name and path.")
        return None
    except Exception as e:
        print("Something went wrong while opening the excel file.")
        print ("Error:", e)
        return None