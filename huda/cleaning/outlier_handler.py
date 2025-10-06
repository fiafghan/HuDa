import polars as pl

def outlier_handler(df, columns=None, method="iqr", factor=1.5):
    """
    📊 Handle extreme or unusual values (outliers) in numeric columns.

    What it does:
    -------------------
    - Sometimes data has values that are too high or too low (outliers).
      Example: age = 20 vs 1000, income = 3000 vs 99999999.
    - These outliers can distort averages, sums, and charts.
    - This function detects them and replaces them with null.

    Columns:
    -------------------
    - If you pass a column name → only that column is checked.
    - If you pass multiple column names → only those columns are checked.
    - If you pass nothing → all numeric columns are checked.

    Method:
    -------------------
    - IQR (default): flags values far from the interquartile range.
    - Z-score: flags values far from the mean.

    Example Usage:
    -------------------
        df = pl.DataFrame({
            "age": [20, 22, 19, 100, 21, 23],
            "income": [3000, 3200, 3100, 99999, 3050, 3150]
        })

        # Check all numeric columns
        df_clean = handle_outliers(df)

        # Check only the 'age' column
        df_clean_age = handle_outliers(df, columns="age")

        # Check multiple specific columns
        df_clean_some = handle_outliers(df, columns=["age", "income"])

    Output:
    -------------------
        Extreme values are replaced with null, e.g.:
        ┌─────┬────────┐
        │ age │ income │
        │ --- │ ---    │
        │ 20  │ 3000   │
        │ 22  │ 3200   │
        │ 19  │ 3100   │
        │ null│ null   │
        │ 21  │ 3050   │
        │ 23  │ 3150   │
        └─────┴────────┘

    When & Why:
    -------------------
    ✅ When:
        - Your data has extreme numbers from errors or unusual values.
        - You want accurate calculations, charts, and analysis.
    💡 Why:
        - Prevents wrong averages, sums, or plots.
        - Makes datasets cleaner and ready for analysis or modeling.
    """
    try:
        # Identify numeric columns
        numeric_cols = [col for col, dtype in zip(df.columns, df.dtypes) if dtype in [pl.Int64, pl.Float64]]
        
        # Determine which columns to process
        if columns is None:
            cols_to_check = numeric_cols
        elif isinstance(columns, str):
            cols_to_check = [columns]
        else:
            cols_to_check = columns

        # Apply outlier handling
        for col in cols_to_check:
            if col not in df.columns:
                continue
            if method == "iqr":
                q1 = df[col].quantile(0.25)
                q3 = df[col].quantile(0.75)
                iqr = q3 - q1
                lower = q1 - factor * iqr
                upper = q3 + factor * iqr
                df = df.with_columns(
                    pl.when((pl.col(col) < lower) | (pl.col(col) > upper))
                    .then(None)
                    .otherwise(pl.col(col))
                    .alias(col)
                )
            elif method == "zscore":
                mean = df[col].mean()
                std = df[col].std()
                df = df.with_columns(
                    pl.when(((pl.col(col) - mean).abs() / std) > factor)
                    .then(None)
                    .otherwise(pl.col(col))
                    .alias(col)
                )
        print(f"✅ Outliers handled for columns: {', '.join(cols_to_check)}")
        return df

    except Exception as e:
        print("⚠️ Error while handling outliers:", e)
        return df
