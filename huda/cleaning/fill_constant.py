import polars as pl

def fill_constant(df, value=None, column=None):
    """
    🧱 Fill missing values with a constant value.
    - If a column is specified → fill only that column.
    - If no column is specified → fill all columns.

    Example:
    ----------
        import polars as pl
        from huda.missing.fill_constant import fill_constant

        df = pl.DataFrame({
            "name": ["Ali", None],
            "city": [None, "Herat"]
        })

        # Fill all missing values with "Unknown"
        df_all = fill_constant(df, value="Unknown")

        # Fill only one column
        df_name = fill_constant(df, value="N/A", column="name")
    """
    try:
        if column:
            # 🔹 Fill specific column
            df_clean = df.with_columns(pl.col(column).fill_null(value))
            print(f"✅ Missing values in '{column}' filled with '{value}'")
        else:
            # 🔹 Fill ALL columns
            df_clean = df.with_columns([
                pl.col(c).fill_null(value).alias(c) for c in df.columns
            ])
            print(f"✅ All missing values filled with '{value}'")
        return df_clean
    except Exception as e:
        print("⚠️ Error while filling with constant:", e)
        return df
