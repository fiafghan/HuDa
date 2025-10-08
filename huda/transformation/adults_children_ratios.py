import polars as pl
from typing import Union

def adults_children_ratios(
    data: Union[str, pl.DataFrame],
    numerator_columns: list,
    denominator_columns: list,
    suffix: str = "_ratio"
) -> pl.DataFrame:
    """
    ⚖️ Calculate Ratios (e.g., children vs adults)
    ================================================

    What it does:
    -------------
    - Computes ratios between columns (e.g., children / adults)
    - Adds new ratio columns automatically
    - Works with Polars DataFrame or CSV file path

    Parameters:
    -----------
    data : str | pl.DataFrame
        Path to CSV file or a Polars DataFrame

    numerator_columns : list
        Columns to use as numerator (e.g., ["children"])

    denominator_columns : list
        Columns to use as denominator (e.g., ["adults"])

    suffix : str, default="_ratio"
        Text to append to new ratio column names

    Returns:
    --------
    pl.DataFrame
        DataFrame with added ratio columns

    Example Usage:
    --------------
    df = pl.DataFrame({
        "province": ["Kabul", "Herat", "Kandahar"],
        "children": [1200000, 250000, 300000],
        "adults": [3300000, 750000, 900000]
    })

    df_ratio = adults_children_ratios(df, numerator_columns=["children"], denominator_columns=["adults"])
    print(df_ratio)

    Output Table:
    -------------
    ┌──────────┬───────────┬─────────┬────────────┐
    │ province │ children  │ adults  │ children_ratio │
    ├──────────┼───────────┼─────────┼───────────────┤
    │ Kabul    │ 1200000   │ 3300000 │ 0.36          │
    │ Herat    │ 250000    │ 750000  │ 0.33          │
    │ Kandahar │ 300000    │ 900000  │ 0.33          │
    └──────────┴───────────┴─────────┴───────────────┘

    When to Use:
    ------------
    - You want to compare different groups (children/adults, male/female)
    - Common in humanitarian surveys for demographic analysis

    Why It’s Useful:
    ----------------
    - Helps understand proportions between groups
    - Useful for reports, dashboards, and planning
    - Can be combined with percentages for richer insights
    """
    try:
        # ✅ Step 1: Read CSV if string is passed
        if isinstance(data, str):
            df = pl.read_csv(data)
        elif isinstance(data, pl.DataFrame):
            df = data
        else:
            raise TypeError("Input must be a CSV path or a Polars DataFrame.")

        # ✅ Step 2: Validate numerator and denominator columns
        for col in numerator_columns + denominator_columns:
            if col not in df.columns:
                raise ValueError(f"Column '{col}' not found in dataset!")

        # ✅ Step 3: Calculate ratios
        for num_col, denom_col in zip(numerator_columns, denominator_columns):
            new_col = f"{num_col}_vs_{denom_col}{suffix}"
            df = df.with_columns(
                (pl.col(num_col) / pl.col(denom_col)).round(2).alias(new_col)
            )

        print("✅ Ratios calculated successfully.")
        return df

    except Exception as e:
        print("⚠️ Error calculating ratios:", e)
        return None
