import polars as pl

def region_based_data_aggregation(df, region_col="province", agg_method="mean"):
    """
    📊 Aggregate Data by Region
    ===========================

    💡 What it does:
    ----------------
    - Groups the dataset by a region column (e.g., province, district)
    - Calculates summary statistics for each region
    - Works automatically for numeric columns (population, income, etc.)

    🧾 Parameters:
    ----------------
    df : pl.DataFrame
        The dataset you want to summarize.
    region_col : str
        The column name representing regions (e.g., 'province', 'district').
    agg_method : str
        Aggregation method: 'mean', 'sum', 'median', or 'count'.

    🧠 Example Usage:
    -----------------
    df = pl.DataFrame({
        "province": ["Kabul", "Kabul", "Herat", "Herat", "Balkh"],
        "population": [4500000, 4600000, 1000000, 1050000, 800000],
        "patients": [23000, 24000, 5000, 5200, 4000],
        "income": [12000, 12500, 8000, 8500, 7000]
    })

    df_agg = aggregate_data_by_region(df, region_col="province", agg_method="mean")
    print(df_agg)

    🧾 Output:
    ----------
    ┌───────────┬────────────┬──────────┬──────────┐
    │ province  ┆ population ┆ patients ┆ income   │
    │ ---       ┆ ---        ┆ ---      ┆ ---      │
    │ str       ┆ f64        ┆ f64      ┆ f64      │
    ╞═══════════╪════════════╪══════════╪══════════╡
    │ Kabul     ┆ 4550000.0  ┆ 23500.0  ┆ 12250.0  │
    │ Herat     ┆ 1025000.0  ┆ 5100.0   ┆ 8250.0   │
    │ Balkh     ┆ 800000.0   ┆ 4000.0   ┆ 7000.0   │
    └───────────┴────────────┴──────────┴──────────┘

    📅 When & Why:
    ---------------
    ✅ Use when:
        - You have multiple records per region (e.g., several surveys from the same province)
        - You want to summarize data at the **regional level**

    💡 Why:
        - Helps simplify analysis (1 record per region)
        - Makes it easier to visualize regional patterns
        - Saves memory and makes datasets lighter
    """
    try:
        # Detect numeric columns
        numeric_cols = [c for c, t in zip(df.columns, df.dtypes) if t in [pl.Int64, pl.Float64]]

        if not numeric_cols:
            print("⚠️ No numeric columns to aggregate.")
            return df

        if agg_method == "mean":
            df_agg = df.group_by(region_col).agg([pl.col(c).mean().alias(c) for c in numeric_cols])
        elif agg_method == "sum":
            df_agg = df.group_by(region_col).agg([pl.col(c).sum().alias(c) for c in numeric_cols])
        elif agg_method == "median":
            df_agg = df.group_by(region_col).agg([pl.col(c).median().alias(c) for c in numeric_cols])
        elif agg_method == "count":
            df_agg = df.group_by(region_col).agg([pl.count().alias("records_count")])
        else:
            raise ValueError("❌ Invalid aggregation method. Use 'mean', 'sum', 'median', or 'count'.")

        print(f"✅ Data aggregated successfully by {region_col} using {agg_method}.")
        return df_agg

    except Exception as e:
        print("⚠️ Error during aggregation:", e)
        return df
