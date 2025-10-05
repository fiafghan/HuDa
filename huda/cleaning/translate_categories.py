import polars as pl

def translate_categories(df, columns=None):
    """
    🈹 Automatically translate or standardize common categorical values 
    (Yes/No, Male/Female, Active/Inactive, etc.) to a clean and consistent format.

    💡 Simple Explanation:
    -------------------
    This function automatically finds and replaces messy or multilingual category values
    (like “بلی”, “Yes”, “Y”, “نخیر”, “No”, “N”) into a consistent English standard (Yes/No).

    🧠 Example Usage:
    -------------------
        import polars as pl
        from huda.cleaning.translate_categories import translate_categories

        df = pl.DataFrame({
            "response": ["Yes", "No", "Y", "N", "بلی", "نخیر", "Active", "غیرفعال", "زن", "مرد"],
            "status": ["فعال", "غیرفعال", "Active", "Inactive", "بلی", "نخیر", None, "Y", "N", "Yes"],
            "score": [1, 0, 1, 0, 1, 0, 1, 0, 1, 1]
        })

        # Apply to one column
        df_clean1 = translate_categories(df, "response")

        # Apply to multiple columns
        df_clean2 = translate_categories(df, ["response", "status"])

        # Apply to all columns automatically
        df_clean3 = translate_categories(df)

    🧾 Output:
    -------------------
        ┌───────────┬────────────┬────────┐
        │ response  │ status     │ score  │
        │ ---       │ ---        │ ---    │
        │ str       │ str        │ i64    │
        ╞═══════════╪════════════╪════════╡
        │ Yes       │ Active     │ 1      │
        │ No        │ Inactive   │ 0      │
        │ Yes       │ Active     │ 1      │
        │ No        │ Inactive   │ 0      │
        │ Yes       │ Yes        │ 1      │
        │ No        │ No         │ 0      │
        │ Active    │ None       │ 1      │
        │ Inactive  │ Yes        │ 0      │
        │ Female    │ No         │ 1      │
        │ Male      │ Yes        │ 1      │
        └───────────┴────────────┴────────┘

    📅 When & Why:
    -------------------
    ✅ **When:**
        - You have categorical text in multiple languages or inconsistent forms.
        - You want unified, clean labels before encoding or analytics.

    💡 **Why:**
        - Prevents duplicate category confusion.
        - Helps merge multilingual datasets.
        - Simplifies analysis and visualizations.
    """

    try:
        # 🌍 Universal mapping for categorical normalization
        auto_mapping = {
            # Yes/No
            "yes": "Yes", "y": "Yes", "true": "Yes", "1": "Yes",
            "بلی": "Yes", "آره": "Yes", "ه": "Yes", "اووه": "Yes",
            "no": "No", "n": "No", "false": "No", "0": "No",
            "نخیر": "No", "نی": "No", "نه": "No",

            # Gender
            "male": "Male", "m": "Male", "آقا": "Male", "مرد": "Male",
            "female": "Female", "f": "Female", "خانم": "Female", "زن": "Female",

            # Status
            "active": "Active", "فعال": "Active", "on": "Active",
            "inactive": "Inactive", "غیرفعال": "Inactive", "off": "Inactive",

            # Availability
            "available": "Available", "در دسترس": "Available",
            "unavailable": "Unavailable", "در دسترس نیست": "Unavailable",

            # Quality
            "poor": "Poor", "medium": "Medium", "good": "Good", "excellent": "Excellent",
            "بد": "Poor", "متوسط": "Medium", "خوب": "Good", "عالی": "Excellent"
        }

        def normalize(val):
            if val is None:
                return None
            key = str(val).strip().lower()  # safely convert anything to string
            return auto_mapping.get(key, str(val))

        # 🔍 Determine target columns
        if columns is None:
            columns_to_process = df.columns  # All columns
        elif isinstance(columns, str):
            columns_to_process = [columns]   # Single column
        else:
            columns_to_process = columns     # Multiple columns

        # 🧹 Process each selected column
        for col in columns_to_process:
            if col not in df.columns:
                continue

            # Apply normalization safely (Polars infers the dtype)
            df = df.with_columns(
                pl.col(col).map_elements(normalize).alias(col)
            )

        print(f"✅ Translated columns: {', '.join(columns_to_process)}")
        return df

    except Exception as e:
        print("⚠️ Error while translating categories:", e)
        return df
