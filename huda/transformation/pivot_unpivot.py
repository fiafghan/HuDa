import polars as pl
from typing import Union

def pivot_unpivot(
    data: Union[str, "pd.DataFrame", pl.DataFrame],
    index: list = None,
    columns: str = None,
    values: list = None,
    operation: str = "pivot"
) -> pl.DataFrame:
    """
    🔄 Pivot / Unpivot Data (Wide ↔ Long)
    ====================================

    What it does:
    -------------
    - Converts your dataset from wide format to long format or vice versa
    - Works automatically on CSV, Pandas DF, or Polars DF
    - Useful for time-series, survey results, or indicator analysis

    Parameters:
    -----------
    data : str | pd.DataFrame | pl.DataFrame
        CSV path, Pandas DataFrame, or Polars DataFrame
    index : list of str, optional
        Columns to keep as identifier (for pivot or unpivot)
    columns : str, optional
        Column to pivot on (only for pivot)
    values : list of str, optional
        Columns to aggregate or unpivot
    operation : str, default="pivot"
        "pivot" → wide format
        "unpivot" → long format

    Returns:
    --------
    pl.DataFrame
        Pivoted or unpivoted table

    Example Usage:
    --------------

    import polars as pl

    # Sample Afghan survey dataset
    df = pl.DataFrame({
        "province": ["Kabul", "Herat", "Kandahar"],
        "beneficiaries_jan": [120, 200, 250],
        "beneficiaries_feb": [150, 180, 300]
    })

    # Pivot example (wide)
    df_pivot = pivot_unpivot(
        df,
        index=["province"],
        columns="month",
        values=["beneficiaries_jan", "beneficiaries_feb"],
        operation="pivot"
    )

    # Unpivot example (long)
    df_unpivot = pivot_unpivot(
        df,
        index=["province"],
        values=["beneficiaries_jan", "beneficiaries_feb"],
        operation="unpivot"
    )

    """

    try:
        # Step 1: Convert input to Polars DataFrame if needed
        if isinstance(data, str):
            df = pl.read_csv(data)
        elif "pandas" in str(type(data)):
            import pandas as pd
            df = pl.from_pandas(data)
        elif isinstance(data, pl.DataFrame):
            df = data
        else:
            raise TypeError("Input must be CSV path, Pandas DataFrame, or Polars DataFrame")

        # Step 2: Decide operation
        op = operation.lower()
        if op == "pivot":
            if not index or not columns or not values:
                raise ValueError("For pivot, provide index, columns, and values")
            df_wide = df.pivot(
                values=values,
                index=index,
                columns=columns,
                aggregate_fn="first"  # use first if no aggregation needed
            )
            print("✅ Data pivoted to wide format")
            return df_wide

        elif op == "unpivot":
            if not index or not values:
                raise ValueError("For unpivot, provide index and values")
            df_long = df.melt(
                id_vars=index,
                value_vars=values,
                variable_name="variable",
                value_name="value"
            )
            print("✅ Data unpivoted to long format")
            return df_long

        else:
            raise ValueError("operation must be 'pivot' or 'unpivot'")

    except Exception as e:
        print("⚠️ Error in pivot/unpivot operation:", e)
        return None
