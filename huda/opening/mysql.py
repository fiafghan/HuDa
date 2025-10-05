import polars as pl
from sqlalchemy import create_engine

def open_mysql(host, port, user, password, database, table_name):
    """
    Open data from a MySQL database into a Polars DataFrame using SQLAlchemy.

    Parameters:
        - host, port, user, password, database: MySQL connection details
        - table_name: name of the table to load

    Example usage:
    ----------------------
        df = open_mysql("localhost", 3306, "root", "1234", "humanitarian_mysql", "needs_table")
        print(df)

    ✅ This will show all rows from 'needs_table'.
    """
    try:
        # Create SQLAlchemy engine (Polars can read from this)
        engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

        # Build query
        query = f"SELECT * FROM {table_name}"

        # Load data into Polars
        df = pl.read_database(query, engine)

        # Dispose engine
        engine.dispose()

        print("✅ MySQL data loaded successfully!")
        print(f"Rows: {df.height}, Columns: {df.width}")
        return df

    except Exception as e:
        print("⚠️ MySQL load error:", e)
        return None
