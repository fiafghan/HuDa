import polars as pl

def open_parquet(file_path, columns=None):
    """
    Load a Parquet file easily into Polars DataFrame for analysis.

    Parameters:
        - file_path: path to your Parquet file
        - columns: optional list of columns to select (like a simple filter)
    
    Example usage:
    ----------------------
    # Load entire Parquet file
    df = open_parquet("humanitarian_data.parquet")
    print(df)

    # Load only specific columns
    df_filtered = open_parquet("humanitarian_data.parquet", columns=["province", "population"])
    print(df_filtered)
    """
    try:
        # Load Parquet with Polars
        df = pl.read_parquet(file_path, columns=columns)
        print("✅ Parquet file loaded successfully!")
        print(f"Rows: {df.height}, Columns: {df.width}")
        return df
    except FileNotFoundError:
        print("⚠️ File not found. Check the file name and path.")
        return None
    except Exception as e:
        print("⚠️ Something went wrong while loading the Parquet file.")
        print("Error:", e)
        return None
