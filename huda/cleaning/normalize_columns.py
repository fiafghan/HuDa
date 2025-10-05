import polars as pl
import re

def normalize_columns(df):
    """
    🧾 Normalize all column names in a Polars DataFrame.
    Makes them clean, lowercase, and safe for analysis/code.

    ✅ What it does:
    ----------------
    - Converts all column names to lowercase
    - Replaces spaces (' ') and dashes ('-') with underscores ('_')
    - Removes special characters like ()!?.
    - Removes extra or trailing underscores
    - Makes column names clean and ready for analysis

    🧠 Why & When to Normalize Columns:
    -----------------------------------
    - When datasets come from different sources (CSV, Excel, JSON, API),
      column names are often inconsistent or messy.
    - Example problems:
        "Country Name", "country-name", and "COUNTRY_NAME" all mean the same thing
        but your code will treat them as **different columns**.
    - Normalizing fixes this problem and ensures:
        ✅ No errors due to case-sensitivity
        ✅ Easier filtering and merging of datasets
        ✅ More professional, clean data ready for analysis

    🧪 Example Usage:
    -----------------
        import polars as pl
        from huda.cleaning import normalize_columns

        df = pl.DataFrame({
            "Country Name ": ["Afghanistan", "Syria"],
            "Population(2025)": [12345, 67890],
            "Food-Security": ["High", "Low"]
        })

        df_clean = normalize_columns(df)
        print(df_clean)

    🧾 Example Output:
    -------------------
    ✅ Column names normalized successfully!
    🔹 Old Names: ['Country Name ', 'Population(2025)', 'Food-Security']
    🔹 New Names: ['country_name', 'population2025', 'food_security']

    shape: (2, 3)
    ┌──────────────┬────────────────┬───────────────┐
    │ country_name ┆ population2025 ┆ food_security │
    │ ---          ┆ ---            ┆ ---           │
    │ str          ┆ i64            ┆ str           │
    ╞══════════════╪════════════════╪═══════════════╡
    │ Afghanistan  ┆ 12345          ┆ High          │
    │ Syria        ┆ 67890          ┆ Low           │
    └──────────────┴────────────────┴───────────────┘
    """
    try:
        # Clean and normalize all column names
        new_columns = []
        for col in df.columns:
            clean_name = col.strip().lower()
            clean_name = re.sub(r"[^\w\s-]", "", clean_name)  # remove special chars
            clean_name = clean_name.replace(" ", "_").replace("-", "_")
            clean_name = re.sub(r"_+", "_", clean_name)  # remove multiple underscores
            clean_name = clean_name.strip("_")
            new_columns.append(clean_name)

        # Assign new names to DataFrame
        df_clean = df.rename(dict(zip(df.columns, new_columns)))

        print("✅ Column names normalized successfully!")
        print("🔹 Old Names:", df.columns)
        print("🔹 New Names:", new_columns)
        return df_clean
    except Exception as e:
        print("⚠️ Error while normalizing column names:", e)
        return df
