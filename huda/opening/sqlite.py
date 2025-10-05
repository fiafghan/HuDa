import polars as pl
import sqlite3

def open_sqlite(db_path, table_name):
    """
    Open data from a SQLite database file into a Polars DataFrame.

    Parameters:
        - db_path: path to your SQLite .db file
        - table_name: name of the table you want to load

    Example usage:
    ----------------------
        df = open_sqlite("humanitarian_sqlite.db", "needs_table")
        print(df)

    ✅ This will show all rows from the 'needs_table' table.
    """
    try:
        conn = sqlite3.connect(db_path)
        query = f"SELECT * FROM {table_name}"
        df = pl.read_database(query, conn)
        conn.close()

        print("✅ SQLite data loaded successfully!")
        print(f"Rows: {df.height}, Columns: {df.width}")
        return df
    except Exception as e:
        print("⚠️ SQLite load error:", e)
        return None
