import polars as pl
import pandas as pd
from typing import Union, Optional
import io


def generate_summary_statistics_per_dataset(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO]
) -> pl.DataFrame:
    """
    Generate clear, per-column summary statistics for a dataset.

    What this does:
    - Produces a tidy table with one row per column in the dataset.
    - Includes column data type, counts, missing values, unique values, and
      numeric summaries (min, max, mean, median, std) where applicable.

    When to use:
    - Early data exploration and quality review.
    - Before analysis and visualization to understand distributions and gaps.

    Why important:
    - Quickly surfaces data issues (missing values, unexpected types).
    - Helps select the right cleaning and transformation steps.

    Where to apply:
    - Afghanistan survey datasets (e.g., household assessments in Kabul, Herat, Balkh),
      sector activity tracking (targeted vs reached), and monitoring data.

    Example (Afghanistan):
    ```python
    import polars as pl
    from huda.validation_and_quality import generate_summary_statistics_per_dataset

    df = pl.DataFrame({
        "province": ["Kabul", "Herat", "Balkh", "Kabul"],
        "households_targeted": [1000, 800, 600, 500],
        "households_reached": [950, 700, 600, None],
    })

    stats = generate_summary_statistics_per_dataset(df)
    print(stats)
    ```

    Returns a Polars DataFrame with columns like:
    - column
    - dtype
    - count
    - null_count
    - unique_count
    - min, max, mean, median, std (for numeric columns; null for non-numeric)
    """
    # 1) Normalize input to Polars DataFrame
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

    # 2) Build per-column summary
    rows = []
    total_rows = df.height

    numeric_types = {
        pl.Int8, pl.Int16, pl.Int32, pl.Int64,
        pl.UInt8, pl.UInt16, pl.UInt32, pl.UInt64,
        pl.Float32, pl.Float64
    }

    for col in df.columns:
        s = df.get_column(col)
        dtype = s.dtype
        is_numeric = dtype in numeric_types

        # counts
        null_count = s.null_count()
        unique_count = s.n_unique()
        count = total_rows - null_count

        # numeric summaries
        if is_numeric:
            # Use select for performance when possible
            agg = df.select(
                pl.col(col).min().alias("min"),
                pl.col(col).max().alias("max"),
                pl.col(col).mean().alias("mean"),
                pl.col(col).median().alias("median"),
                pl.col(col).std().alias("std"),
            ).row(0)
            min_v, max_v, mean_v, median_v, std_v = agg
        else:
            min_v = max_v = mean_v = median_v = std_v = None

        rows.append({
            "column": col,
            "dtype": str(dtype),
            "count": count,
            "null_count": null_count,
            "unique_count": unique_count,
            "min": min_v,
            "max": max_v,
            "mean": mean_v,
            "median": median_v,
            "std": std_v,
        })

    return pl.DataFrame(rows)
