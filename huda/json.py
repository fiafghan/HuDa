import polars as pl
import json

def open_json(file_path, initial_filters=None):
    """
    🔹 Super Easy JSON Loader with Polars

    This function loads a JSON file and converts it into a Polars DataFrame.
    Beginners do NOT need to write select() or filter() commands.

    Parameters:
    - file_path: path to your JSON file (example: "data/sample.json")
    - initial_filters: dictionary of basic filters to apply automatically (optional)
        Example: {"country": "Afghanistan", "year": 2025}

    Returns:
    - Polars DataFrame ready for analysis
    - Or Python data if JSON cannot be converted into a table

    Usage Examples:

    1. Load JSON directly:
       df = load_json_easy("data/sample.json")
       print(df)

    2. Load JSON and automatically filter:
       df = load_json_easy(
           "data/sample.json",
           initial_filters={"country": "Afghanistan", "year": 2025}
       )
       print(df)

    ✅ Notes:
    - Polars is faster than pandas for table-like JSON data.
    - If JSON is nested or not a table, it will be returned as Python data.
    """
    try:
        # Try reading as table-like JSON using Polars
        df = pl.read_json(file_path)

        # Apply initial filters automatically if provided
        if initial_filters:
            for col, val in initial_filters.items():
                if col in df.columns:
                    df = df.filter(pl.col(col) == val)

        print(f"✅ JSON file opened successfully with {len(df)} rows and {len(df.columns)} columns.")
        return df

    except Exception:
        # Fallback: read as general Python JSON
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print("✅ JSON loaded successfully as Python data (not a table).")
            return data
        except FileNotFoundError:
            print("⚠️ Oops! File not found. Check the file name and path.")
            return None
        except Exception as e:
            print("⚠️ Something went wrong while opening the JSON file.")
            print("Error:", e)
            return None
