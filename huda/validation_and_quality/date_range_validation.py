import polars as pl
import pandas as pd
from typing import Union, List, Optional
import io
from datetime import datetime

def date_range_validation(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    date_columns: List[str],
    group_by_cols: Optional[List[str]] = None
) -> pl.DataFrame:
    """
    📅 Validate Date Columns for Reasonable Ranges
    =============================================

    🧭 What this function does:
    ----------------------------
    Checks that date columns are:
    - Not before 1900-01-01
    - Not in the future (after today)

    Flags invalid dates as "Invalid" and valid dates as "Valid".

    💡 Example:
    -----------------------
    Input dataset:

    ┌────────────┬────────────┐
    │ province   ┆ survey_date │
    ├────────────┼────────────┤
    │ Kabul      ┆ 2023-05-10 │
    │ Herat      ┆ 1800-01-01 │
    │ Kandahar   ┆ 2026-01-01 │
    │ Balkh      ┆ 2022-12-31 │
    └────────────┴────────────┘

    After running the function:

    ┌────────────┬────────────┬────────────┐
    │ province   ┆ survey_date ┆ valid_flag │
    ├────────────┼────────────┼────────────┤
    │ Kabul      ┆ 2023-05-10 │ Valid      │
    │ Herat      ┆ 1800-01-01 │ Invalid    │
    │ Kandahar   ┆ 2026-01-01 │ Invalid    │
    │ Balkh      ┆ 2022-12-31 │ Valid      │
    └────────────┴────────────┴────────────┘

    🧮 Parameters:
    --------------
    data : str | pd.DataFrame | pl.DataFrame | io.BytesIO  
        Input dataset (CSV path, DataFrame, or bytes)

    date_columns : List[str]  
        List of columns containing dates to validate

    group_by_cols : Optional[List[str]]  
        Optional columns to group by and count valid/invalid dates

    🕒 When to Use:
    ---------------
    - Before analysis to ensure date fields are realistic
    - During data cleaning and quality checks

    🤔 Why Useful:
    ---------------
    - Detects wrong or future dates in surveys or reports
    - Ensures dashboards, charts, and reports are accurate

    🌍 Where to Apply:
    ------------------
    - Afghanistan humanitarian surveys
    - Program monitoring datasets
    - Any dataset with date columns
    """

    # --- 1. Convert input to Polars DataFrame ---
    if isinstance(data, str):
        df = pl.read_csv(data)
    elif isinstance(data, io.BytesIO):
        df = pl.read_csv(data)
    elif isinstance(data, pd.DataFrame):
        df = pl.from_pandas(data)
    elif isinstance(data, pl.DataFrame):
        df = data
    else:
        raise TypeError("Unsupported data type")

    # --- 2. Define date limits ---
    min_date = pl.lit(datetime(1900, 1, 1))
    max_date = pl.lit(datetime.today())

    # --- 3. Create validation expressions for each date column ---
    validation_exprs = []
    for col in date_columns:
        # Ensure column is parsed as date
        df = df.with_columns(pl.col(col).cast(pl.Utf8).str.strptime(pl.Date, "%Y-%m-%d", strict=False).alias(col))
        validation_exprs.append(
            pl.when((pl.col(col) < min_date) | (pl.col(col) > max_date))
            .then(pl.lit("Invalid"))
            .otherwise(pl.lit("Valid"))
            .alias(f"{col}_valid_flag")
        )

    df = df.with_columns(validation_exprs)

    # --- 4. Optional grouping ---
    if group_by_cols:
        for col in date_columns:
            df = df.group_by(group_by_cols + [f"{col}_valid_flag"]).agg(pl.count().alias("count"))

    return df
