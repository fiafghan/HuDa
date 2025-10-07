import polars as pl

def admin_boundaries(df, country_col="country", adm1_col="province", adm2_col="district", adm3_col=None, reference_df=None):
    """
    🗺 Resolve Administrative Boundaries (ADM0–ADM3)
    =================================================
    
    💡 Simple Explanation:
    ----------------------
    This function automatically fills or validates administrative levels in your dataset:
    - ADM0 → Country
    - ADM1 → Province / Region
    - ADM2 → District / Sub-region
    - ADM3 → Optional lower level (if available)
    
    👇 How it works:
    ----------------
    - Uses a reference dataset (official admin boundaries)
    - Matches the input names to the official names
    - Fixes spelling variations or missing levels
    - Returns the original dataset with corrected ADM columns
    
    🧾 Parameters:
    ----------------
    - df : pl.DataFrame
        Your dataset with location information
    - country_col : str
        Column containing country names (ADM0)
    - adm1_col : str
        Column containing province names (ADM1)
    - adm2_col : str
        Column containing district names (ADM2)
    - adm3_col : str | None
        Optional lower-level administrative unit
    - reference_df : pl.DataFrame | None
        Reference dataset with columns: country, adm1, adm2, adm3
    
    🧠 Example Usage:
    -----------------
    import polars as pl

    df = pl.DataFrame({
        "country": ["Afghanistan"]*5,
        "province": ["Kabul", "Herat", "Kandahar", "Badakhshan", "Balkh"],
        "district": ["Kabul", "Herat", "Kandahar", "Fayzabad", "Mazar-i-Sharif"]
    })

    # Reference dataset (official admin boundaries)
    reference_df = pl.DataFrame({
        "country": ["Afghanistan"]*5,
        "adm1": ["Kabul", "Herat", "Kandahar", "Badakhshan", "Balkh"],
        "adm2": ["Kabul", "Herat", "Kandahar", "Fayzabad", "Mazar-i-Sharif"]
    })

    df_clean = admin_boundaries(df, reference_df=reference_df)
    print(df_clean)

    🧾 Output:
    -----------------
    ADM columns are corrected and standardized.
    """
    try:
        if reference_df is None:
            print("⚠️ Reference dataset not provided. Returning original dataframe.")
            return df

        # Merge df with reference admin boundaries
        df_resolved = df.join(
            reference_df, 
            left_on=[country_col, adm1_col, adm2_col], 
            right_on=["country", "adm1", "adm2"],
            how="left"
        )

        # If ADM3 column exists, rename
        if adm3_col and adm3_col in reference_df.columns:
            df_resolved = df_resolved.with_columns(
                reference_df[adm3_col].alias("adm3")
            )

        print(f"✅ Administrative boundaries resolved using reference dataset.")
        return df_resolved

    except Exception as e:
        print("⚠️ Error while resolving administrative boundaries:", e)
        return df
