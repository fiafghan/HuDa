"""
HumData - A Humanitarian Data Analytics Helper Library
"""

from .csv_loader import open_csv
from .excel_loader import open_excel

__all__ = [
    "open_csv",
    "open_excel",
]
