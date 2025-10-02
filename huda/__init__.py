"""
HumData - A Humanitarian Data Analytics Helper Library
"""

from .csv import open_csv
from .excel import open_excel
from .json import open_json
from .xml import openxml

__all__ = [
    "open_csv",
    "open_excel",
    "open_json",
    "open_xml",
]
