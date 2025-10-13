import polars as pl
import pandas as pd
from typing import Union, List, Optional
import io

def mandatory_fields_check(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    mandatory_fields: List[str]
) -> pl.DataFrame:
    """
    ⚠️ Check for Missing Mandatory Fields in Humanitarian Data
    =========================================================

    🧭 What this function does:
    ----------------------------
    This function checks if required columns (mandatory fields) have missing values
    (empty cells or nulls). It helps ensure that all important data is filled 
    before analysis or reporting.

    💡 Afghanistan Example:
    -----------------------
    Suppose you have a survey dataset:

    ┌────────────┬─────┬──────────┐
    │ province   ┆ age ┆ gender   │
    ├────────────┼─────┼──────────┤
    │ Kabul      ┆ 25  ┆ Male     │
    │ Herat      ┆     ┆ Female   │
    │ Kandahar   ┆ 35  ┆          │
    │ Balkh      ┆ 40  ┆ Male     │
    └────────────┴─────┴──────────┘

    If `mandatory_fields = ["age", "gender"]`, the function identifies the missing data
    in rows 2 and 3.

    🧮 Parameters:
    --------------
    data : str | pandas.DataFrame | polars.DataFrame | io.BytesIO  
        The input dataset (CSV path, DataFrame, or file bytes)

    mandatory_fields : List[str]  
        List of column names that must not have missing values.  

    🕒 When to Use:
    ---------------
    - Before performing analysis or reporting
    - To ensure all surveys have required data
    - To avoid errors in dashboards or calculations

    🤔 Why Useful:
    ---------------
    - Prevents missing data from breaking analysis
    - Helps identify incomplete forms or surveys
    - Ensures reports are trustworthy and accurate

    🌍 Where to Apply:
    ------------------
    - Afghanistan humanitarian surveys
    - Health, education, protection, or nutrition datasets
    - Any dataset with critical columns

    📊 Example Usage:
    -----------------
    ```python
    import polars as pl

    df = pl.DataFrame({
        "province": ["Kabul", "Herat", "Kandahar", "Balkh"],
        "age": [25, None, 35, 40],
        "gender": ["Male", "Female", None, "Male"]
    })

    missing_report = mandatory_fields_check(
        data=df,
        mandatory_fields=["age", "gender"]
    )

    print(missing_report)
    ```

    ✅ Expected Output:
    -------------------
    ┌────────────┬─────┬────────┬─────────────┐
    │ province   ┆ age ┆ gender ┆ missing_count│
    ├────────────┼─────┼────────┼─────────────┤
    │ Herat      ┆     ┆ Female ┆ 1           │
    │ Kandahar   ┆ 35  ┆ None   ┆ 1           │
    └────────────┴─────┴────────┴─────────────┘
    """

    # --- 1. Convert data to Polars DataFrame ---
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

    # --- 2. Identify rows with missing mandatory fields ---
    missing_exprs = [pl.col(col).is_null() for col in mandatory_fields]
    df_missing = df.filter(pl.any_horizontal(missing_exprs))
    
    # --- 3. Count number of missing fields per row ---
    df_missing = df_missing.with_columns(
        sum(pl.col(col).is_null().cast(pl.Int8) for col in mandatory_fields).alias("missing_count")
    )

    return df_missing
