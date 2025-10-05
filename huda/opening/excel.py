import polars as pl

def open_excel(file_path, initial_filters=None, sheet_name=None):
    """
    🔹 Super Easy Excel Loader using Polars

    This function loads your Excel file and applies basic filters automatically.
    Beginners do NOT need to write any filter or select commands.

    Parameters:
    - file_path: Path to your Excel file (example: "data/myfile.xlsx")
    - sheet_name: Name or index of the sheet to load (default is 0, the first sheet)
    - initial_filters: dictionary of filters to apply automatically (optional)
        Example: {"country": "Afghanistan", "year": 2025}

    Returns:
    - Polars DataFrame ready for analysis

    Usage Examples:

    1. Load Excel without filters:
       df = load_excel_easy("data/sample.xlsx")
       print(df)

    2. Load Excel with automatic filter: country = Afghanistan
       df_afg = load_excel_easy(
           "data/sample.xlsx",
           initial_filters={"country": "Afghanistan"}
       )
       print(df_afg)

    3. Load Excel with multiple filters: country = Afghanistan, year = 2025
       df_afg_2025 = load_excel_easy(
           "data/sample.xlsx",
           initial_filters={"country": "Afghanistan", "year": 2025}
       )
       print(df_afg_2025)

    ✅ Notes:
    - No need to use select() or filter() manually.
    - Polars is faster than pandas for large Excel files.
    - You can continue analysis directly on the returned DataFrame.
    """
    try:
        # Read Excel file using Polars
        df = pl.read_excel(file_path, sheet_name=sheet_name)

        # Apply initial filters automatically if provided
        if initial_filters:
            for col, val in initial_filters.items():
                if col in df.columns:
                    df = df.filter(pl.col(col) == val)

        print(f"✅ Excel file loaded successfully with {df.shape[0]} rows and {df.shape[1]} columns.")
        return df

    except FileNotFoundError:
        print("⚠️ Oops! File not found. Check the file name and path.")
        return None
    except Exception as e:
        print("⚠️ Something went wrong while opening the Excel file.")
        print("Error:", e)
        return None
