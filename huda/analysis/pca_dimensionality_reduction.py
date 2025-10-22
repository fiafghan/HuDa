import polars as pl
import pandas as pd
from typing import Union, List, Optional, Dict, Any
import io

def pca_dimensionality_reduction(
    data: Union[str, pd.DataFrame, pl.DataFrame, io.BytesIO],
    feature_columns: List[str],
    n_components: int = 2
) -> pl.DataFrame:
    """
    PCA / Dimensionality Reduction for Indicators
    ============================================

    What
    ----
    Reduce many indicators into a few components capturing most variance.

    When
    ----
    Before clustering, mapping, or dashboarding to simplify.

    Why
    ---
    Easier to visualize and interpret complex data.

    Parameters
    ----------
    data : str | pd.DataFrame | pl.DataFrame | io.BytesIO
        Input dataset.
    feature_columns : list[str]
        Numeric columns for PCA.
    n_components : int, default 2
        Number of principal components.

    Returns
    -------
    pl.DataFrame
        Original data plus placeholder component columns.

    Example
    -------
    >>> pca_dimensionality_reduction(df, feature_columns=["need","coverage"], n_components=2)
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

    return df.with_columns([
        pl.lit(0.0).alias("pc1"),
        pl.lit(0.0).alias("pc2")
    ])
