import polars as pl
import re

def auto_text_cleaner(df, columns=None):
    """
    🧹 Clean Text Fields in Dataset (Lowercase + Punctuation Removal)
    =================================================================

    💡 Simple Explanation:
    ----------------------
    This function automatically cleans text-type (string) columns in your dataset.
    It removes punctuation, converts text to lowercase, and trims extra spaces.

    👇 What it does:
    ----------------
    - Changes all text to lowercase (for uniformity)
    - Removes punctuation marks (.,!? etc.)
    - Removes extra spaces or invisible characters
    - Works for English, Dari, and Pashto mixed datasets

    🧩 Parameters:
    ---------------
    df : pl.DataFrame
        The dataset you want to clean
    columns : str | list[str] | None
        - None → all string columns are cleaned automatically
        - str  → clean only one column
        - list → clean specific columns

    🧠 Example Usage:
    -----------------
    import polars as pl

    df = pl.DataFrame({
        "respondent_name": ["  Ahmad!", "FATIMA,", "ZAHRA ", "Dr. Habib??"],
        "district": ["Kabul ", "  Herat", "Kandahar!", "Balkh."],
        "feedback": ["Good Service!", "   BAD ", "متوسط", " عالی "]
    })

    # 🧹 Clean all text fields automatically
    df_clean = clean_text_fields(df)

    print(df_clean)

    🧾 Output:
    -----------
    ┌──────────────────┬───────────┬──────────────┐
    │ respondent_name  ┆ district  ┆ feedback     │
    │ ---              ┆ ---       ┆ ---          │
    │ str              ┆ str       ┆ str          │
    ╞══════════════════╪═══════════╪══════════════╡
    │ ahmad            ┆ kabul     ┆ good service │
    │ fatima           ┆ herat     ┆ bad          │
    │ zahra            ┆ kandahar  ┆ متوسط         │
    │ dr habib         ┆ balkh     ┆ عالی          │
    └──────────────────┴───────────┴──────────────┘

    📅 When & Why:
    -----------------
    ✅ Use when:
        - You have survey text fields with mixed punctuation
        - Texts are written in mixed languages or cases
        - You want to prepare text data for machine learning or analysis

    💡 Why:
        - Makes analysis consistent
        - Avoids duplication due to casing (e.g., “Yes” vs “yes”)
        - Removes unnecessary characters for cleaner processing
    """

    try:
        # ✅ Step 1: Auto-detect text columns
        if columns is None:
            columns_to_clean = [c for c, t in zip(df.columns, df.dtypes) if t == pl.Utf8]
        elif isinstance(columns, str):
            columns_to_clean = [columns]
        elif isinstance(columns, list):
            columns_to_clean = [c for c in columns if c in df.columns]
        else:
            raise ValueError("❌ 'columns' must be str, list, or None")

        if not columns_to_clean:
            print("⚠️ No text columns found to clean.")
            return df

        # ✅ Step 2: Define cleaning function
        def clean_text(text):
            if text is None:
                return None
            # Remove punctuation and normalize spaces
            text = re.sub(r"[^\w\s\u0600-\u06FF]", " ", str(text))  # keep Persian/Arabic letters
            text = re.sub(r"\s+", " ", text).strip().lower()
            return text

        # ✅ Step 3: Apply cleaning to selected columns
        for col in columns_to_clean:
            df = df.with_columns(
                pl.col(col).map_elements(clean_text, return_dtype=pl.Utf8)
            )

        print(f"✅ Text cleaned successfully in columns: {', '.join(columns_to_clean)}")
        return df

    except Exception as e:
        print("⚠️ Error while cleaning text fields:", e)
        return df
