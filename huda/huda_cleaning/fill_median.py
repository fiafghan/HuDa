import polars as pl

def fill_median(df, column):
    """
    📈 Fill missing values in a numeric column with its median.

    Example:
    ----------
        df = pl.DataFrame({"age": [20, None, 40]})
        df_clean = fill_median(df, "age")
    """
    try:
        median_val = df[column].median()
        df_clean = df.with_columns(pl.col(column).fill_null(median_val))
        print(f"✅ Missing values in '{column}' filled with median ({median_val})")
        return df_clean
    except Exception as e:
        print("⚠️ Error while filling with median:", e)
        return df
