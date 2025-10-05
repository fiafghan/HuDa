import polars as pl

def duplicate(df, subset=None, keep="first"):
    """
    ♻️ Handle (remove or keep) duplicate rows in a DataFrame.

    - If no `subset` is given → checks all columns for duplicates.
    - `keep="first"` → keeps the first occurrence.
    - `keep="last"` → keeps the last occurrence.
    - `keep=False` → removes all duplicates completely.

    Example:
    ----------
        import polars as pl
        from huda.cleaning import duplicate

        df = pl.DataFrame({
            "country": ["Afghanistan", "Afghanistan", "Syria", "Yemen", "Yemen"],
            "year": [2025, 2025, 2024, 2025, 2025],
            "sector": ["Health", "Health", "Food", "Health", "Health"]
        })

        # ✅ Remove duplicates based on all columns
        df_no_dupes = duplicate(df)

        # ✅ Remove duplicates only based on 'country' column, keep last occurrence
        df_country = duplicate(df, subset=["country"], keep="last")

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
        df_clean = df.unique(subset=subset, keep=keep)
        print("✅ Duplicate rows handled successfully!")
        return df_clean
    except Exception as e:
        print("⚠️ Error while handling duplicates:", e)
        return df
