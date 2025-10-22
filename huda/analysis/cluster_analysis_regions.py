import polars as pl
import pandas as pd
from typing import Union, List, Optional, Dict, Any
import io

def cluster_analysis_regions(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    feature_columns: List[str],
    n_clusters: int = 5,
    region_col: Optional[str] = None
) -> pl.DataFrame:
    """
    Cluster Analysis (k-means for Regions)
    =====================================

    What
    ----
    Group provinces/districts with similar indicators.

    When
    ----
    For targeting strategies or typology of areas.

    Why
    ---
    Simplifies complex data into meaningful groups.

    Parameters
    ----------
    data : str | pd.DataFrame | pl.DataFrame | io.BytesIO
        Input dataset.
    feature_columns : list[str]
        Numeric columns to cluster on.
    n_clusters : int, default 5
        Number of clusters (k).
    region_col : str | None
        Optional name column to keep in results.

    Returns
    -------
    pl.DataFrame
        Data with a placeholder cluster label column.

    Example
    -------
    >>> cluster_analysis_regions(df, feature_columns=["need","access"], n_clusters=4, region_col="province")
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

    return df.with_columns(pl.lit(0).alias("cluster"))
