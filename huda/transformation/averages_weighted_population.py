import polars as pl
import pandas as pd
from typing import List, Dict, Union, Optional
import io

def averages_weighted_population(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    needs_columns: List[str],
    provided_columns: List[str],
    population_column: Optional[str] = None,
    output_coverage_col: str = "weighted_coverage_pct", 
    group_by_cols: Optional[List[str]] = None,
    weights: Optional[Dict[str, Union[int, float]]] = None
) -> pl.DataFrame:
    """
    🚨 Calculate Humanitarian Needs Coverage (with Population Weighting)
    ===================================================================

    🧭 What this function does:
    ----------------------------
    It measures **how much of the total needs** (like food, water, shelter)  
    have been **covered by the provided aid** — both per-need and overall.  
    It can also **weight coverage by population**, so provinces with more people
    have more impact on the national average.

    💡 Simple Afghanistan Example:
    -------------------------------
    Suppose you have a humanitarian survey like this:

    ┌────────────┬────────────┬────────────┬──────────────┬──────────────┬──────────────┐
    │ province   ┆ population ┆ food_needs ┆ food_provided┆ water_needs  ┆ water_provided│
    ├────────────┼────────────┼────────────┼──────────────┼──────────────┼──────────────┤
    │ Kabul      ┆ 5000000    ┆ 1000       ┆ 800          ┆ 5000         ┆ 4000          │
    │ Herat      ┆ 2000000    ┆ 800        ┆ 500          ┆ 4000         ┆ 2500          │
    │ Kandahar   ┆ 3000000    ┆ 1200       ┆ 900          ┆ 6000         ┆ 4500          │
    └────────────┴────────────┴────────────┴──────────────┴──────────────┴──────────────┘

    Each province reports its needs and aid provided.  
    You can use this function to get:

    - Coverage per type:  
      `food_needs_coverage_pct` → (food_provided / food_needs × 100)  
      `water_needs_coverage_pct` → (water_provided / water_needs × 100)

    - Weighted by population (so Kabul counts more in averages)
    - Overall combined coverage for all needs
    - Optional grouping (e.g., by province or month)

    📊 Expected Output:
    -------------------
    ┌────────────┬──────────────┬──────────────┬────────────────────┬────────────────────────┐
    │ province   ┆ food_needs_coverage_pct ┆ water_needs_coverage_pct ┆ total_needs_coverage_pct ┆ weighted_coverage_pct │
    ├────────────┼─────────────────────────┼─────────────────────────┼─────────────────────────┼───────────────────────┤
    │ Kabul      ┆ 80.0                   ┆ 80.0                   ┆ 80.0                   ┆ 80.0                  │
    │ Herat      ┆ 62.5                   ┆ 62.5                   ┆ 62.5                   ┆ 70.0                  │
    │ Kandahar   ┆ 75.0                   ┆ 75.0                   ┆ 75.0                   ┆ 75.0                  │
    └────────────┴─────────────────────────┴─────────────────────────┴─────────────────────────┴───────────────────────┘

    🧮 Parameters:
    --------------
    data : str | pandas.DataFrame | polars.DataFrame | io.BytesIO  
        Input dataset  
    needs_columns : List[str]  
        Columns that represent total needs (e.g., ["food_needs", "water_needs"])  
    provided_columns : List[str]  
        Columns representing aid provided (same order as `needs_columns`)  
    population_column : Optional[str]  
        Column name for population weighting (e.g., "population")  
    output_coverage_col : str  
        Name for the final overall weighted coverage column  
    group_by_cols : Optional[List[str]]  
        Optional columns to group by (like province, month)  
    weights : Optional[Dict[str, float]]  
        Optional manual weights for importance between need types  

    🕒 When to Use:
    ---------------
    - When you have multiple aid indicators (food, water, shelter)
    - When population size matters for national averages
    - During humanitarian needs analysis or coverage monitoring

    🤔 Why Useful:
    ---------------
    - Helps identify areas with low coverage  
    - Makes national summaries fairer (big provinces count more)  
    - Great for dashboards, reports, or UN-OCHA/WFP analyses  

    🌍 Where to Apply:
    ------------------
    - Afghanistan humanitarian dashboards  
    - Provincial situation reports  
    - NGO planning and coverage assessments
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

    # --- 2. Calculate per-need coverage ---
    for need_col, provided_col in zip(needs_columns, provided_columns):
        cov_col = f"{need_col}_coverage_pct"
        df = df.with_columns(
            pl.when(pl.col(need_col) > 0)
            .then(pl.col(provided_col) / pl.col(need_col) * 100)
            .otherwise(None)
            .alias(cov_col)
        )

    # --- 3. Group if requested ---
    if group_by_cols:
        agg_exprs = []

        for col in needs_columns + provided_columns:
            agg_exprs.append(pl.sum(col).alias(col))

        for need_col in needs_columns:
            cov_col = f"{need_col}_coverage_pct"
            agg_exprs.append(pl.mean(cov_col).alias(cov_col))

        if population_column:
            agg_exprs.append(pl.sum(population_column).alias(population_column))

        df = df.group_by(group_by_cols).agg(agg_exprs)

    # --- 4. Weighted by need-type importance ---
    if weights:
        total_weight = sum(weights.values())
        weighted_sum = sum(pl.col(f"{col}_coverage_pct") * w for col, w in weights.items())
        df = df.with_columns((weighted_sum / total_weight).alias(output_coverage_col))

    # --- 5. ✅ Total combined coverage across all needs ---
    df = df.with_columns([
        (pl.sum_horizontal([pl.col(c) for c in provided_columns]) /
         pl.sum_horizontal([pl.col(c) for c in needs_columns]) * 100)
        .alias("total_needs_coverage_pct")
    ])

    # --- 6. ✅ Weighted average by population (if available) ---
    if population_column and population_column in df.columns:
        df = df.with_columns(
            (pl.col("total_needs_coverage_pct") * pl.col(population_column))
            .alias("_weighted_cov")
        )
        total_pop = df.select(pl.sum(population_column)).item()
        weighted_avg = df.select(pl.sum("_weighted_cov")).item() / total_pop
        df = df.with_columns(pl.lit(weighted_avg).alias("population_weighted_avg_pct"))
        df = df.drop("_weighted_cov")

    return df


# ✅ Example Test
if __name__ == "__main__":
    df = pl.DataFrame({
        "province": ["Kabul", "Herat", "Kandahar"],
        "population": [5000000, 2000000, 3000000],
        "food_needs": [1000, 800, 1200],
        "food_provided": [800, 500, 900],
        "water_needs": [5000, 4000, 6000],
        "water_provided": [4000, 2500, 4500],
    })

    result = needs_coverage_calculation(
        data=df,
        needs_columns=["food_needs", "water_needs"],
        provided_columns=["food_provided", "water_provided"],
        population_column="population",
        group_by_cols=["province"]
    )

    print(result)
