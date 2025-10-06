import polars as pl
from sklearn.ensemble import IsolationForest
import numpy as np

def outlier_isolation(df, columns=None, contamination=None, random_state=42):
    """
    🛡 Handle outliers using Isolation Forest (with auto contamination detection).

    💡 Simple Explanation:
    ----------------------
    This function automatically detects and removes outliers using the Isolation Forest algorithm.
    If you don't specify the contamination value, it will automatically estimate it 
    based on your dataset using the IQR (Interquartile Range) method.

    🧠 How it works:
    ----------------
    1. If you pass one column → it isolates outliers in that column only.
    2. If you pass multiple columns → it looks at them together and finds multi-dimensional outliers.
    3. If you pass no columns → it uses all numeric columns automatically.
    4. It automatically estimates the contamination level (proportion of outliers).

    📊 Auto Contamination Estimation:
    ---------------------------------
    - Uses the IQR method to estimate what % of data points are outliers.
    - Then it limits that percentage between 1% and 15% (safe professional range).

    🧩 Example Usage:
    -----------------
        df = pl.DataFrame({
            "price": [100, 150, 200, 10000, 250, 300, -50],
            "population": [1000, 2000, 1500, 30000, 1800, 2100, 50000],
            "year": [2015, 2016, 2017, 2025000, 2018, 2019, 2020]
        })

        # ✅ Case 1: Handle all numeric columns (auto contamination)
        df_clean = outlier_isolation(df)

        # ✅ Case 2: Handle specific columns
        df_some = outlier_isolation(df, columns=["price", "population"])

        # ✅ Case 3: Handle one column only
        df_one = outlier_isolation(df, columns="year")

    📅 When & Why:
    -----------------
    ✅ Use when:
        - You have datasets with multiple numeric columns.
        - You want automatic, intelligent outlier detection.
        - Your data might have complex relationships between columns.

    ⚠️ Avoid when:
        - Dataset is very small (< 30 rows).
        - You know the contamination value and want to control it manually.

    💡 Why this method:
        - Combines IQR (for auto contamination) with Isolation Forest (for smart detection).
        - Automatically adapts to your dataset.
        - Prevents over- or under-removal of data.
    """

    try:
        # 🔍 Step 1: Select numeric columns if not provided
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

        # 🎯 Step 2: Extract numeric data
        data = df.select(columns_to_use).to_numpy()

        # 🧮 Step 3: Automatically estimate contamination if not given
        if contamination is None:
            flat_data = df.select(columns_to_use).to_numpy().flatten()
            q1, q3 = np.percentile(flat_data, [25, 75])
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            outlier_fraction = np.mean((flat_data < lower_bound) | (flat_data > upper_bound))

            # Cap between 0.01 and 0.15 (1%–15%)
            contamination = float(np.clip(outlier_fraction, 0.01, 0.15))

            print(f"📊 Auto contamination estimated as: {contamination:.3f}")

        # 🧠 Step 4: Train Isolation Forest
        iso = IsolationForest(contamination=contamination, random_state=random_state)
        preds = iso.fit_predict(data)  # 1 = normal, -1 = outlier

        # 🧩 Step 5: Create boolean mask (True = keep)
        mask = preds == 1

        # 🧱 Step 6: Apply mask to dataframe
        mask_series = pl.Series("mask", mask)
        df_clean = df.with_columns(mask_series).filter(pl.col("mask")).drop("mask")

        print(f"✅ Outliers handled successfully using Isolation Forest on: {', '.join(columns_to_use)}")
        return df_clean

    except Exception as e:
        print("⚠️ Error while handling outliers:", e)
        return df
