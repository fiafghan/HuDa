import pandas as pd
from .encoding_detector import detect_encoding

def open_csv(file_path):
    """
    Load CSV file with smart encoding + delimeter detection.
    """
    
    encoding = detect_encoding(file_path)
    try:
        df = pd.read_csv(file_path, encoding=encoding, sep=None, engine='python')
        return df
    
    except Exception as e:
        raise e












