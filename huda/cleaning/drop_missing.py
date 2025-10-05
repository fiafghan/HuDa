import polars as pl

def drop_missing(df, column=None):
    """
    🧹 Remove rows with missing (null) values.
    - If a column is specified → drop rows where that column has null.
    - If no column is specified → drop rows with any null in the entire DataFrame.

    Example:
    ----------
        import polars as pl
        from huda.missing.drop_missing import drop_missing

        df = pl.DataFrame({
            "name": ["Ali", "Sara", None],
            "age": [23, None, 25]
        })

        # Drop missing values from all columns
        df_all = drop_missing(df)

        # Drop missing only from one column
        df_name = drop_missing(df, column="name")
    """
    try:
        if column:
            df_clean = df.filter(pl.col(column).is_not_null())
            print(f"✅ Missing rows removed from column '{column}' only!")
        else:
            df_clean = df.drop_nulls()
            print("✅ Missing rows removed from all columns!")
        return df_clean
    except Exception as e:
        print("⚠️ Error while dropping missing data:", e)
        return df
