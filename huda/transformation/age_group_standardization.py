import polars as pl
import pandas as pd
from typing import List, Union, Optional
import io

def age_group_standardization(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    age_column: str,
    age_bins: Optional[List[int]] = None,
    age_labels: Optional[List[str]] = None,
    group_by_cols: Optional[List[str]] = None
) -> pl.DataFrame:
    """
🚨 Standardize Age Groups in Humanitarian Data
==============================================

🧭 What this function does:
----------------------------
This function converts individual ages into **standard age groups**.
For example, children 0-4, youth 5-17, adults 18-59, and elders 60+.
It helps to organize survey data so everyone is counted in the same bins.

💡 Afghanistan Example:
-----------------------
Suppose a survey reports the ages of people receiving aid:

┌────────────┬─────┐
│ province   ┆ age │
├────────────┼─────┤
│ Kabul      ┆ 2   │
│ Herat      ┆ 16  │
│ Kandahar   ┆ 35  │
│ Balkh      ┆ 70  │
└────────────┴─────┘

If we use age_bins `[0,5,18,60,120]` and labels 
`["0-4","5-17","18-59","60+"]`, we get:

┌────────────┬─────┬───────────┐
│ province   ┆ age ┆ age_group │
├────────────┼─────┼───────────┤
│ Kabul      ┆ 2   ┆ 0-4       │
│ Herat      ┆ 16  ┆ 5-17      │
│ Kandahar   ┆ 35  ┆ 18-59     │
│ Balkh      ┆ 70  ┆ 60+       │
└────────────┴─────┴───────────┘

🧮 Parameters:
--------------
data : str | pandas.DataFrame | polars.DataFrame | io.BytesIO  
    Input dataset. Can be a CSV file path, a Pandas DataFrame, a Polars DataFrame, or uploaded file bytes.  

age_column : str  
    Name of the column that contains individual ages.  

age_bins : List[int], optional  
    Bin edges for age groups. Default: `[0,5,18,60,120]`.  

age_labels : List[str], optional  
    Labels for each age bin. Default: `["0-4","5-17","18-59","60+"]`.  

group_by_cols : Optional[List[str]]  
    Columns to group by (like province, gender). If used, it will count how many people are in each age group per group.

🕒 When to Use:
---------------
- When you want to summarize survey data by age categories.
- For humanitarian reporting or aid targeting.
- When comparing different datasets that report ages differently.

🤔 Why Useful:
---------------
- Makes different datasets comparable.
- Helps analyze needs per age group.
- Simplifies dashboards and reporting.

🌍 Where to Apply:
------------------
- Afghanistan humanitarian surveys.
- Provincial health, nutrition, or education reports.
- NGO or UN dashboards for planning aid distribution.

📊 Example Usage:
-----------------
import polars as pl

df = pl.DataFrame({
    "province": ["Kabul", "Herat", "Kandahar", "Balkh"],
    "age": [2, 16, 35, 70]
})

result = age_group_standardization(
    data=df,
    age_column="age",
    age_bins=[0,5,18,60,120],
    age_labels=["0-4","5-17","18-59","60+"]
)

print(result)

Expected Output:

┌────────────┬─────┬───────────┐
│ province   ┆ age ┆ age_group │
├────────────┼─────┼───────────┤
│ Kabul      ┆ 2   ┆ 0-4       │
│ Herat      ┆ 16  ┆ 5-17      │
│ Kandahar   ┆ 35  ┆ 18-59     │
│ Balkh      ┆ 70  ┆ 60+       │
└────────────┴─────┴───────────┘
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

    # --- 2. Default bins and labels if not provided ---
    if age_bins is None:
        age_bins = [0, 5, 18, 60, 120]
    if age_labels is None:
        age_labels = ["0-4", "5-17", "18-59", "60+"]

    # --- 3. Create a new age_group column ---
    def map_age_group(age):
        for i in range(len(age_bins)-1):
            if age_bins[i] <= age < age_bins[i+1]:
                return age_labels[i]
        return age_labels[-1]

    df = df.with_columns(
        pl.col(age_column).map_elements(map_age_group).alias("age_group")
    )

    # --- 4. Optional grouping ---
    if group_by_cols:
        df = df.groupby(group_by_cols + ["age_group"]).agg(pl.count().alias("count"))

    return df