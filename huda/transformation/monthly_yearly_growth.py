import polars as pl
import pandas as pd  # Import pandas for type hinting and internal use with plot libs
from typing import Union
import io  # To handle file uploads as a buffer

# Your original monthly_yearly_growth function definition
# ----------------------------------------------------------------------------------
def monthly_yearly_growth(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
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
    - Automatically converts CSV path, Pandas DF, Polars DF, or bytes buffer to Polars DF
    
    Parameters:
    -----------
    data : str | pd.DataFrame | pl.DataFrame | io.BytesIO
        CSV path, Pandas DataFrame, Polars DataFrame, or a bytes buffer (e.g., from a file upload).
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
    from your_library_name import monthly_yearly_growth # Assuming this function is in 'your_library_name'

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
    if isinstance(data, io.BytesIO):
        df = pl.read_csv(data)
    elif isinstance(data, str):
        df = pl.read_csv(data)
    elif "pandas" in str(type(data)):  # This will match pd.DataFrame
        df = pl.from_pandas(data)
    elif isinstance(data, pl.DataFrame):
        df = data
    else:
        raise TypeError("Input 'data' must be CSV path (str), Pandas DataFrame, Polars DataFrame, or an io.BytesIO object.")

    # ---- Step 2: Validate and convert date column ----
    if date_column not in df.columns:
        raise ValueError(f"Date column '{date_column}' not found in your data.")

    if df.schema[date_column] == pl.Utf8:
        try:
            # Try common YYYY-MM-DD
            df = df.with_columns(
                pl.col(date_column).str.strptime(pl.Date, "%Y-%m-%d", strict=True).alias(date_column)
            )
        except Exception:
            try:  # Try MM/DD/YYYY
                df = df.with_columns(
                    pl.col(date_column).str.strptime(pl.Date, "%m/%d/%Y", strict=True).alias(date_column)
                )
            except Exception:
                raise ValueError(
                    f"Could not parse date column '{date_column}'. Please ensure it's in "
                    f"YYYY-MM-DD or MM/DD/YYYY format. Column type is: {df.schema[date_column]}"
                )
    elif df.schema[date_column] != pl.Date:
        raise TypeError(
            f"Date column '{date_column}' is not in a recognized date or string format. "
            f"Found: {df.schema[date_column]}. Expected Utf8 or Date."
        )

    # Ensure value column is numeric
    if df.schema[value_column] not in [pl.Int64, pl.Float64]:
        raise TypeError(f"Value column '{value_column}' must be a numeric type. Found: {df.schema[value_column]}.")

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
        raise ValueError("Parameter 'period' must be 'monthly' or 'yearly'.")

    return df
