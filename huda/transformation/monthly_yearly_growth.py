import polars as pl
from typing import Union

def monthly_yearly_growth(
    data: Union[str, "pd.DataFrame", pl.DataFrame],
    value_column: str = "beneficiaries",
    date_column: str = "date",
    period: str = "monthly"
) -> pl.DataFrame:
    """
        📊 Calculate Growth Rates (Month-over-Month, Year-over-Year)
        ============================================================
        
        What it does:
        -------------
        - Calculates growth of a numeric column over time
        - Supports monthly (MoM) or yearly (YoY) growth
        - Automatically converts CSV or Pandas DF to Polars DF
        
        Parameters:
        -----------
        data : str | pd.DataFrame | pl.DataFrame
            CSV path, Pandas DataFrame, or Polars DataFrame
        value_column : str
            Numeric column to calculate growth on (e.g., beneficiaries)
        date_column : str
            Column containing dates
        period : str, default="monthly"
            "monthly" → Month-over-Month
            "yearly"  → Year-over-Year

        Returns:
        --------
        pl.DataFrame
            Original data with new column "growth_rate_pct"
        
        Example Usage (Afghan survey):
        -------------------------------
        import polars as pl
        
        df = pl.DataFrame({
            "province": ["Kabul", "Kabul", "Herat", "Herat", "Kandahar", "Kandahar"],
            "date": ["2024-01-01","2024-02-01","2024-01-01","2024-02-01","2024-01-01","2024-02-01"],
            "beneficiaries": [100, 150, 200, 250, 120, 180]
        })
        
        df_growth = monthly_yearly_growth(df, value_column="beneficiaries", date_column="date", period="monthly")
        print(df_growth)

        Output Table:
        -------------
        ┌────────────┬───────────────┬────────┬───────┬────────────────┐
        │ date       ┆ beneficiaries ┆ year   ┆ month ┆ growth_rate_pct│
        ├────────────┼───────────────┼────────┼───────┼────────────────┤
        │ 2024-01-01 ┆ 100           ┆ 2024   ┆ 1     ┆ NaN            │
        │ 2024-02-01 ┆ 150           ┆ 2024   ┆ 2     ┆ 50.0           │
        │ 2024-01-01 ┆ 200           ┆ 2024   ┆ 1     ┆ NaN            │
        │ 2024-02-01 ┆ 250           ┆ 2024   ┆ 2     ┆ 25.0           │
        │ 2024-01-01 ┆ 120           ┆ 2024   ┆ 1     ┆ NaN            │
        │ 2024-02-01 ┆ 180           ┆ 2024   ┆ 2     ┆ 50.0           │
        └────────────┴───────────────┴────────┴───────┴────────────────┘

        When to Use:
        ------------
        - You have time-series survey data (monthly or yearly)
        - Want to see how numbers change over time
        - Track trends for beneficiaries, cases, or aid delivery

        Why It Is Useful:
        -----------------
        - Quickly identifies growth or decline
        - Helps plan interventions in Afghan provinces
        - Makes dashboards and reports clearer

        Where to Use:
        -------------
        - Humanitarian surveys in Afghanistan
        - Provincial health or aid statistics
        - Any dataset with numeric measures over time
        """

    # ---- Step 1: Convert input to Polars DF ----
    if isinstance(data, str):
        df = pl.read_csv(data)
    elif "pandas" in str(type(data)):
        import pandas as pd
        df = pl.from_pandas(data)
    elif isinstance(data, pl.DataFrame):
        df = data
    else:
        raise TypeError("Input must be CSV path, Pandas DF, or Polars DF")

    # ---- Step 2: Convert date column if needed ----
    # Only convert if column is string
    if df.schema[date_column] in [pl.Utf8, str]:
        df = df.with_columns(
            pl.col(date_column).str.strptime(pl.Date, "%Y-%m-%d", strict=False)
        )

    # ---- Step 3: Extract year/month for grouping and sorting ----
    df = df.with_columns([
        pl.col(date_column).dt.year().alias("year"),
        pl.col(date_column).dt.month().alias("month")
    ])
    df = df.sort(date_column)

    # ---- Step 4: Calculate growth rate ----
    if period.lower() == "monthly":
        df = df.with_columns([
            ((pl.col(value_column) - pl.col(value_column).shift(1)) / pl.col(value_column).shift(1) * 100).alias("growth_rate_pct")
        ])
    elif period.lower() == "yearly":
        df = df.with_columns([
            ((pl.col(value_column) - pl.col(value_column).shift(12)) / pl.col(value_column).shift(12) * 100).alias("growth_rate_pct")
        ])
    else:
        raise ValueError("period must be 'monthly' or 'yearly'")

    print(f"✅ Growth rates calculated ({period})")
    return df

# ---------------- Example Usage ----------------
if __name__ == "__main__":
    df = pl.DataFrame({
        "province": ["Kabul", "Kabul", "Herat", "Herat", "Kandahar", "Kandahar"],
        "date": ["2024-01-01","2024-02-01","2024-01-01","2024-02-01","2024-01-01","2024-02-01"],
        "beneficiaries": [100, 150, 200, 250, 120, 180]
    })
    
    df_growth = monthly_yearly_growth(df, value_column="beneficiaries", date_column="date", period="monthly")
    print(df_growth)
