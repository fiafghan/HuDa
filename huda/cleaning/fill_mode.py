import polars as pl

def fill_mode(df, column):
    """
    🏷️ Fill missing values in a column with its mode (most common value).

    Example:
    ----------
        import polars as pl
        from huda.missing.fill_mode import fill_mode

        # Create a sample DataFrame
        df = pl.DataFrame({
            "city": ["Kabul", None, "Kabul", "Herat", None],
            "year": [2020, 2021, 2020, 2022, 2021]
        })

        # Apply mode filling
        df_clean = fill_mode(df, "city")

        # Output:
        # ✅ Missing values in 'city' filled with mode (Kabul)
        # shape: (5, 2)
        # ┌────────┬──────┐
        # │ city   ┆ year │
        # │ ---    ┆ ---  │
        # │ str    ┆ i64  │
        # ╞════════╪══════╡
        # │ Kabul  ┆ 2020 │
        # │ Kabul  ┆ 2021 │
        # │ Kabul  ┆ 2020 │
        # │ Herat  ┆ 2022 │
        # │ Kabul  ┆ 2021 │
        # └────────┴──────┘
    """
    try:
        # Calculate the most frequent (mode) value
        mode_val = df[column].drop_nulls().mode().to_list()[0]
        # Fill missing values with that mode
        df_clean = df.with_columns(pl.col(column).fill_null(mode_val))
        print(f"✅ Missing values in '{column}' filled with mode ({mode_val})")
        return df_clean
    except Exception as e:
        print("⚠️ Error while filling with mode:", e)
        return df
