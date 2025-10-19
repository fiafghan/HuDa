import polars as pl
import pandas as pd
from typing import Union, Optional, Dict, List, Any
import io


Rule = Dict[str, Any]
StandardsConfig = Dict[str, List[Rule]]


def _builtin_standards(name: str) -> StandardsConfig:
    name = (name or "").lower()
    if name == "sphere":
        return {
            # Numeric rules: each rule applies row-wise
            "numeric": [
                {
                    "column": "water_liters_per_person_per_day",
                    "op": ">=",
                    "threshold": 15.0,
                    "description": "Sphere: min 15L of safe water per person per day",
                },
                {
                    "column": "coverage_percent",
                    "op": "between_inclusive",
                    "threshold": (0.0, 100.0),
                    "description": "Coverage should be between 0% and 100%",
                },
                {
                    "column": "cmr_per_10k_per_day",
                    "op": "<=",
                    "threshold": 1.0,
                    "description": "Sphere emergency threshold: CMR <= 1/10,000/day",
                },
            ],
            # Categorical rules
            "categorical": [
                {
                    "column": "sex",
                    "allowed": ["male", "female"],
                    "description": "Standardized sex categories",
                }
            ],
        }
    if name == "ipc":
        return {
            "numeric": [
                {
                    "column": "fcs",  # Food Consumption Score (typical range 0-112)
                    "op": "between_inclusive",
                    "threshold": (0.0, 112.0),
                    "description": "FCS should be within [0, 112]",
                },
                {
                    "column": "coverage_percent",
                    "op": "between_inclusive",
                    "threshold": (0.0, 100.0),
                    "description": "Coverage should be between 0% and 100%",
                },
            ],
            "categorical": [
                {
                    "column": "ipc_phase",
                    "allowed": [1, 2, 3, 4, 5],
                    "description": "IPC phase must be 1–5",
                }
            ],
        }
    return {"numeric": [], "categorical": []}


def validate_humanitarian_indicators_against_standards(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    standards: Union[str, StandardsConfig] = "sphere",
) -> pl.DataFrame:
    """
    Validate humanitarian indicators against Sphere/IPC standards or a custom rule set.

    What this does:
    - Checks numeric and categorical indicators row-by-row against defined rules.
    - Returns a tidy violations table indicating which rows/columns break which standards.

    When to use:
    - During data quality checks before publishing analyses/dashboards.
    - After cleaning/merging, to ensure indicators comply with common standards.

    Why important:
    - Avoids reporting values outside accepted humanitarian thresholds.
    - Standardizes validation across datasets and partners.

    Where to apply:
    - Afghanistan assessments: water access, mortality, food security (IPC), coverage.

    Parameters:
    - data: CSV path, pandas.DataFrame, polars.DataFrame, or CSV file bytes.
    - standards: "sphere", "ipc", or a custom dict with:
        {
          "numeric": [
            {"column": str, "op": one of ">=","<=","<",">","==","between_inclusive", "!=", "description": str, "threshold": number or (low, high)},
          ],
          "categorical": [
            {"column": str, "allowed": List[Any], "description": str},
          ]
        }

    Returns:
    - pl.DataFrame with columns:
      - row_index, column, rule, description, value

    Afghanistan example:
    ```python
    from huda.validation_and_quality import validate_humanitarian_indicators_against_standards
    import polars as pl

    df = pl.DataFrame({
        "province": ["Kabul", "Herat", "Balkh"],
        "water_liters_per_person_per_day": [12, 18, 10],
        "ipc_phase": [3, 6, 2],
        "coverage_percent": [95, 105, -2],
    })

    # Sphere + IPC combined (simple union)
    violations = validate_humanitarian_indicators_against_standards(df, standards="sphere")
    # You can run again with IPC or pass a merged custom standard set

    print(violations)
    ```

    Example violation table:
    ┌───────────┬────────────────────────────────────┬──────────────────────────────────────────────────────────┬───────┬───────┐
    │ row_index ┆ column                             ┆ description                                              ┆ rule  ┆ value │
    ├───────────┼────────────────────────────────────┼──────────────────────────────────────────────────────────┼───────┼───────┤
    │ 0         ┆ water_liters_per_person_per_day    ┆ Sphere: min 15L of safe water per person per day        ┆ < 15  ┆ 12.0  │
    │ 1         ┆ coverage_percent                   ┆ Coverage should be between 0% and 100%                   ┆ > 100 ┆ 105.0 │
    │ 2         ┆ ipc_phase                          ┆ IPC phase must be 1–5                                    ┆ not in│ 6     │
    └───────────┴────────────────────────────────────┴──────────────────────────────────────────────────────────┴───────┴───────┘
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

    # Load standards
    if isinstance(standards, str):
        cfg = _builtin_standards(standards)
    else:
        cfg = standards or {"numeric": [], "categorical": []}

    violations_tables: List[pl.DataFrame] = []

    # Numeric rules
    for rule in cfg.get("numeric", []):
        col = rule.get("column")
        op = rule.get("op")
        thr = rule.get("threshold")
        desc = rule.get("description", "")
        if col not in df.columns:
            continue
        col_expr = pl.col(col).cast(pl.Float64, strict=False)
        if op == ">=":
            mask = col_expr < float(thr)
            rule_label = f"< {thr}"
        elif op == "<=":
            mask = col_expr > float(thr)
            rule_label = f"> {thr}"
        elif op == ">":
            mask = col_expr <= float(thr)
            rule_label = f"<= {thr}"
        elif op == "<":
            mask = col_expr >= float(thr)
            rule_label = f">= {thr}"
        elif op == "==":
            mask = col_expr != float(thr)
            rule_label = f"!= {thr}"
        elif op == "!=":
            mask = col_expr == float(thr)
            rule_label = f"== {thr}"
        elif op == "between_inclusive":
            low, high = thr
            mask = (col_expr < float(low)) | (col_expr > float(high))
            rule_label = f"not in [{low}, {high}]"
        else:
            raise ValueError(f"Unsupported op: {op}")

        tbl = df.select([
            pl.int_range(0, df.height).alias("row_index"),
            pl.col(col).alias("value"),
        ]).filter(mask)
        if tbl.height:
            violations_tables.append(
                tbl.with_columns([
                    pl.lit(col).alias("column"),
                    pl.lit(desc).alias("description"),
                    pl.lit(rule_label).alias("rule"),
                ])["row_index", "column", "description", "rule", "value"]
            )

    # Categorical rules
    for rule in cfg.get("categorical", []):
        col = rule.get("column")
        allowed = rule.get("allowed", [])
        desc = rule.get("description", "")
        if col not in df.columns:
            continue
        s = df.get_column(col)
        tbl = df.select([
            pl.int_range(0, df.height).alias("row_index"),
            pl.col(col).alias("value"),
        ]).filter(~pl.col(col).is_in(allowed))
        if tbl.height:
            violations_tables.append(
                tbl.with_columns([
                    pl.lit(col).alias("column"),
                    pl.lit(desc).alias("description"),
                    pl.lit("not in").alias("rule"),
                ])["row_index", "column", "description", "rule", "value"]
            )

    if not violations_tables:
        return pl.DataFrame({"row_index": [], "column": [], "description": [], "rule": [], "value": []})

    return pl.concat(violations_tables, how="vertical")
