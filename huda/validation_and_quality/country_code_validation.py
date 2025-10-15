import polars as pl
import pandas as pd
from typing import Union, List, Optional
import io
import pycountry

def country_code_validation(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    country_column: str,
    group_by_cols: Optional[List[str]] = None
) -> pl.DataFrame:
    
    """
    🌐 Validate Country Codes Using pycountry (ISO 3166-1 alpha-2)
    =============================================================

    🧭 What this function does:
    ----------------------------
    Checks if the country codes in your dataset are valid ISO alpha-2 codes
    using the pycountry library. Invalid or missing codes are flagged as "Invalid".

    💡 Example:
    ------------
    Input:

    ┌────────────┬─────────┐
    │ province   ┆ country │
    ├────────────┼─────────┤
    │ Kabul      ┆ AF      │
    │ Herat      ┆ XX      │
    │ Kandahar   ┆ af      │
    │ Balkh      ┆ ""      │
    └────────────┴─────────┘

    Output after running the function:

    ┌────────────┬─────────┬────────────┐
    │ province   ┆ country ┆ valid_flag │
    ├────────────┼─────────┼────────────┤
    │ Kabul      ┆ AF      ┆ Valid      │
    │ Herat      ┆ XX      ┆ Invalid    │
    │ Kandahar   ┆ af      ┆ Valid      │
    │ Balkh      ┆ ""      ┆ Invalid    │
    └────────────┴─────────┴────────────┘
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

    # --- 2. Build set of valid ISO alpha-2 codes using pycountry ---
    valid_codes = {c.alpha_2 for c in pycountry.countries}

    # --- 3. Validate country codes ---
    df = df.with_columns(
    pl.when(pl.col(country_column).str.to_uppercase().is_in(valid_codes))
    .then(pl.lit("Valid"))
    .otherwise(pl.lit("Invalid"))
    .alias("valid_flag")
)


    # --- 4. Optional grouping ---
    if group_by_cols:
        df = df.group_by(group_by_cols + ["valid_flag"]).agg(pl.count().alias("count"))

    return df
