import polars as pl

def forward_fill(df, column):
    """
    ⏩ Fill missing values with the previous value (useful for time series).

    Example:
    ----------
        df = pl.DataFrame({"temp": [20, None, 25, None, 30]})
        df_clean = forward_fill(df, "temp")
    """
    try:
        df_clean = df.with_columns(pl.col(column).fill_null(strategy="forward"))
        print(f"✅ Missing values in '{column}' filled using forward-fill")
        return df_clean
    except Exception as e:
        print("⚠️ Error while forward filling:", e)
        return df
