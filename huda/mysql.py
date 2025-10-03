import polars as pl
import pymysql

def open_mysql(host, port, user, password, database, table_name):
    """
    Open data from a MySQL database into a Polars DataFrame.

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
        conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        query = f"SELECT * FROM {table_name}"
        df = pl.read_database(query, conn)
        conn.close()

        print("✅ MySQL data loaded successfully!")
        print(f"Rows: {df.height}, Columns: {df.width}")
        return df
    except Exception as e:
        print("⚠️ MySQL load error:", e)
        return None
