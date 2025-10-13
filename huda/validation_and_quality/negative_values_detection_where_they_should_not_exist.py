import polars as pl
import pandas as pd
from typing import Union, List
import io

def negative_values_detection_where_they_should_not_exist(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    numeric_columns: List[str]
) -> pl.DataFrame:
    """
    ⚠️ Detect Negative Values in Columns Where They Should Not Exist
    =================================================================

    🧭 What this function does:
    ----------------------------
    Some columns in humanitarian or survey data should never have negative numbers
    (like age, population, food distributed, water liters, shelter units).  
    This function finds rows where these columns have invalid negative values.

    💡 Afghanistan Example:
    -----------------------
    Suppose you have this data:

    ┌────────────┬─────┬────────────┐
    │ province   ┆ age ┆ food_provided │
    ├────────────┼─────┼────────────┤
    │ Kabul      ┆ 25  ┆ 100          │
    │ Herat      ┆ -5  ┆ 50           │
    │ Kandahar   ┆ 35  ┆ -10          │
    │ Balkh      ┆ 40  ┆ 70           │
    └────────────┴─────┴────────────┘

    Using this function on `["age", "food_provided"]`, it will return only the rows
    with invalid negative numbers:

    ┌────────────┬─────┬────────────┬──────────────┐
    │ province   ┆ age ┆ food_provided │ negative_count │
    ├────────────┼─────┼────────────┤──────────────┤
    │ Herat      ┆ -5  ┆ 50           │ 1            │
    │ Kandahar   ┆ 35  ┆ -10          │ 1            │
    └────────────┴─────┴────────────┤──────────────┘

    🧮 Parameters:
    --------------
    data : str | pandas.DataFrame | polars.DataFrame | io.BytesIO  
        Input dataset (CSV file path, Pandas/Polars DataFrame, or file bytes)

    numeric_columns : List[str]  
        List of columns where negative numbers are **not allowed** (e.g., ["age", "population", "food_provided"])

    🕒 When to Use:
    ---------------
    - During data cleaning to detect impossible negative values  
    - Before analysis or reporting  

    🤔 Why Useful:
    ---------------
    - Prevents errors in calculations and dashboards  
    - Helps identify data entry mistakes or survey issues  
    - Ensures datasets are valid and trustworthy  

    🌍 Where to Apply:
    ------------------
    - Afghanistan humanitarian surveys  
    - NGO program monitoring datasets  
    - Any dataset with numeric indicators  

    📊 Example Usage:
    -----------------
    ```python
    import polars as pl

    df = pl.DataFrame({
        "province": ["Kabul", "Herat", "Kandahar", "Balkh"],
        "age": [25, -5, 35, 40],
        "food_provided": [100, 50, -10, 70]
    })

    negative_rows = negative_values_detection_where_they_should_not_exist(
        data=df,
        numeric_columns=["age", "food_provided"]
    )

    print(negative_rows)
    ```

    ✅ Expected Output:
    -------------------
    ┌────────────┬─────┬────────────┬──────────────┐
    │ province   ┆ age ┆ food_provided │ negative_count │
    ├────────────┼─────┼────────────┤──────────────┤
    │ Herat      ┆ -5  ┆ 50           │ 1            │
    │ Kandahar   ┆ 35  ┆ -10          │ 1            │
    └────────────┴─────┴────────────┤──────────────┘
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

    # --- 2. Detect negative values ---
    negative_exprs = [
        (pl.when(pl.col(c) < 0).then(1).otherwise(0)).alias(f"{c}_negative_flag")
        for c in numeric_columns
    ]
    df = df.with_columns(negative_exprs)

    df = df.with_columns(
        pl.sum_horizontal([pl.col(f"{c}_negative_flag") for c in numeric_columns]).alias("negative_count")
)


    # --- 3. Return only rows with at least one negative value ---
    return df.filter(pl.col("negative_count") > 0)
