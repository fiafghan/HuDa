import pandas as pd
from sqlalchemy import create_engine

def open_sqlite(query, db_path):
    """
    Open data from a SQLite database file.
    
    Parameters:
        - query: SQL query string
        - db_path: path to the SQLite .db file
    
    Example:
        df = open_sqlite("SELECT * FROM needs_table", "humanitarian_sqlite.db")
    """
    try:
        engine = create_engine(f"sqlite:///{db_path}")
        df = pd.read_sql_query(query, engine)
        engine.dispose()
        
        print("✅ SQLite data loaded successfully!")
        print(f"Rows: {len(df)}, Columns: {len(df.columns)}")
        return df
    
    except Exception as e:
        print("⚠️ SQLite read error:", e)
        return None
