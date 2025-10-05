import polars as pl
from .encoding_detector import detect_encoding

def open_csv(file_path, initial_filters=None):
    """
    🔹 Super Easy CSV Loader using Polars

    This function loads your CSV file and applies basic filters automatically.
    Beginners do NOT need to write any filter or select commands.

    Parameters:
    - file_path: Path to your CSV file (example: "data/myfile.csv")
    - initial_filters: dictionary of filters to apply automatically (optional)
        Example: {"country": "Afghanistan", "year": 2025}

    Returns:
    - Polars DataFrame ready for analysis

    Usage Examples:

    1. Load CSV without filters:
       df = load_csv_easy("data/myfile.csv")
       print(df)

    2. Load CSV and automatically filter country and year:
       df = load_csv_easy(
           "data/myfile.csv",
           initial_filters={"country": "Afghanistan", "year": 2025}
       )
       print(df)

    ✅ Notes:
    - No need to use select() or filter() manually.
    - Polars is faster than pandas for large files.
    - You can continue analysis directly on the returned DataFrame.
    """
    # Detect file encoding automatically
    encoding = detect_encoding(file_path)

    try:
        # Read CSV into Polars DataFrame
        df = pl.read_csv(file_path, encoding=encoding, try_parse_dates=True)

        # Apply initial filters automatically if provided
        if initial_filters:
            for col, val in initial_filters.items():
                if col in df.columns:
                    df = df.filter(pl.col(col) == val)

        print(f"✅ CSV loaded successfully with {len(df)} rows and {len(df.columns)} columns.")
        return df

    except Exception as e:
        print("⚠️ Error loading CSV:", e)
        return None
