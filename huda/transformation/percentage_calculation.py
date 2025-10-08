import polars as pl
from typing import Union

def percentage_calculation(
    data: Union[str, pl.DataFrame],
    numerator_columns: list,
    denominator_column: str,
    suffix: str = "_pct"
) -> pl.DataFrame:
    """
    📊 Calculate Percentages (e.g., % of population in need)
    =========================================================

    What it does:
    -------------
    - Calculates percentage values for columns such as "people_in_need" or "students"
    - Uses a reference column like "population" as denominator
    - Automatically adds new percentage columns (e.g., people_in_need_pct)
    - Works with Polars DataFrame or directly from a CSV file

    Parameters:
    -----------
    data : str | pl.DataFrame
        Path to CSV file or a Polars DataFrame

    numerator_columns : list
        List of columns to calculate percentages for (e.g., ["in_need", "vaccinated"])

    denominator_column : str
        Column name representing the total population or reference value

    suffix : str, default="_pct"
        Text to append to new percentage column names

    Returns:
    --------
    pl.DataFrame
        DataFrame with added percentage columns

    Example Usage:
    --------------
    df = pl.DataFrame({
        "province": ["Kabul", "Herat", "Kandahar"],
        "population": [4500000, 1000000, 1200000],
        "people_in_need": [900000, 150000, 200000],
        "students": [1200000, 250000, 300000]
    })

    df_pct = calculate_percentages(df, numerator_columns=["people_in_need", "students"], denominator_column="population")
    print(df_pct)

    Output:
    -------
    ┌──────────┬────────────┬────────────────┬───────────┬────────────────────┬──────────────────┐
    │ province │ population │ people_in_need │ students  │ people_in_need_pct │ students_pct     │
    ├──────────┼────────────┼────────────────┼───────────┼────────────────────┼──────────────────┤
    │ Kabul    │ 4500000    │ 900000         │ 1200000   │ 20.0               │ 26.67            │
    │ Herat    │ 1000000    │ 150000         │ 250000    │ 15.0               │ 25.0             │
    │ Kandahar │ 1200000    │ 200000         │ 300000    │ 16.67              │ 25.0             │
    └──────────┴────────────┴────────────────┴───────────┴────────────────────┴──────────────────┘

    When to Use:
    ------------
    - You want to find how much of a population is affected, helped, or covered.
    - Common in humanitarian surveys or OCHA datasets.

    Why It’s Useful:
    ----------------
    - Easy way to show proportion or coverage.
    - Ideal for dashboards, infographics, or reports.
    - Makes big numbers meaningful (% instead of raw totals).
    """
    try:
        # ✅ Step 1: Read CSV if string is passed
        if isinstance(data, str):
            df = pl.read_csv(data)
        elif isinstance(data, pl.DataFrame):
            df = data
        else:
            raise TypeError("Input must be a CSV path or a Polars DataFrame.")

        # ✅ Step 2: Check that denominator exists
        if denominator_column not in df.columns:
            raise ValueError(f"Column '{denominator_column}' not found!")

        # ✅ Step 3: Calculate percentages for each numerator
        for col in numerator_columns:
            if col not in df.columns:
                print(f"⚠️ Column '{col}' not found — skipping.")
                continue
            new_col = f"{col}{suffix}"
            df = df.with_columns(
                (pl.col(col) / pl.col(denominator_column) * 100).round(2).alias(new_col)
            )

        print("✅ Percentages calculated successfully.")
        return df

    except Exception as e:
        print("⚠️ Error calculating percentages:", e)
        return None
