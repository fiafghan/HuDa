import polars as pl

def drop_missing(df):
    """
    🧹 Remove rows with any missing (null) values.

    Example:
    ----------
        import polars as pl
        from drop_missing import drop_missing

        df = pl.DataFrame({
            "name": ["Ali", "Sara", None],
            "age": [23, None, 25]
        })

        df_clean = drop_missing(df)
        print(df_clean)
    """
    try:
        df_clean = df.drop_nulls()
        print("✅ Missing rows removed successfully!")
        return df_clean
    except Exception as e:
        print("⚠️ Error while dropping missing data:", e)
        return df
