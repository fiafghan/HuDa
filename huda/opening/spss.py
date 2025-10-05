import polars as pl
import pyreadstat

def open_spss(file_path):

    try:
        df_pandas, meta = pyreadstat.read_sav(file_path)
        df = pl.from_pandas(df_pandas)
        print("spss file loaded successfully!")
        print(f"rows{df.height}, columns:{df.width}")
        return df

    except Exception as e:
        print("spss load error:", e)
        return None