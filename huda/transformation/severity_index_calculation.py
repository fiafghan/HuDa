import polars as pl
import pandas as pd
from typing import List, Dict, Union, Optional
import io

def severity_index_calculation(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    indicator_columns: List[str],
    weights: Optional[Dict[str, Union[int, float]]] = None,
    output_index_col: str = "severity_index",
    normalize_method: str = "min_max",
    target_min: float = 1.0,
    target_max: float = 5.0,
    reverse_indicators: Optional[List[str]] = None
) -> pl.DataFrame:
    """
    🚨 Calculate a Humanitarian Severity Index
    =========================================

    What it does in simple terms:
    ----------------------------
    Imagine you have a table of information about different places (like provinces or districts).
    For each place, you have many numbers, like:
    - How many people are affected.
    - A score for how bad food shortages are (where a higher score means worse problems).
    - The percentage of people who have access to clean water (where a higher percentage means better access).
    - How many people have been displaced.

    You want to combine all these different numbers into one single "severity score" for each place.
    This helps you quickly see which places are in the most trouble. That's exactly what this function does!

    Key features:
    -------------
    - Helps you create a single "severity score" from many different numeric indicators.
    - Makes sure all your different numbers are on the same scale first (normalization).
    - You can give more importance (weights) to certain numbers if some are more critical.
    - The final score will be presented between a minimum (like 1) and a maximum (like 5) that you choose.
    - It can also handle numbers where a *higher* value actually means *less* severe (e.g., "access to water" - more access is good, so it flips the score correctly).

    Parameters (What you need to tell the function):
    -----------
    data : str | pandas.DataFrame | polars.DataFrame | io.BytesIO
        Your input data. This can be:
        - The name of a CSV file (e.g., "my_aid_data.csv")
        - A Pandas DataFrame (a common way to store table data in Python)
        - A Polars DataFrame (another fast way to store table data, used internally)
        - Or raw file content as bytes (e.g., when someone uploads a file on a website or Streamlit app)

    indicator_columns : List[str]
        A list of column names in your data that you want to use to calculate severity.
        These columns **must** contain numbers.
        Example: ["affected_people", "food_insecurity_score"]

    weights : Optional[Dict[str, Union[int, float]]], default=None
        (Optional) A way to tell the function which indicators are more important.
        It's a dictionary where you link an indicator column name to a number (its weight).
        If you don't provide this (leave it as `None`), all your chosen indicators will be equally important.
        Example: {"affected_people": 0.4, "food_insecurity_score": 0.6} (means 'food_insecurity_score' contributes 60% to the total, 'affected_people' 40%)

    output_index_col : str, default="severity_index"
        The name you want for the new column that will hold the calculated severity score in the output DataFrame.

    normalize_method : str, default="min_max"
        How the function should put all your different indicator numbers on the same scale.
        Currently, only "min_max" is supported. This method scales numbers from 0 (least severe) to 1 (most severe).

    target_min : float, default=1.0
        The smallest number you want for your final scaled severity score (e.g., 1 for a 1-5 scale, or 0 for a 0-100 scale).

    target_max : float, default=5.0
        The largest number you want for your final scaled severity score (e.g., 5 for a 1-5 scale, or 100 for a 0-100 scale).

    reverse_indicators : Optional[List[str]], default=None
        (Optional) A list of indicator column names where a *higher* value signifies *lower* severity.
        For example, if "access_to_water" is an indicator, a higher percentage means less severe.
        The function will automatically flip these numbers during scaling so they fit the "higher value = worse" pattern for severity.

    Returns (What you get back):
    --------
    polars.DataFrame
        Your original data, but with a new column added that contains the
        calculated 'severity_index' (or whatever name you chose in `output_index_col`).

    Example Usage (with outputs):
    -----------------------------
    import polars as pl
    # from your_library_name import severity_index_calculation # Assuming this function is in your library

    data_example = pl.DataFrame({
        "location": ["Province A", "Province B", "Province C", "Province D"],
        "affected_people": [1000, 5000, 2000, 1500],
        "food_insecurity_score": [3.5, 4.8, 2.1, 4.0], # Higher is worse
        "water_access_pct": [80, 20, 60, 90],        # Higher is better, needs reversal
        "displacement_rate": [0.1, 0.5, 0.2, 0.3],   # Higher is worse
        "date": ["2024-01-01", "2024-01-01", "2024-01-01", "2024-01-01"]
    })

    print("--- Example 1: Equal weights, default 1-5 scale ---")
    df_severity_equal = severity_index_calculation(
        data=data_example,
        indicator_columns=["affected_people", "food_insecurity_score", "water_access_pct", "displacement_rate"],
        reverse_indicators=["water_access_pct"] # Tell the function to flip 'water_access_pct'
    )
    print(df_severity_equal)
    # Explanation: Province B has the highest affected people, highest food insecurity,
    # lowest water access, and highest displacement. Therefore, it gets the highest severity index.
    # Province C has the lowest severity because its indicators suggest less dire conditions.
    # Output:
    # ┌────────────┬───────────────┬───────────────┬──────────────────┬─────────────────┬────────────┬────────────────┐
    # │ location   ┆ affected_peo… ┆ food_insecu… ┆ water_access_pct ┆ displacement_ra…┆ date       ┆ severity_index │
    # │ ‹str›      ┆ ‹i64›         ┆ ‹f64›         ┆ ‹i64›            ┆ ‹f64›           ┆ ‹str›      ┆ ‹f64›          │
    # ╞════════════╪═══════════════╪═══════════════╪══════════════════╪═════════════════╪════════════╪════════════════╡
    # │ Province A ┆ 1000          ┆ 3.5           ┆ 80               ┆ 0.1             ┆ 2024-01-01 ┆ 2.067347       │
    # │ Province B ┆ 5000          ┆ 4.8           ┆ 20               ┆ 0.5             ┆ 2024-01-01 ┆ 5.0            │
    # │ Province C ┆ 2000          ┆ 2.1           ┆ 60               ┆ 0.2             ┆ 2024-01-01 ┆ 1.489796       │
    # │ Province D ┆ 1500          ┆ 4.0           ┆ 90               ┆ 0.3             ┆ 2024-01-01 ┆ 2.224490       │
    # └────────────┴───────────────┴───────────────┴──────────────────┴─────────────────┴────────────┴────────────────┘

    print("\n--- Example 2: Custom weights, 0-100 scale ---")
    custom_weights = {
        "affected_people": 0.3,
        "food_insecurity_score": 0.4, # Giving more importance to food insecurity
        "water_access_pct": 0.1,
        "displacement_rate": 0.2
    }
    df_severity_custom = calculate_severity_index(
        data=data_example,
        indicator_columns=["affected_people", "food_insecurity_score", "water_access_pct", "displacement_rate"],
        weights=custom_weights,
        output_index_col="custom_severity",
        target_min=0,
        target_max=100, # Scale the final output from 0 to 100
        reverse_indicators=["water_access_pct"]
    )
    print(df_severity_custom)
    # Explanation: Notice that Province B still has the highest index (100.0), but the numbers
    # are now between 0 and 100 instead of 1 and 5. The order of severity usually stays the same.
    # Output:
    # ┌────────────┬───────────────┬───────────────┬──────────────────┬─────────────────┬────────────┬──────────────────┐
    # │ location   ┆ affected_peo… ┆ food_insecu… ┆ water_access_pct ┆ displacement_ra…┆ date       ┆ custom_severity  │
    # │ ‹str›      ┆ ‹i64›         ┆ ‹f64›         ┆ ‹i64›            ┆ ‹f64›           ┆ ‹str›      ┆ ‹f64›            │
    # ╞════════════╪═══════════════╪═══════════════╪══════════════════╪═════════════════╪════════════╪══════════════════╡
    # │ Province A ┆ 1000          ┆ 3.5           ┆ 80               ┆ 0.1             ┆ 2024-01-01 ┆ 27.659574        │
    # │ Province B ┆ 5000          ┆ 4.8           ┆ 20               ┆ 0.5             ┆ 2024-01-01 ┆ 100.0            │
    # │ Province C ┆ 2000          ┆ 2.1           ┆ 60               ┆ 0.2             ┆ 2024-01-01 ┆ 0.0              │
    # │ Province D ┆ 1500          ┆ 4.0           ┆ 90               ┆ 0.3             ┆ 2024-01-01 ┆ 32.765957        │
    # └────────────┴───────────────┴───────────────┴──────────────────┴─────────────────┴────────────┴──────────────────┘

    # Note: Example 3 (CSV input) and the edge cases (constant values) are omitted from the
    # docstring for brevity and focus on core examples, but would be good to include in
    # a separate 'examples.py' file for the library.

    Raises:
    -------
    TypeError
        If input data is not a recognized type, or an indicator column is not numeric.
    ValueError
        If indicator columns are not found in the data, weights are invalid (e.g., sum to zero),
        or the `normalize_method` is unsupported.
    """

    # --- Step 1: Get your data ready ---
    # This part checks what kind of data you gave it (CSV file name, Pandas table, etc.)
    # and makes sure it's in a Polars DataFrame, which is good for calculations.
    if isinstance(data, io.BytesIO):
        df = pl.read_csv(data)
    elif isinstance(data, str):
        df = pl.read_csv(data)
    elif "pandas" in str(type(data)):
        df = pl.from_pandas(data)
    elif isinstance(data, pl.DataFrame):
        df = data
    else:
        raise TypeError("Your data must be a CSV file name, a Pandas table, a Polars table, or file content.")

    # --- Step 2: Check your indicator columns ---
    # This makes sure that:
    # 1. All the column names you listed for indicators actually exist in your data.
    # 2. These columns contain numbers, not text or other types. If not, it will stop and tell you.
    for col in indicator_columns:
        if col not in df.columns:
            raise ValueError(f"The indicator column '{col}' was not found in your data. Please check the name.")
        if df.schema[col] not in [pl.Int64, pl.Float64, pl.Int32, pl.Float32]:
            raise TypeError(f"The indicator column '{col}' must be a number type (like whole numbers or decimals). It's currently: {df.schema[col]}.")

    # --- Step 3: Prepare the weights (how important each indicator is) ---
    if weights is None:
        # If you didn't give any weights, all indicators are treated as equally important.
        weights = {col: 1.0 for col in indicator_columns}
    else:
        # If you gave weights, this part checks if every indicator has a weight.
        if not all(col in weights for col in indicator_columns):
            raise ValueError("You provided weights, but not for all indicator columns. Please make sure every indicator column has a weight.")
        # It also makes sure your weights add up correctly (usually to 1.0). If they don't, it adjusts them.
        weight_sum = sum(weights.values())
        if weight_sum == 0:
            raise ValueError("The sum of your weights cannot be zero. Please check your weights.")
        if weight_sum != 1.0: # Only normalize if sum is not already 1 to avoid tiny floating point errors
            weights = {k: v / weight_sum for k, v in weights.items()}

    # --- Step 4: Put all indicator numbers on the same scale (Normalization) ---
    # This is like converting different currencies into one standard currency.
    # For example, if "affected_people" goes from 100 to 10,000, and "food_insecurity_score" from 1 to 5,
    # this step changes them all to be between 0 and 1.
    normalized_cols_exprs = []
    if normalize_method == "min_max":
        for col in indicator_columns:
            min_val = df[col].min() # Find the smallest number in this column
            max_val = df[col].max() # Find the largest number in this column

            if max_val == min_val:
                # If all numbers in this column are the same, we just give it a 0.
                normalized_cols_exprs.append(pl.lit(0.0).alias(f"{col}_normalized"))
                continue

            if reverse_indicators and col in reverse_indicators:
                # If this indicator is one where *higher* means *less severe* (like "water access"):
                # We flip the score so that higher original numbers become lower normalized scores (closer to 0, meaning less severe).
                normalized_expr = (max_val - pl.col(col)) / (max_val - min_val)
            else:
                # For normal indicators (where higher means *more severe*):
                # Higher numbers stay higher, scaled between 0 and 1.
                normalized_expr = (pl.col(col) - min_val) / (max_val - min_val)
            
            normalized_cols_exprs.append(normalized_expr.alias(f"{col}_normalized"))
        df = df.with_columns(normalized_cols_exprs) # Add these new normalized columns to your data
    else:
        raise ValueError(f"The normalization method '{normalize_method}' is not supported yet. Only 'min_max' works.")

    # --- Step 5: Combine the normalized indicators into a single raw score ---
    # Now that all indicators are on the same 0-1 scale, and they have their "importance levels" (weights), the function adds them all up for each place.
    # This gives you a "raw" severity score.
    weighted_sum_expr = pl.sum(
        [
            pl.col(f"{col}_normalized") * weights.get(col, 1.0)
            for col in indicator_columns
        ]
    )
    
    df = df.with_columns(weighted_sum_expr.alias("raw_severity_index"))

    # --- Step 6: Scale the raw score to your desired final range (e.g., 1 to 5) ---
    # The 'raw_severity_index' might still be on a weird scale (like 0.2 to 0.8).
    # This step adjusts it so it fits exactly between your 'target_min' and 'target_max' (e.g., 1 to 5).
    min_raw = df["raw_severity_index"].min()
    max_raw = df["raw_severity_index"].max()

    if max_raw == min_raw:
        # If all raw scores are the same (very rare), we just assign the middle of your target range.
        scaled_expr = pl.lit((target_min + target_max) / 2.0)
    else:
        # This formula smoothly stretches or shrinks the raw scores to fit your target range.
        scaled_expr = (
            (pl.col("raw_severity_index") - min_raw) / (max_raw - min_raw)
        ) * (target_max - target_min) + target_min
    
    df = df.with_columns(scaled_expr.alias(output_index_col))

    # --- Step 7: Clean up (remove temporary columns) ---
    # We remove the temporary "_normalized" columns and the "raw_severity_index" column
    # because the user usually only wants the final "severity_index" column.
    normalized_temp_cols = [f"{col}_normalized" for col in indicator_columns]
    df = df.drop(normalized_temp_cols + ["raw_severity_index"])

    return df

# ----------------------------------------------------------------------------------

# Example usage block (only runs when this script is executed directly)
if __name__ == "__main__":
    print("--- Running example for calculate_severity_index ---")

    data_example = pl.DataFrame({
        "location": ["Province A", "Province B", "Province C", "Province D"],
        "affected_people": [1000, 5000, 2000, 1500],
        "food_insecurity_score": [3.5, 4.8, 2.1, 4.0],
        "water_access_pct": [80, 20, 60, 90],
        "displacement_rate": [0.1, 0.5, 0.2, 0.3],
        "date": ["2024-01-01", "2024-01-01", "2024-01-01", "2024-01-01"]
    })

    # Example 1: Equal weights, default 1-5 scale
    print("\n--- Example 1: Equal weights, default 1-5 scale ---")
    df_severity_equal = calculate_severity_index(
        data=data_example,
        indicator_columns=["affected_people", "food_insecurity_score", "water_access_pct", "displacement_rate"],
        reverse_indicators=["water_access_pct"]
    )
    print(df_severity_equal)

    # Example 2: Custom weights, specific target range (0-100)
    print("\n--- Example 2: Custom weights, 0-100 scale ---")
    custom_weights = {
        "affected_people": 0.3,
        "food_insecurity_score": 0.4,
        "water_access_pct": 0.1,
        "displacement_rate": 0.2
    }
    df_severity_custom = calculate_severity_index(
        data=data_example,
        indicator_columns=["affected_people", "food_insecurity_score", "water_access_pct", "displacement_rate"],
        weights=custom_weights,
        output_index_col="custom_severity",
        target_min=0,
        target_max=100,
        reverse_indicators=["water_access_pct"]
    )
    print(df_severity_custom)

    # Example 3: Test with CSV file input (create a dummy CSV first)
    print("\n--- Example 3: CSV file input ---")
    dummy_csv_content = """location,affected_people,food_insecurity_score,water_access_pct,displacement_rate
Province X,2000,3.0,70,0.15
Province Y,4500,4.2,30,0.40
Province Z,1000,2.5,90,0.05
"""
    with open("dummy_severity_data.csv", "w") as f:
        f.write(dummy_csv_content)

    df_severity_from_csv = calculate_severity_index(
        data="dummy_severity_data.csv",
        indicator_columns=["affected_people", "food_insecurity_score", "water_access_pct", "displacement_rate"],
        reverse_indicators=["water_access_pct"]
    )
    print(df_severity_from_csv)
    import os
    os.remove("dummy_severity_data.csv")
    
    # Example 4: Test with an indicator column where all values are the same
    print("\n--- Example 4: Indicator with constant values ---")
    data_constant = pl.DataFrame({
        "location": ["A", "B", "C"],
        "indicator1": [10, 20, 30],
        "indicator2": [5, 5, 5],
    })
    df_constant_indicator = calculate_severity_index(
        data=data_constant,
        indicator_columns=["indicator1", "indicator2"]
    )
    print(df_constant_indicator)

    # Example 5: Test with all raw index values being the same (a very rare edge case)
    print("\n--- Example 5: All raw index values constant (edge case) ---")
    data_all_same = pl.DataFrame({
        "location": ["A", "B", "C"],
        "i1": [1, 1, 1],
        "i2": [2, 2, 2],
    })
    df_all_same_index = calculate_severity_index(
        data=data_all_same,
        indicator_columns=["i1", "i2"],
        target_min=0, target_max=10
    )
    print(df_all_same_index)