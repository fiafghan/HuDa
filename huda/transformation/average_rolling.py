import polars as pl
from typing import Union

def average_rolling(
    data: Union[str, "pd.DataFrame", pl.DataFrame],
    value_columns: list = None,
    window: int = 3,
    min_periods: int = 1
) -> pl.DataFrame:
    """
    📈 Calculate Rolling Averages (Moving Mean)
    ==========================================

    What it does:
    -------------
    - Computes the average of values over a sliding window
    - Useful for smoothing time-series data
    - Works automatically with CSV, Pandas DataFrame, or Polars DataFrame

    Parameters:
    -----------
    data : str | pd.DataFrame | pl.DataFrame
        CSV path, Pandas DataFrame, or Polars DataFrame
    value_columns : list of str, optional
        Columns to calculate rolling averages for. If None, all numeric columns are used
    window : int, default=3
        Number of rows to include in each moving average window
    min_periods : int, default=1
        Minimum number of values in the window required to calculate a mean

    Returns:
    --------
    pl.DataFrame
        Original table with additional columns named `{col}_rolling` for each value column

    Example Usage:
    --------------
    df = pl.DataFrame({
        "province": ["Kabul", "Kabul", "Kabul", "Herat", "Herat"],
        "beneficiaries": [120, 150, 170, 200, 180],
        "food_baskets": [30, 40, 50, 60, 55]
    })

    df_rolling = average_rolling(df, value_columns=["beneficiaries", "food_baskets"], window=2)
    print(df_rolling)

    Output Table:
    -------------
    ┌───────────┬──────────────┬───────────────┬───────────────────┬──────────────────┐
    │ province  ┆ beneficiaries ┆ food_baskets ┆ beneficiaries_rolling ┆ food_baskets_rolling │
    │ ---       ┆ ---          ┆ ---           ┆ ---               ┆ ---              │
    │ str       ┆ i64          ┆ i64           ┆ f64               ┆ f64              │
    ╞═══════════╪══════════════╪═══════════════╪═══════════════════╪══════════════════╡
    │ Kabul     ┆ 120          ┆ 30            ┆ 120.0             ┆ 30.0             │
    │ Kabul     ┆ 150          ┆ 40            ┆ 135.0             ┆ 35.0             │
    │ Kabul     ┆ 170          ┆ 50            ┆ 160.0             ┆ 45.0             │
    │ Herat     ┆ 200          ┆ 60            ┆ 185.0             ┆ 55.0             │
    │ Herat     ┆ 180          ┆ 55            ┆ 190.0             ┆ 57.5             │
    """

    try:
        # Step 1: Convert input to Polars DataFrame if needed
        if isinstance(data, str):
            df = pl.read_csv(data)
        elif "pandas" in str(type(data)):
            import pandas as pd
            df = pl.from_pandas(data)
        elif isinstance(data, pl.DataFrame):
            df = data
        else:
            raise TypeError("Input must be CSV path, Pandas DataFrame, or Polars DataFrame")

        # Step 2: Identify numeric columns if not provided
        if value_columns is None:
            value_columns = [c for c, dt in df.schema.items() if dt in (pl.Int64, pl.Float64)]

        # Step 3: Calculate rolling averages
        for col in value_columns:
            df = df.with_columns(
                pl.col(col).rolling_mean(window_size=window, min_periods=min_periods).alias(f"{col}_rolling")
            )

        print(f"✅ Rolling averages calculated with window={window}")
        return df

    except Exception as e:
        print("⚠️ Error calculating rolling averages:", e)
        return None
