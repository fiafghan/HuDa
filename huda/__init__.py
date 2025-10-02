"""
HumData - A Humanitarian Data Analytics Helper Library
"""

from .csv import open_csv
from .excel import open_excel
from .json import open_json

__all__ = [
    "open_csv",
    "open_excel",
    "open_json",
]
