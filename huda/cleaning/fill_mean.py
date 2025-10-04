import polars as pl

def fill_mean(df, column):
    """
    📊 Fill missing values in a numeric column with its mean.

    Example:
    ----------
        df = pl.DataFrame({"age": [20, None, 30]})
        df_clean = fill_mean(df, "age")
    """
    try:
        mean_val = df[column].mean()
        df_clean = df.with_columns(pl.col(column).fill_null(mean_val))
        print(f"✅ Missing values in '{column}' filled with mean ({mean_val:.2f})")
        return df_clean
    except Exception as e:
        print("⚠️ Error while filling with mean:", e)
        return df
