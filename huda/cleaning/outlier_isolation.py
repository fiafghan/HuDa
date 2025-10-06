import polars as pl
from sklearn.ensemble import IsolationForest
import numpy as np

def outlier_isolation(df, columns=None, contamination=0.05, random_state=42):
    """
    🛡 Handle outliers using Isolation Forest (advanced outlier detection).

    💡 Simple Explanation:
    ----------------------
    Isolation Forest automatically detects and removes "unusual" rows 
    that look very different from the rest. 
    It’s smarter than simple IQR or Z-score because it looks at all selected columns together.

    🧠 Example Usage:
    -----------------
        import polars as pl
        from huda.outliers.handle_outliers_isolation import outlier_isolation

        df = pl.DataFrame({
            "price": [100, 150, 200, 10000, 250, 300, -50],
            "population": [1000, 2000, 1500, 30000, 1800, 2100, 50000],
            "year": [2015, 2016, 2017, 2025000, 2018, 2019, 2020]
        })

        # ✅ Case 1: Handle outliers for all numeric columns
        df_all = outlier_isolation(df)

        # ✅ Case 2: Handle outliers only for one column
        df_one = outlier_isolation(df, columns="price")

        # ✅ Case 3: Handle outliers for specific columns
        df_some = outlier_isolation(df, columns=["price", "population"])

    🧾 Output:
    -----------
    Rows detected as outliers (-1) are removed.
    The result is a cleaned DataFrame with only normal (non-outlier) rows.

    📅 When & Why:
    -----------------
    ✅ **When to use Isolation Forest:**
        - Your dataset is large (hundreds or thousands of rows).
        - You have multiple numeric columns.
        - You expect that some outliers depend on more than one column (e.g., high income but low age).

    ⚠️ **When NOT to use:**
        - Dataset is very small (< 30 rows).
        - You only have one simple numeric column → better use IQR or Z-Score.

    💡 **Why Isolation Forest:**
        - Detects multi-dimensional and subtle outliers.
        - Handles non-linear relationships automatically.
        - Works well even if data is not normally distributed.
    """

    try:
        # 🔍 Select numeric columns if not provided
        if columns is None:
            columns_to_use = [c for c, t in zip(df.columns, df.dtypes) if t in [pl.Int64, pl.Float64]]
        elif isinstance(columns, str):
            columns_to_use = [columns]
        elif isinstance(columns, list):
            columns_to_use = [c for c in columns if c in df.columns]
        else:
            raise ValueError("Invalid type for 'columns'. Must be str, list, or None.")

        if not columns_to_use:
            print("⚠️ No numeric columns found to analyze for outliers.")
            return df

        # 🎯 Extract numeric data as numpy array
        data = df.select(columns_to_use).to_numpy()

        # 🧠 Train Isolation Forest model
        iso = IsolationForest(contamination=contamination, random_state=random_state)
        preds = iso.fit_predict(data)  # 1 = normal, -1 = outlier

        # 🧩 Create boolean mask (True = keep)
        mask = preds == 1

        # 🧱 Convert mask to Polars boolean column
        mask_series = pl.Series("mask", mask)

        # 🔧 Apply mask safely to the whole dataframe
        df_clean = df.with_columns(mask_series).filter(pl.col("mask")).drop("mask")

        print(f"✅ Outliers handled successfully using Isolation Forest on: {', '.join(columns_to_use)}")
        return df_clean

    except Exception as e:
        print("⚠️ Error while handling outliers:", e)
        return df
