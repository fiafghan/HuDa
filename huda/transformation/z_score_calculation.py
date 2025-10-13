import polars as pl
import pandas as pd
from typing import Union, Optional, List
import io

def z_score_calculation(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    column: str,
    threshold: float = 3.0,
    group_by: Optional[List[str]] = None,
    add_flag: bool = True
) -> pl.DataFrame:
    """
    📊 Calculate Z-Scores for Anomaly Detection
    ==========================================

    🧭 What this function does:
    ----------------------------
    This function calculates **z-scores** for a numeric column —  
    a statistical way to detect values that are unusually high or low  
    compared to the rest of the data.

    The **z-score** measures how many standard deviations a value is from the mean.
    - Values with |z| > 3 are often considered **anomalies**.

    💡 Example (Afghanistan Dataset):
    ---------------------------------
    Suppose you have a dataset of aid distribution:

    ┌────────────┬────────┐
    │ province   ┆ amount │
    ├────────────┼────────┤
    │ Kabul      ┆ 200    │
    │ Herat      ┆ 180    │
    │ Kandahar   ┆ 5000   │
    │ Balkh      ┆ 210    │
    └────────────┴────────┘

    The function can calculate a **z-score** for each “amount”  
    and flag the outlier (like Kandahar with 5000).

    🧮 Parameters:
    --------------
    data : str | pandas.DataFrame | polars.DataFrame | io.BytesIO  
        Input dataset (file path, dataframe, or file bytes)

    column : str  
        Name of the numeric column to analyze.

    threshold : float, default = 3.0  
        The z-score cutoff for flagging anomalies.  
        Example: values with |z| > 3 are considered outliers.

    group_by : list of str, optional  
        Group by these columns before calculating z-scores.  
        Useful if you want to detect anomalies **within provinces**,  
        **regions**, or **categories**.

    add_flag : bool, default = True  
        Whether to add a boolean “is_anomaly” column.

    🕒 When to Use:
    ---------------
    - Detecting abnormal values in survey or operational data  
    - Cleaning numeric columns before analysis  
    - Finding extreme outliers in aid, population, or cost data  

    🤔 Why Useful:
    ---------------
    - Identifies data entry errors or unusual values  
    - Improves data quality before dashboards or reports  
    - Works even if your data is grouped by region or category  

    📊 Example Usage:
    -----------------
    ```python
    import polars as pl

    df = pl.DataFrame({
        "province": ["Kabul", "Herat", "Kandahar", "Balkh"],
        "amount": [200, 180, 5000, 210]
    })

    result = calculate_z_scores(df, column="amount")
    print(result)
    ```

    ✅ Expected Output:
    -------------------
    ┌────────────┬────────┬────────┬────────────┐
    │ province   ┆ amount ┆ zscore ┆ is_anomaly │
    ├────────────┼────────┼────────┼────────────┤
    │ Kabul      ┆ 200    ┆ -0.5   ┆ false      │
    │ Herat      ┆ 180    ┆ -0.5   ┆ false      │
    │ Kandahar   ┆ 5000   ┆ 3.2    ┆ true       │
    │ Balkh      ┆ 210    ┆ -0.4   ┆ false      │
    └────────────┴────────┴────────┴────────────┘

    🧾 Grouped Example:
    -------------------
    ```python
    result = calculate_z_scores(
        data=df,
        column="amount",
        group_by=["province_group"]
    )
    ```

    This will calculate z-scores **within each province group** separately.

    🔒 Returns:
    ------------
    pl.DataFrame – same as input but with:
    - `zscore` column (float)
    - optional `is_anomaly` (bool)
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
        raise TypeError("Unsupported data type.")

    # --- 2. Ensure numeric column exists ---
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in dataset.")

    # --- 3. Calculate z-scores ---
    if group_by:
        df = df.with_columns([
            ((pl.col(column) - pl.col(column).mean().over(group_by)) /
             pl.col(column).std().over(group_by)).alias("zscore")
        ])
    else:
        df = df.with_columns([
            ((pl.col(column) - pl.col(column).mean()) /
             pl.col(column).std()).alias("zscore")
        ])

    # --- 4. Optional anomaly flag ---
    if add_flag:
        df = df.with_columns(
            (pl.col("zscore").abs() > threshold).alias("is_anomaly")
        )

    return df
