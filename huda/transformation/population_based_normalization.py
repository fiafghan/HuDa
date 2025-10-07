import polars as pl
from typing import Union

def population_based_normalization(
    data: Union[str, "pd.DataFrame", pl.DataFrame],
    value_columns: list,
    population_column: str,
    per: int = 1000
) -> pl.DataFrame:
    """
    📊 Normalize survey indicators per population size
    =================================================

    What it does:
    -------------
    - Converts absolute counts (cases, students, patients, etc.) 
      into per capita metrics (e.g., per 1,000 people)
    - Useful for comparing regions with different population sizes

    Parameters:
    -----------
    data : str | pd.DataFrame | pl.DataFrame
        CSV path, Pandas DataFrame, or Polars DataFrame
    value_columns : list
        List of column names to normalize (e.g., ["patients", "students"])
    population_column : str
        Column name containing the population for each region
    per : int, default=1000
        Number of people to normalize per (1000, 10000, 1, etc.)

    Returns:
    --------
    pl.DataFrame
        Original dataset with new normalized columns added, named as "{col}_per_{per}"

    Example Usage:
    --------------
    df = pl.DataFrame({
        "province": ["Kabul", "Herat", "Kandahar"],
        "population": [4500000, 1000000, 1200000],
        "patients": [23000, 5000, 8000],
        "students": [1200000, 250000, 300000]
    })

    df_norm = population_based_normalization(
        df,
        value_columns=["patients", "students"],
        population_column="population",
        per=1000
    )

    print(df_norm)

    Output Table:
    -------------
    ┌───────────┬────────────┬─────────┬─────────┬────────────────────┬─────────────────────┐
    │ province  ┆ population ┆ patients┆ students┆ patients_per_1000  ┆ students_per_1000   │
    ├───────────┼────────────┼─────────┼─────────┼────────────────────┼─────────────────────┤
    │ Kabul     ┆ 4500000    ┆ 23000   ┆ 1200000┆ 5.111              ┆ 266.667            │
    │ Herat     ┆ 1000000    ┆ 5000    ┆ 250000 ┆ 5.0                ┆ 250.0              │
    │ Kandahar  ┆ 1200000    ┆ 8000    ┆ 300000 ┆ 6.667              ┆ 250.0              │
    └───────────┴────────────┴─────────┴─────────┴────────────────────┴─────────────────────┘
    """
    try:
        # Step 1: Convert to Polars if needed
        if isinstance(data, str):
            df = pl.read_csv(data)
        elif "pandas" in str(type(data)):
            import pandas as pd
            df = pl.from_pandas(data)
        elif isinstance(data, pl.DataFrame):
            df = data
        else:
            raise TypeError("Input must be CSV path, Pandas DataFrame, or Polars DataFrame")

        # Step 2: Add normalized columns
        for col in value_columns:
            norm_col_name = f"{col}_per_{per}"
            df = df.with_columns(
                (pl.col(col) / pl.col(population_column) * per).alias(norm_col_name)
            )

        print(f"✅ Normalized columns per {per} population: {', '.join(value_columns)}")
        return df

    except Exception as e:
        print("⚠️ Error normalizing per population:", e)
        return df
