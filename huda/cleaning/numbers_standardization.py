import polars as pl
import re

def standardize_numbers(df, columns=None):
    """
    🔢 Handle and standardize inconsistent number formats across the dataset.

    💡 Simple Explanation:
    -------------------
    This function automatically converts messy, localized, or string-based numbers 
    (like "1,200", "۱٬۲۰۰", "1.200,50", "1 200 AFN", "N/A") into clean numeric values.

    It understands commas, dots, Persian digits, spaces, and currency symbols.

    🧠 Example Usage:
    -------------------
        import polars as pl
        from huda.cleaning.normalize_numbers import normalize_numbers

        df = pl.DataFrame({
            "price": ["1,200", "۱٬۵۰۰", "2.000,50", "1 000", "N/A", None],
            "population": ["2,345,000", "۳٬۴۵۶٬۷۸۹", "4.5M", "1.2 B", "500k", "۵۰۰۰"]
        })

        # Normalize all numeric columns
        df_clean = normalize_numbers(df)

        print(df_clean)

    🧾 Output:
    -------------------
        ┌────────┬────────────┐
        │ price  │ population │
        │ ---    │ ---        │
        │ f64    │ f64        │
        ╞════════╪════════════╡
        │ 1200.0 │ 2345000.0  │
        │ 1500.0 │ 3456789.0  │
        │ 2000.5 │ 4500000.0  │
        │ 1000.0 │ 1200000000 │
        │ null   │ 500000.0   │
        │ 5000.0 │ 5000.0     │
        └────────┴────────────┘

    📅 When & Why:
    -------------------
    ✅ **When:**
        - Your data comes from multiple countries/languages with different number styles.
        - You see values like "1,200", "1.200,50", "۱٬۲۰۰", "2k", "3.5M", etc.

    💡 **Why:**
        - Makes sure all numeric data can be compared, analyzed, or plotted correctly.
        - Prevents calculation and aggregation errors due to string formats.
        - Converts all valid formats into real float or integer numbers.

    """

    try:
        # 🔠 Mapping for Persian / Arabic digits to English
        digit_map = str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789")

        # 🧹 Cleaner function
        def clean_number(value):
            if value is None:
                return None
            val = str(value).strip()

            # Skip if empty or known invalid
            if val.lower() in ["nan", "n/a", "none", "null", ""]:
                return None

            # Convert Persian/Arabic digits
            val = val.translate(digit_map)

            # Remove spaces and currency symbols
            val = re.sub(r"[^\d.,\-kKmMbB]", "", val)

            # Handle multipliers
            multiplier = 1
            if re.search(r"[kK]", val):
                multiplier = 1_000
                val = re.sub(r"[kK]", "", val)
            elif re.search(r"[mM]", val):
                multiplier = 1_000_000
                val = re.sub(r"[mM]", "", val)
            elif re.search(r"[bB]", val):
                multiplier = 1_000_000_000
                val = re.sub(r"[bB]", "", val)

            # Handle European format "1.200,50"
            if re.match(r"^\d{1,3}(\.\d{3})*,\d+$", val):
                val = val.replace(".", "").replace(",", ".")

            # Handle standard format "1,200.50"
            elif re.match(r"^\d{1,3}(,\d{3})+(\.\d+)?$", val):
                val = val.replace(",", "")

            # Handle plain "1.200" or "1,200"
            elif "," in val and "." not in val:
                val = val.replace(",", "")

            try:
                return float(val) * multiplier
            except:
                return None

        # 🔍 Determine which columns to process
        if columns is None:
            columns_to_process = df.columns
        elif isinstance(columns, str):
            columns_to_process = [columns]
        else:
            columns_to_process = columns

        # 🧩 Apply cleaning
        for col in columns_to_process:
            if col not in df.columns:
                continue

            df = df.with_columns(
                pl.col(col)
                .cast(pl.Utf8)                       # <-- force string type first
                .map_elements(clean_number, return_dtype=pl.Float64)
                .alias(col)
            )


        print(f"✅ Normalized number formats in: {', '.join(columns_to_process)}")
        return df

    except Exception as e:
        print("⚠️ Error while normalizing numbers:", e)
        return df
