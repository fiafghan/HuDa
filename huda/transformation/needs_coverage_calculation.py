import polars as pl
import pandas as pd
from typing import List, Dict, Union, Optional
import io

def needs_coverage_calculation(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    needs_columns: List[str],
    provided_columns: List[str],
    output_coverage_col: str = "coverage_pct",
    group_by_cols: Optional[List[str]] = None,
    weights: Optional[Dict[str, Union[int, float]]] = None
) -> pl.DataFrame:
    """
    🚨 Calculate Humanitarian Needs Coverage
    ======================================

    🧭 What it does:
    ----------------
    Calculates how much of the humanitarian *needs* (like food, water, shelter)
    have been met by the *provided* aid — either per type or as a weighted or total overall percentage.

    🧮 Parameters:
    --------------
    data : str | pandas.DataFrame | polars.DataFrame | io.BytesIO
        Input dataset (CSV path, pandas/polars DF, or uploaded bytes)
    needs_columns : List[str]
        Columns representing total needs (e.g., ["food_needs", "water_needs", "shelter_needs"])
    provided_columns : List[str]
        Columns representing aid provided (same order as `needs_columns`)
    output_coverage_col : str, default="coverage_pct"
        Column name for weighted overall result if `weights` are provided
    group_by_cols : Optional[List[str]]
        Columns to group by (e.g., ["province", "date"])
    weights : Optional[Dict[str, Union[int, float]]]
        Optional weighting for calculating a weighted average across needs

    🧾 Returns:
    ------------
    pl.DataFrame
        Polars DataFrame containing:
        - Individual coverage per need (e.g., `food_needs_coverage_pct`)
        - Optional weighted overall coverage if `weights` are used
        - ✅ New column `total_needs_coverage_pct` representing the combined overall coverage

    🧩 Formula for total coverage:
        total_needs_coverage_pct = (Σ all provided) / (Σ all needs) × 100

    🧪 Example:
    -----------
    df = pl.DataFrame({
        "province": ["Kabul", "Herat"],
        "food_needs": [1000, 800],
        "food_provided": [700, 600],
        "water_needs": [5000, 4000],
        "water_provided": [3500, 3200],
        "shelter_needs": [2000, 1500],
        "shelter_provided": [1200, 1000],
    })

    df_out = needs_coverage_calculation(
        data=df,
        needs_columns=["food_needs", "water_needs", "shelter_needs"],
        provided_columns=["food_provided", "water_provided", "shelter_provided"]
    )

    print(df_out)
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

    # --- 2. Calculate individual coverage for each need ---
    for need_col, provided_col in zip(needs_columns, provided_columns):
        coverage_col_name = f"{need_col}_coverage_pct"
        df = df.with_columns(
            pl.when(pl.col(need_col) > 0)
            .then((pl.col(provided_col) / pl.col(need_col) * 100))
            .otherwise(None)
            .alias(coverage_col_name)
        )

    # --- 3. Grouping (if provided) ---
    if group_by_cols:
        agg_exprs = []

        # Sum up totals for needs and provided
        for col in needs_columns + provided_columns:
            agg_exprs.append(pl.sum(col).alias(col))

        # Mean of coverage percentages
        for need_col in needs_columns:
            cov_col = f"{need_col}_coverage_pct"
            agg_exprs.append(pl.mean(cov_col).alias(cov_col))

        df = df.group_by(group_by_cols).agg(agg_exprs)

    # --- 4. Weighted overall coverage ---
    if weights:
        weighted_exprs = []
        total_weight = sum(weights.values())
        for need_col, weight in weights.items():
            cov_col = f"{need_col}_coverage_pct"
            weighted_exprs.append(pl.col(cov_col) * weight)

        df = df.with_columns(
            (sum(weighted_exprs) / total_weight).alias(output_coverage_col)
        )

    # --- 5. ✅ Total (overall) combined coverage ---
    df = df.with_columns([
        (pl.sum_horizontal([pl.col(c) for c in provided_columns]) /
         pl.sum_horizontal([pl.col(c) for c in needs_columns]) * 100)
        .alias("total_needs_coverage_pct")
    ])

    return df


# ✅ Example test
if __name__ == "__main__":
    df = pl.DataFrame({
        "location": ["Kabul", "Herat", "Kandahar"],
        "food_needs": [1000, 800, 1200],
        "food_provided": [700, 600, 800],
        "water_needs": [5000, 4000, 6000],
        "water_provided": [3500, 3200, 4200],
        "shelter_needs": [2000, 1800, 2400],
        "shelter_provided": [1500, 1200, 1800],
    })

    df_out = needs_coverage_calculation(
        data=df,
        needs_columns=["food_needs", "water_needs", "shelter_needs"],
        provided_columns=["food_provided", "water_provided", "shelter_provided"]
    )

    print(df_out)
