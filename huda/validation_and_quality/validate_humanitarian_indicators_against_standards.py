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


def _normalize_key(s: str) -> str:
    """Lowercase and keep alphanumerics/underscore to compare column names flexibly."""
    return "".join(ch for ch in s.lower() if ch.isalnum() or ch == "_")


def _resolve_column(
    df: pl.DataFrame,
    canonical: str,
    column_aliases: Optional[Dict[str, str]] = None,
    synonyms: Optional[Dict[str, List[str]]] = None,
) -> Optional[str]:
    """
    Resolve an actual dataframe column name for a canonical indicator name.
    Priority:
    1) explicit column_aliases mapping
    2) exact match (case-insensitive)
    3) synonyms list match (case-insensitive)
    Returns the matched column name or None if not found.
    """
    column_aliases = column_aliases or {}
    synonyms = synonyms or {}

    # Build lookup of normalized df columns
    df_cols_norm = {_normalize_key(c): c for c in df.columns}

    # 1) explicit mapping
    if canonical in column_aliases:
        cand = column_aliases[canonical]
        if cand in df.columns:
            return cand
        # try normalized match
        cand_norm = _normalize_key(cand)
        if cand_norm in df_cols_norm:
            return df_cols_norm[cand_norm]

    # 2) exact/normalized canonical
    can_norm = _normalize_key(canonical)
    if can_norm in df_cols_norm:
        return df_cols_norm[can_norm]

    # 3) synonyms
    for syn in synonyms.get(canonical, []):
        syn_norm = _normalize_key(syn)
        if syn_norm in df_cols_norm:
            return df_cols_norm[syn_norm]

    return None


def validate_humanitarian_indicators_against_standards(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    standards: Union[str, StandardsConfig] = "sphere",
    column_aliases: Optional[Dict[str, str]] = None,
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
    - column_aliases: Optional explicit mapping from canonical indicator names
      (e.g., "coverage_percent") to your dataset's column names (e.g., "coverage").
      If omitted, common synonyms are auto-detected (e.g., "sex" -> "gender").

    Returns:
    - pl.DataFrame with columns:
      - row_index, column, rule, description, value

    Afghanistan example:
    ```python
    from huda.validation_and_quality import validate_humanitarian_indicators_against_standards
    import polars as pl

    # Simple column names (auto-mapped):
    df = pl.DataFrame({
        "province": ["Kabul", "Herat", "Balkh"],
        "water_per_person": [12, 18, 10],          # auto -> water_liters_per_person_per_day
        "ipc": [3, 6, 2],                           # auto -> ipc_phase
        "coverage": [95, 105, -2],                  # auto -> coverage_percent
        "sex": ["male", "female", "other"],       # matches categorical
        "cmr_per_10k": [0.8, 1.2, 0.5],             # auto -> cmr_per_10k_per_day
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

    # Synonyms for auto-mapping common column names
    synonyms: Dict[str, List[str]] = {
        "water_liters_per_person_per_day": ["water_per_person", "water_liters", "water_lppd", "waterppd"],
        "coverage_percent": ["coverage", "coverage_pct", "pct_coverage"],
        "cmr_per_10k_per_day": ["cmr", "cmr_per_10k", "cmr10k"],
        "ipc_phase": ["ipc", "phase"],
        "sex": ["gender"],
        "fcs": ["food_consumption_score"],
    }

    # Add row index once to avoid ColumnNotFound during filtering
    df_idx = df.with_row_count("row_index")

    # Numeric rules
    for rule in cfg.get("numeric", []):
        canonical_col = rule.get("column")
        op = rule.get("op")
        thr = rule.get("threshold")
        desc = rule.get("description", "")
        actual_col = _resolve_column(df, canonical_col, column_aliases, synonyms)
        if actual_col is None:
            continue
        col_expr = pl.col(actual_col).cast(pl.Float64, strict=False)
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

        tbl = df_idx.filter(mask).select([
            "row_index",
            pl.col(actual_col).alias("value"),
        ])
        if tbl.height:
            violations_tables.append(
                tbl.with_columns([
                    pl.lit(actual_col).alias("column"),
                    pl.lit(desc).alias("description"),
                    pl.lit(rule_label).alias("rule"),
                ])["row_index", "column", "description", "rule", "value"]
            )

    # Categorical rules
    for rule in cfg.get("categorical", []):
        canonical_col = rule.get("column")
        allowed = rule.get("allowed", [])
        desc = rule.get("description", "")
        actual_col = _resolve_column(df, canonical_col, column_aliases, synonyms)
        if actual_col is None:
            continue
        tbl = df_idx.filter(~pl.col(actual_col).is_in(allowed)).select([
            "row_index",
            pl.col(actual_col).alias("value"),
        ])
        if tbl.height:
            violations_tables.append(
                tbl.with_columns([
                    pl.lit(actual_col).alias("column"),
                    pl.lit(desc).alias("description"),
                    pl.lit("not in").alias("rule"),
                ])["row_index", "column", "description", "rule", "value"]
            )

    if not violations_tables:
        return pl.DataFrame({"row_index": [], "column": [], "description": [], "rule": [], "value": []})

    return pl.concat(violations_tables, how="vertical")
