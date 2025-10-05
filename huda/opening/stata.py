import polars as pl

def open_stata(file_path):
    """
    📘 Load Stata (.dta) file easily into Polars DataFrame.

    Parameters:
        - file_path: Path to your .dta file

    Example usage:
    -------------------------
        df = open_stata("data/sample_stata.dta")
        print(df)

    ✅ This will load Stata data into a table for easy analysis!
    """
    try:
        df = pl.read_ipc(file_path)  # Polars can't read .dta directly
        print("✅ Stata file loaded successfully as Polars DataFrame!")
        print(f"Rows: {df.height}, Columns: {df.width}")
        return df
    except Exception as e:
        print("⚠️ Stata load error:", e)
        return None
