"""
HumData - A Humanitarian Data Analytics Helper Library
"""

from .csv import open_csv
from .excel import open_excel

__all__ = [
    "open_csv",
    "open_excel",
]
