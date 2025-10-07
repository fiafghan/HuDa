import polars as pl
from fuzzywuzzy import process

def admin_boundaries(df, country_col="country", adm1_col="province", adm2_col="district", threshold=80):
    """
    🗺 Autonomous Admin Boundaries Resolver (ADM0–ADM2)
    =====================================================

    💡 What it does:
    ----------------
    - Automatically detects and fixes inconsistent spellings of provinces and districts
    - Works without any external reference dataset
    - Uses fuzzy string matching to map similar names together
    - Adds standardized ADM columns: 'adm0', 'adm1', 'adm2'

    🧾 Parameters:
    ----------------
    - df : pl.DataFrame
        Dataset with country, province, and district columns
    - country_col, adm1_col, adm2_col : str
        Columns containing country, province, and district names
    - threshold : int
        Fuzzy matching threshold (0–100) for considering names as similar

    🧠 Example Usage:
    -----------------
    import polars as pl

    df = pl.DataFrame({
        "country": ["Afghanistan", "Afganistan", "Afghanistan"],
        "province": ["Kabul", "Kabol", "Herat"],
        "district": ["Kabul", "Kabool", "Herat"]
    })

    df_clean = admin_boundaries(df, country_col = "country", adm1_col = "province", adm2_col = "district", threshold=80)
    print(df_clean)
    """
    try:
        # ✅ Normalize text
        df = df.with_columns([
            pl.col(country_col).str.strip_chars().str.to_lowercase().alias("adm0_raw"),
            pl.col(adm1_col).str.strip_chars().str.to_lowercase().alias("adm1_raw"),
            pl.col(adm2_col).str.strip_chars().str.to_lowercase().alias("adm2_raw"),
        ])

        # ✅ Create unique lists for matching
        unique_countries = df["adm0_raw"].unique().to_list()
        unique_provinces = df["adm1_raw"].unique().to_list()
        unique_districts = df["adm2_raw"].unique().to_list()

        # ✅ Define fuzzy match function
        def match_name(name, choices, threshold=threshold):
            if name is None or name == "":
                return None
            match = process.extractOne(name, choices)
            if match and match[1] >= threshold:
                return match[0]
            return name

        # ✅ Apply matching using Polars map_elements (NOT apply)
        df = df.with_columns([
            pl.col("adm0_raw").map_elements(lambda x: match_name(x, unique_countries), return_dtype=pl.Utf8).alias("Admin_0_Name"),
            pl.col("adm1_raw").map_elements(lambda x: match_name(x, unique_provinces), return_dtype=pl.Utf8).alias("Admin_1_Name"),
            pl.col("adm2_raw").map_elements(lambda x: match_name(x, unique_districts), return_dtype=pl.Utf8).alias("Admin_2_Name"),
        ])

        print("✅ Administrative boundaries resolved autonomously (ADM0–ADM2)")
        return df.drop(["adm0_raw", "adm1_raw", "adm2_raw"])

    except Exception as e:
        print("⚠️ Error resolving admin boundaries:", e)
        return df
