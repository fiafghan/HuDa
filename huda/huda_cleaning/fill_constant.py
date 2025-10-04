import polars as pl

def fill_constant(df, value="Unknown"):
    """
    🧱 Fill all missing values in the DataFrame with a constant value.

    Example:
    ----------
        df = pl.DataFrame({"name": ["Ali", None], "city": [None, "Herat"]})
        df_clean = fill_constant(df, "Missing")
    """
    try:
        df_clean = df.fill_nulls(value)
        print(f"✅ All missing values filled with '{value}'")
        return df_clean
    except Exception as e:
        print("⚠️ Error while filling with constant:", e)
        return df
