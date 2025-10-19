import polars as pl
import pandas as pd
from typing import Union, Dict
import io


def automatic_data_profiling_report(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    top_k: int = 10,
) -> Dict[str, pl.DataFrame]:
    """
    Create an automatic data profiling report with multiple tidy tables.

    What this does:
    - Generates a set of tables to quickly understand a dataset:
      - summary_per_column: dtype, counts, missing, uniques, basic numeric stats.
      - numeric_details: extended numeric stats (quantiles).
      - categorical_details: top-k value frequencies per categorical column.
      - datetime_details: min/max per datetime-like columns.

    When to use:
    - First look at any new dataset, after ingestion/cleaning.
    - Before analysis or model building to spot issues and distributions.

    Why important:
    - Surfaces missingness, ranges, and dominant categories early.
    - Guides cleaning (imputation, capping) and indicator selection.

    Where to apply:
    - Afghanistan assessments and activity tracking (e.g., Kabul/Herat/Balkh surveys).

    Parameters:
    - data: CSV path, pandas.DataFrame, polars.DataFrame, or CSV bytes.
    - top_k: number of most frequent categories to report per categorical column.

    Returns:
    - dict[str, pl.DataFrame] with keys:
      - "summary_per_column"
      - "numeric_details"
      - "categorical_details"
      - "datetime_details"

    Afghanistan example:
    ```python
    from huda.validation_and_quality import automatic_data_profiling_report
    import polars as pl

    df = pl.DataFrame({
        "province": ["Kabul", "Herat", "Balkh", "Kabul"],
        "households_targeted": [1000, 800, 600, 500],
        "households_reached": [950, 700, 600, None],
        "assessment_date": ["2025-05-01", "2025-05-02", "2025-05-03", "2025-05-04"],
    })

    report = automatic_data_profiling_report(df)
    for name, tbl in report.items():
        print(f"\n=== {name} ===")
        print(tbl)
    ```

    Example outputs:

    summary_per_column
    ┌──────────────────────┬──────────┬───────┬────────────┬──────────────┬──────┬──────┬───────┬────────┬─────────┐
    │ column               ┆ dtype    ┆ count ┆ null_count ┆ unique_count ┆ min  ┆ max  ┆ mean  ┆ median ┆ std     │
    ├──────────────────────┼──────────┼───────┼────────────┼──────────────┼──────┼──────┼───────┼────────┼─────────┤
    │ province             ┆ Utf8     ┆ 4     ┆ 0          ┆ 3            ┆      ┆      ┆       ┆        ┆         │
    │ households_targeted  ┆ Int64    ┆ 4     ┆ 0          ┆ 4            ┆ 500  ┆ 1000 ┆ 725.0 ┆ 700.0  ┆ 216.02  │
    │ households_reached   ┆ Float64  ┆ 3     ┆ 1          ┆ 3            ┆ 600  ┆ 950  ┆ 750.0 ┆ 700.0  ┆ 176.78  │
    │ assessment_date      ┆ Utf8     ┆ 4     ┆ 0          ┆ 4            ┆      ┆      ┆       ┆        ┆         │
    └──────────────────────┴──────────┴───────┴────────────┴──────────────┴──────┴──────┴───────┴────────┴─────────┘

    numeric_details
    ┌─────────────────────┬──────┬──────┬───────┬────────┬────────┬────────┐
    │ column              ┆ q01  ┆ q05  ┆ q25   ┆ q50    ┆ q75    ┆ q95    │
    ├─────────────────────┼──────┼──────┼───────┼────────┼────────┼────────┤
    │ households_targeted ┆ 515  ┆ 525  ┆ 650   ┆ 700    ┆ 875    ┆ 975    │
    │ households_reached  ┆ 600  ┆ 625  ┆ 650   ┆ 700    ┆ 825    ┆ 925    │
    └─────────────────────┴──────┴──────┴───────┴────────┴────────┴────────┘

    categorical_details (top 10)
    ┌──────────┬──────────┬───────┬────────┐
    │ column   ┆ value    ┆ count ┆ freq   │
    ├──────────┼──────────┼───────┼────────┤
    │ province ┆ Kabul    ┆ 2     ┆ 0.50   │
    │ province ┆ Herat    ┆ 1     ┆ 0.25   │
    │ province ┆ Balkh    ┆ 1     ┆ 0.25   │
    └──────────┴──────────┴───────┴────────┘

    datetime_details
    ┌─────────────────┬────────────┬────────────┐
    │ column          ┆ min_date   ┆ max_date   │
    ├─────────────────┼────────────┼────────────┤
    │ assessment_date ┆ 2025-05-01 ┆ 2025-05-04 │
    └─────────────────┴────────────┴────────────┘
    """
    # Normalize input
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

    n_rows = df.height

    # Detect types
    numeric_types = {
        pl.Int8, pl.Int16, pl.Int32, pl.Int64,
        pl.UInt8, pl.UInt16, pl.UInt32, pl.UInt64,
        pl.Float32, pl.Float64
    }

    # Try to parse datelike strings into Date for profiling
    df_cast = df.clone()
    datetime_cols: list[str] = []
    for c in df_cast.columns:
        s = df_cast.get_column(c)
        # Try parsing only if Utf8 and looks date-like in some rows
        if s.dtype == pl.Utf8:
            try:
                parsed = pl.Series(c, pl.Series(s).str.strptime(pl.Date, strict=False))
                if parsed.drop_nulls().len() > 0:
                    df_cast = df_cast.with_columns(parsed)
                    datetime_cols.append(c)
            except Exception:
                pass
        elif s.dtype in (pl.Date, pl.Datetime):
            datetime_cols.append(c)

    # Summary per column
    rows = []
    for col in df_cast.columns:
        s = df_cast.get_column(col)
        dtype = s.dtype
        null_count = s.null_count()
        unique_count = s.n_unique()
        count = n_rows - null_count
        if dtype in numeric_types:
            agg = df_cast.select(
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

    summary_per_column = pl.DataFrame(rows)

    # Numeric details with quantiles
    numeric_cols = [c for c in df_cast.columns if df_cast.get_column(c).dtype in numeric_types]
    numeric_tables = []
    for c in numeric_cols:
        q = df_cast.select([
            pl.col(c).quantile(0.01, interpolation="nearest").alias("q01"),
            pl.col(c).quantile(0.05, interpolation="nearest").alias("q05"),
            pl.col(c).quantile(0.25, interpolation="nearest").alias("q25"),
            pl.col(c).quantile(0.50, interpolation="nearest").alias("q50"),
            pl.col(c).quantile(0.75, interpolation="nearest").alias("q75"),
            pl.col(c).quantile(0.95, interpolation="nearest").alias("q95"),
        ])
        numeric_tables.append(q.with_columns(pl.lit(c).alias("column")).select(["column", "q01", "q05", "q25", "q50", "q75", "q95"]))
    numeric_details = pl.concat(numeric_tables, how="vertical") if numeric_tables else pl.DataFrame({"column": [], "q01": [], "q05": [], "q25": [], "q50": [], "q75": [], "q95": []})

    # Categorical details: top-k frequencies
    categorical_cols = [
        c for c in df_cast.columns
        if (df_cast.get_column(c).dtype not in numeric_types) and (c not in datetime_cols)
    ]
    cat_tables = []
    for c in categorical_cols:
        freq = df_cast.group_by(c).agg(pl.len().alias("count")).sort("count", descending=True).with_columns((pl.col("count") / n_rows).alias("freq")).head(top_k)
        if freq.height:
            # Rename value column to 'value'
            freq = freq.rename({c: "value"})
            freq = freq.with_columns(pl.lit(c).alias("column")).select(["column", "value", "count", "freq"])
            cat_tables.append(freq)
    categorical_details = pl.concat(cat_tables, how="vertical") if cat_tables else pl.DataFrame({"column": [], "value": [], "count": [], "freq": []})

    # Datetime details
    dt_tables = []
    for c in datetime_cols:
        dt = df_cast.select([
            pl.col(c).min().alias("min_date"),
            pl.col(c).max().alias("max_date"),
        ])
        dt_tables.append(dt.with_columns(pl.lit(c).alias("column")).select(["column", "min_date", "max_date"]))
    datetime_details = pl.concat(dt_tables, how="vertical") if dt_tables else pl.DataFrame({"column": [], "min_date": [], "max_date": []})

    return {
        "summary_per_column": summary_per_column,
        "numeric_details": numeric_details,
        "categorical_details": categorical_details,
        "datetime_details": datetime_details,
    }
