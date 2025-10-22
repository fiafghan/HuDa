import polars as pl
import pandas as pd
from typing import Union, Optional, List, Dict
import io


def coping_strategy_index(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    strategy_cols: Dict[str, str],
    weights: Optional[Dict[str, float]] = None,
    group_by: Optional[List[str]] = None
) -> pl.DataFrame:
    """
    Coping Strategy Index (rCSI-like)
    =================================

    What
    ----
    Compute a simple coping index from strategy frequency/severity and weights.

    When
    ----
    Food security and shocks assessments.

    Why
    ---
    Summarize reliance on harmful coping strategies.

    Parameters
    ----------
    data : str | pd.DataFrame | pl.DataFrame | io.BytesIO
        Input dataset.
    strategy_cols : dict[str,str]
        Map of strategy name -> column containing frequency or severity.
    weights : dict[str,float] | None
        Optional weights for each strategy.
    group_by : list[str] | None
        Optional grouping.

    Returns
    -------
    pl.DataFrame
        With placeholder coping index column.
    """
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

    weights = weights or {k: 1.0 for k in strategy_cols.keys()}
    exprs = []
    for name, col in strategy_cols.items():
        w = float(weights.get(name, 1.0))
        exprs.append(pl.col(col).cast(pl.Float64) * w)
    score = exprs[0] if exprs else pl.lit(0.0)
    for e in exprs[1:]:
        score = score + e
    return df.with_columns(score.alias("coping_index_placeholder"))
