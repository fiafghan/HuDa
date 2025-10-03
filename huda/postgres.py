import polars as pl
import psycopg2

def open_postgres(host, port, user, password, database, table_name):
    """
    Open data from a PostgreSQL database into a Polars DataFrame.

    Parameters:
        - host, port, user, password, database: PostgreSQL connection details
        - table_name: name of the table to load

    Example usage:
    ----------------------
        df = open_postgres("localhost", 5432, "postgres", "1234", "humanitarian_db", "needs_table")
        print(df)

    ✅ This will show all rows from 'needs_table'.
    """
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            dbname=database
        )
        query = f"SELECT * FROM {table_name}"
        df = pl.read_database(query, conn)
        conn.close()

        print("✅ PostgreSQL data loaded successfully!")
        print(f"Rows: {df.height}, Columns: {df.width}")
        return df
    except Exception as e:
        print("⚠️ PostgreSQL load error:", e)
        return None
