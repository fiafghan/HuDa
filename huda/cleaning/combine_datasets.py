import polars as pl

def combine_datasets(df1, df2, on, how="inner"):
    """
    🔗 Merge (combine) two datasets easily using Polars.

    ✅ What it does:
    ----------------
    - Combines two DataFrames (tables) into one, based on a shared column (key).
    - You can choose how to merge: inner, left, right, or outer.

    🧠 Why & When to Use Merge:
    ----------------------------
    - When your data is split across multiple sources or files.
    - Example:
        📄 One file has population data by country.
        📄 Another file has GDP data by country.
        👉 You merge them into one table for analysis.

    🧩 Merge Types:
    ---------------
    - "inner" → only rows with matching keys in both tables
    - "left" → all rows from first table, matching ones from second
    - "right" → all rows from second table, matching ones from first
    - "outer" → all rows from both tables, missing values = null

    🧪 Example Usage:
    -----------------
        import polars as pl
        from huda.combine_datasets import combine_datasets

        # Example DataFrames
        df_population = pl.DataFrame({
            "country": ["Afghanistan", "Syria", "Yemen"],
            "population": [39000000, 18000000, 30000000]
        })

        df_gdp = pl.DataFrame({
            "country": ["Afghanistan", "Yemen", "Pakistan"],
            "gdp": [20.1, 25.3, 310.0]
        })

        # Merge datasets
        df_combined = combine_datasets(df_population, df_gdp, on="country", how="outer")
        print(df_combined)

    🧾 Example Output:
    -------------------
    ✅ Datasets combined successfully using 'outer' join on 'country'
    shape: (4, 3)
    ┌──────────────┬────────────┬──────┐
    │ country      ┆ population ┆ gdp  │
    │ ---          ┆ ---        ┆ ---  │
    │ str          ┆ i64        ┆ f64  │
    ╞══════════════╪════════════╪══════╡
    │ Afghanistan  ┆ 39000000   ┆ 20.1 │
    │ Syria        ┆ 18000000   ┆ null │
    │ Yemen        ┆ 30000000   ┆ 25.3 │
    │ Pakistan     ┆ null       ┆ 310.0│
    └──────────────┴────────────┴──────┘
    """
    try:
        df_combined = df1.join(df2, on=on, how=how)
        print(f"✅ Datasets merged successfully using '{how}' join on '{on}'")
        print(f"Rows: {df_combined.height}, Columns: {df_combined.width}")
        return df_combined
    except Exception as e:
        print("⚠️ Error while merging datasets:", e)
        return None
