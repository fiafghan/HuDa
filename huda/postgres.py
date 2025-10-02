import pandas as pd
from sqlalchemy import create_engine

def open_postgres(query, host, port, user, password, database):
    """
    Open data from a PostgreSQL database.
    
    Example:
        df = open_postgres("SELECT * FROM needs_table",
                           host="localhost", port=5432,
                           user="postgres", password="1234", database="humanitarian_pg")
    """
    try:
        engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")
        df = pd.read_sql_query(query, engine)
        engine.dispose()
        
        print("✅ PostgreSQL data loaded successfully!")
        print(f"Rows: {len(df)}, Columns: {len(df.columns)}")
        return df
    
    except Exception as e:
        print("⚠️ PostgreSQL read error:", e)
        return None
