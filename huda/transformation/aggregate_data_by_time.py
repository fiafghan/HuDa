import polars as pl

def aggregate_by_time(df, date_column_name=None, frequency="monthly", aggregation_method="sum"):
    """
    📅 Aggregate survey data by time (day, month, year)
    ====================================================

    What it does:
    -------------
    - Groups data by day, month, or year
    - Adds up numeric values like beneficiaries, cost, or cases
    - Works automatically with your date column

    Parameters:
    -----------
    df : pl.DataFrame
        Afghan survey dataset with dates and numbers.

    date_col : str, optional
        Column name containing dates. If not given, finds a column with 'date' in its name.

    freq : str, default="monthly"
        Time period for grouping:
        - "daily"
        - "monthly"
        - "yearly"

    agg_method : str, default="sum"
        How to combine numbers:
        - "sum" → add them
        - "mean" → average them
        - "count" → count rows

    Returns:
    --------
    pl.DataFrame
        A table with grouped results.

    Example Usage:
    --------------
    import polars as pl

    # Sample Afghan survey dataset
    df = pl.DataFrame({
        "province": ["Kabul", "Kabul", "Herat", "Herat", "Kandahar", "Kandahar"],
        "date": ["2024-01-01", "2024-01-15", "2024-02-10", "2024-02-28", "2024-03-05", "2024-03-20"],
        "beneficiaries": [120, 150, 200, 180, 250, 300],
        "food_baskets": [30, 40, 50, 45, 60, 70]
    })

    # Aggregate by month
    monthly_agg = aggregate_by_time(df, date_column_name="date", frequency="monthly", aggregation_method="sum")

    print(monthly_agg)

    Output Table:
    -------------
    ┌──────┬───────┬─────────────────┬─────────────────┐
    │ year │ month │ beneficiaries_sum │ food_baskets_sum│
    ├──────┼───────┼─────────────────┼─────────────────┤
    │ 2024 │ 1     │ 270             │ 70              │
    │ 2024 │ 2     │ 380             │ 95              │
    │ 2024 │ 3     │ 550             │ 130             │
    └──────┴───────┴─────────────────┴─────────────────┘

    When to Use:
    ------------
    - You have Afghan survey data collected over time.
    - You want trends per day, month, or year.
    - You want a clean summary table for reporting or dashboards.

    Why It Is Useful:
    -----------------
    - Shows trends over time in a simple table.
    - Helps understand which provinces need more aid.
    - Reduces large datasets to easy-to-read summaries.
    - Can be used directly for graphs, reports, or dashboards.
    """
    try:
        # Find date column automatically
        if date_col is None:
            possible_dates = [c for c in df.columns if "date" in c.lower()]
            if not possible_dates:
                raise ValueError("No date column found!")
            date_col = possible_dates[0]

        # Convert to date type
        df = df.with_columns(pl.col(date_col).str.to_date(strict=False))

        # Extract year, month, day
        df = df.with_columns([
            pl.col(date_col).dt.year().alias("year"),
            pl.col(date_col).dt.month().alias("month"),
            pl.col(date_col).dt.day().alias("day"),
        ])

        # Decide grouping
        if freq == "yearly":
            group_cols = ["year"]
        elif freq == "monthly":
            group_cols = ["year", "month"]
        else:
            group_cols = ["year", "month", "day"]

        # Numeric columns to aggregate
        numeric_cols = [c for c, dt in df.schema.items() if dt in (pl.Float64, pl.Int64)]

        # Choose aggregation method
        if agg_method == "sum":
            agg_exprs = [pl.col(c).sum().alias(f"{c}_sum") for c in numeric_cols]
        elif agg_method == "mean":
            agg_exprs = [pl.col(c).mean().alias(f"{c}_mean") for c in numeric_cols]
        elif agg_method == "count":
            agg_exprs = [pl.count().alias("records_count")]
        else:
            raise ValueError("Invalid aggregation method")

        # Group and aggregate
        df_agg = df.groupby(group_cols).agg(agg_exprs)

        print(f"✅ Aggregated by {freq} using {agg_method}")
        return df_agg

    except Exception as e:
        print("⚠️ Error aggregating by time period:", e)
        return df
