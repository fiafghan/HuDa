import polars as pl

def backward_fill(df, column):
    """
    ⏪ Fill missing values with the next value (useful for time series).

    Example:
    ----------
        df = pl.DataFrame({"temp": [None, 22, None, 28]})
        df_clean = backward_fill(df, "temp")
    """
    try:
        df_clean = df.with_columns(pl.col(column).fill_null(strategy="backward"))
        print(f"✅ Missing values in '{column}' filled using backward-fill")
        return df_clean
    except Exception as e:
        print("⚠️ Error while backward filling:", e)
        return df
