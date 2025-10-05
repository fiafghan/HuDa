import polars as pl

def duplicate(df, columns=None, keep="first"):
    """
    ♻️ Handle (remove or keep) duplicate rows in a DataFrame.

    Parameters
    ----------
    df : pl.DataFrame
        The input DataFrame.
    columns : str | list[str] | None
        Columns to check for duplicates.
        - None → check all columns.
        - str → check only one column.
        - list[str] → check based on multiple columns.
    keep : {"first", "last", False}
        - "first" → keep the first occurrence.
        - "last" → keep the last occurrence.
        - False → remove all duplicates completely.

    Example:
    ----------
        import polars as pl
        from huda.cleaning.duplicate import duplicate

        df = pl.DataFrame({
            "country": ["Afghanistan", "Afghanistan", "Syria", "Yemen", "Yemen"],
            "year": [2025, 2025, 2024, 2025, 2025],
            "sector": ["Health", "Health", "Food", "Health", "Health"]
        })

        # ✅ Remove duplicates based on all columns
        df_no_dupes = duplicate(df)

        # ✅ Remove duplicates only based on one column
        df_country = duplicate(df, columns="country", keep="last")

        # ✅ Remove duplicates based on multiple columns
        df_multi = duplicate(df, columns=["country", "year"])

    Output Example:
    ----------
        shape: (3, 3)
        ┌──────────────┬──────┬────────┐
        │ country      ┆ year ┆ sector │
        │ ---          ┆ ---  ┆ ---    │
        │ str          ┆ i64  ┆ str    │
        ╞══════════════╪══════╪════════╡
        │ Afghanistan  ┆ 2025 ┆ Health │
        │ Syria        ┆ 2024 ┆ Food   │
        │ Yemen        ┆ 2025 ┆ Health │
        └──────────────┴──────┴────────┘

    When and Why:
    -------------
    - 🔍 When combining datasets from multiple sources, duplicates often appear.
    - 🧹 Removing them ensures cleaner and more accurate analysis.
    - 💡 Always inspect your data before removing duplicates to avoid losing valid records.
    """
    try:
        # 🔹 Normalize column input (single str → list)
        if isinstance(columns, str):
            columns = [columns]

        # 🔹 Handle duplicates
        df_clean = df.unique(subset=columns, keep=keep)

        if columns is None:
            print("✅ Duplicates handled based on all columns.")
        else:
            print(f"✅ Duplicates handled based on columns: {columns}")

        return df_clean

    except Exception as e:
        print("⚠️ Error while handling duplicates:", e)
        return df
