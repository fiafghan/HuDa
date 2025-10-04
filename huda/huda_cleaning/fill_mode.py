import polars as pl

def fill_mode(df, column):
    """
    🏷️ Fill missing values in a column with its mode (most common value).

    Example:
    ----------
        df = pl.DataFrame({"city": ["Kabul", None, "Kabul", "Herat"]})
        df_clean = fill_mode(df, "city")
    """
    try:
        mode_val = df[column].mode().to_list()[0]
        df_clean = df.with_columns(pl.col(column).fill_null(mode_val))
        print(f"✅ Missing values in '{column}' filled with mode ({mode_val})")
        return df_clean
    except Exception as e:
        print("⚠️ Error while filling with mode:", e)
        return df
