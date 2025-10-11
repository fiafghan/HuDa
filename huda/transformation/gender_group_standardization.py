import polars as pl
import pandas as pd
from typing import Union, Optional, Dict, List
import io

def gender_group_standardization(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    gender_column: str,
    mapping: Optional[Dict[str, str]] = None,
    group_by_cols: Optional[List[str]] = None
) -> pl.DataFrame:
    """
    🚻 Standardize Gender Categories in Humanitarian Data
    ====================================================

    🧭 What this function does:
    ----------------------------
    This function converts different gender labels (like "M", "Male", "F", "Female", etc.)
    into one standard form.  
    It helps to make gender data clean and consistent across surveys or reports.

    💡 Afghanistan Example:
    -----------------------
    Suppose your survey data looks like this:

    ┌────────────┬──────────┐
    │ province   ┆ gender   │
    ├────────────┼──────────┤
    │ Kabul      ┆ M        │
    │ Herat      ┆ Male     │
    │ Kandahar   ┆ F        │
    │ Balkh      ┆ female   │
    │ Nangarhar  ┆ m        │
    └────────────┴──────────┘

    People may write gender in different ways (M, male, FEMALE, etc.).  
    This function converts them all to one standard word — like “Male”, “Female”, or “Other”.

    👇 After standardization, it becomes:

    ┌────────────┬──────────┐
    │ province   ┆ gender   │
    ├────────────┼──────────┤
    │ Kabul      ┆ Male     │
    │ Herat      ┆ Male     │
    │ Kandahar   ┆ Female   │
    │ Balkh      ┆ Female   │
    │ Nangarhar  ┆ Male     │
    └────────────┴──────────┘

    🧮 Parameters:
    --------------
    data : str | pandas.DataFrame | polars.DataFrame | io.BytesIO  
        Input dataset — can be a CSV file path, a Pandas or Polars DataFrame, or file bytes.

    gender_column : str  
        Name of the column that contains gender information.

    mapping : dict, optional  
        Dictionary that tells the function how to convert each gender label.  
        Example:
        {
            "M": "Male",
            "Male": "Male",
            "m": "Male",
            "F": "Female",
            "female": "Female",
            "f": "Female",
            "unknown": "Other"
        }  
        If not given, a default mapping is used automatically.

    group_by_cols : Optional[List[str]]  
        Optional list of columns to group by (like province).  
        If provided, the function counts how many males/females per group.

    🕒 When to Use:
    ---------------
    - When you receive data from different sources and gender values look inconsistent.  
    - Before calculating statistics by gender.  
    - When creating dashboards or charts about male/female distributions.

    🤔 Why Useful:
    ---------------
    - Cleans messy gender data (e.g., “m”, “M”, “MALE”, “Male” → “Male”)  
    - Prevents errors in analysis and charts.  
    - Makes reports more professional and uniform.  

    🌍 Where to Apply:
    ------------------
    - Afghanistan humanitarian surveys  
    - NGO registration forms  
    - Health, education, or protection datasets  
    - Any dataset with a gender column  

    📊 Example Usage:
    -----------------
    import polars as pl

    df = pl.DataFrame({
        "province": ["Kabul", "Herat", "Kandahar", "Balkh", "Nangarhar"],
        "gender": ["M", "Male", "F", "female", "m"]
    })

    result = standardize_gender_categories(
        data=df,
        gender_column="gender"
    )

    print(result)

    ✅ Expected Output:

    ┌────────────┬──────────┐
    │ province   ┆ gender   │
    ├────────────┼──────────┤
    │ Kabul      ┆ Male     │
    │ Herat      ┆ Male     │
    │ Kandahar   ┆ Female   │
    │ Balkh      ┆ Female   │
    │ Nangarhar  ┆ Male     │
    └────────────┴──────────┘

    📊 Example (Grouped by Province):
    --------------------------------
    If you pass `group_by_cols=["province"]`, it will count:

    ┌────────────┬──────────┬──────────┐
    │ province   ┆ gender   ┆ count    │
    ├────────────┼──────────┼──────────┤
    │ Kabul      ┆ Male     ┆ 1        │
    │ Herat      ┆ Male     ┆ 1        │
    │ Kandahar   ┆ Female   ┆ 1        │
    │ Balkh      ┆ Female   ┆ 1        │
    │ Nangarhar  ┆ Male     ┆ 1        │
    └────────────┴──────────┴──────────┘
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

    # --- 2. Default mapping if none provided ---
    if mapping is None:
        mapping = {
            "m": "Male", "M": "Male", "male": "Male", "Male": "Male", "MALE": "Male",
            "f": "Female", "F": "Female", "female": "Female", "Female": "Female", "FEMALE": "Female",
            "other": "Other", "unknown": "Other", "": "Other", None: "Other"
        }

    # --- 3. Standardize gender values ---
    df = df.with_columns(
       pl.when(pl.col(gender_column).str.to_lowercase().is_in(list(mapping.keys())))
        .then(pl.col(gender_column).str.to_lowercase().map_elements(lambda x: mapping.get(x, "Other")))
        .otherwise(pl.lit("Other"))
        .alias(gender_column)
    )

    # --- 4. Optional grouping ---
    if group_by_cols:
        df = df.group_by(group_by_cols + [gender_column]).agg(pl.count().alias("count"))

    return df
