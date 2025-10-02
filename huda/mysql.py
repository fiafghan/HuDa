import pandas as pd
from sqlalchemy import create_engine

def open_mysql(query, host, port, user, password, database):
    """
    Open data from a MySQL database.
    
    Example:
        df = open_mysql("SELECT * FROM needs_table", 
                        host="localhost", port=3306, 
                        user="root", password="1234", database="humanitarian_mysql")
    """
    try:
        engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
        df = pd.read_sql_query(query, engine)
        engine.dispose()
        
        print("✅ MySQL data loaded successfully!")
        print(f"Rows: {len(df)}, Columns: {len(df.columns)}")
        return df
    
    except Exception as e:
        print("⚠️ MySQL read error:", e)
        return None
