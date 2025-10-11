import polars as pl
import pandas as pd
from typing import Union, Optional, Dict, List
import io


def categorical_code_to_label(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    code_column: str,
    mapping: Optional[Dict[Union[int, str], str]] = None,
    new_column_name: Optional[str] = None,
    group_by_cols: Optional[List[str]] = None
) -> pl.DataFrame:
    """
    🏷️ Convert Categorical Codes to Human-Readable Labels
    ======================================================

    🧭 What this function does:
    ----------------------------
    Many humanitarian or survey datasets use numeric or coded values  
    (like `1, 2, 3`) for categories such as food type, sector, or status.  
    This function replaces those **codes** with **readable labels** (like “Food”, “Shelter”, “Education”).

    💡 Afghanistan Example:
    -----------------------
    Imagine your dataset looks like this:

    ┌────────────┬──────────┐
    │ province   ┆ sector   │
    ├────────────┼──────────┤
    │ Kabul      ┆ 1        │
    │ Herat      ┆ 2        │
    │ Kandahar   ┆ 3        │
    │ Balkh      ┆ 1        │
    └────────────┴──────────┘

    You can pass a mapping like:
    ```python
    mapping = {
        1: "Food",
        2: "Shelter",
        3: "Education"
    }
    ```

    After conversion, it becomes:

    ┌────────────┬──────────┬────────────┐
    │ province   ┆ sector   ┆ sector_label │
    ├────────────┼──────────┼────────────┤
    │ Kabul      ┆ 1        ┆ Food        │
    │ Herat      ┆ 2        ┆ Shelter     │
    │ Kandahar   ┆ 3        ┆ Education   │
    │ Balkh      ┆ 1        ┆ Food        │
    └────────────┴──────────┴────────────┘

    🧮 Parameters:
    --------------
    data : str | pandas.DataFrame | polars.DataFrame | io.BytesIO  
        Input dataset (file path, dataframe, or file bytes)

    code_column : str  
        The name of the column containing category codes (e.g., “sector”)

    mapping : dict, optional  
        A dictionary defining what each code means.  
        Example:
        ```python
        {1: "Food", 2: "Shelter", 3: "Education"}
        ```
        If not given, you can still run the function but you’ll get “Unknown” for unmapped codes.

    new_column_name : str, optional  
        Name of the new column to store the readable label.  
        Defaults to `"{code_column}_label"`

    group_by_cols : List[str], optional  
        Optional list of columns to group by and count how many entries exist for each label.

    🕒 When to Use:
    ---------------
    - When datasets store category information as numeric codes  
    - Before presenting data in dashboards, Excel, or reports  
    - When merging datasets from different sources with different coding systems  

    🤔 Why Useful:
    ---------------
    - Converts confusing codes into clear text (like `1 → Food`)  
    - Makes data understandable for non-technical staff  
    - Helps generate readable charts, summaries, and tables  

    🌍 Where to Apply:
    ------------------
    - Afghanistan humanitarian aid datasets  
    - Sector, cluster, or response reports  
    - Health, education, or protection survey data  

    📊 Example Usage:
    -----------------
    ```python
    import polars as pl

    df = pl.DataFrame({
        "province": ["Kabul", "Herat", "Kandahar", "Balkh"],
        "sector": [1, 2, 3, 1]
    })

    mapping = {1: "Food", 2: "Shelter", 3: "Education"}

    result = categorical_code_to_label(
        data=df,
        code_column="sector",
        mapping=mapping
    )

    print(result)
    ```

    ✅ Expected Output:
    -------------------
    ┌────────────┬──────────┬────────────┐
    │ province   ┆ sector   ┆ sector_label │
    ├────────────┼──────────┼────────────┤
    │ Kabul      ┆ 1        ┆ Food        │
    │ Herat      ┆ 2        ┆ Shelter     │
    │ Kandahar   ┆ 3        ┆ Education   │
    │ Balkh      ┆ 1        ┆ Food        │
    └────────────┴──────────┴────────────┘

    🧾 Example (Grouped by Province):
    --------------------------------
    ```python
    result = categorical_code_to_label(
        data=df,
        code_column="sector",
        mapping=mapping,
        group_by_cols=["province"]
    )
    ```

    Produces:

    ┌────────────┬────────────┬──────────┐
    │ province   ┆ sector_label ┆ count    │
    ├────────────┼────────────┼──────────┤
    │ Kabul      ┆ Food        ┆ 1        │
    │ Herat      ┆ Shelter     ┆ 1        │
    │ Kandahar   ┆ Education   ┆ 1        │
    │ Balkh      ┆ Food        ┆ 1        │
    └────────────┴────────────┴──────────┘
    """

    # --- 1. Convert input to Polars DataFrame ---
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

    # --- 2. Default mapping handling ---
    if mapping is None:
        mapping = {}

    # --- 3. Default new column name ---
    if new_column_name is None:
        new_column_name = f"{code_column}_label"

    # --- 4. Convert codes to labels ---
    df = df.with_columns(
        pl.col(code_column)
        .map_elements(lambda x: mapping.get(x, "Unknown"))
        .alias(new_column_name)
    )

    # --- 5. Optional grouping ---
    if group_by_cols:
        df = df.group_by(group_by_cols + [new_column_name]).agg(pl.count().alias("count"))

    return df
