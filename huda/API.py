import requests
import pandas as pd

def api_load(url, filters=None):
    """
    Load data from a REST API URL directly into a DataFrame and optionally filter it.
    
    Parameters:
        - url: Full API URL including endpoint
        - filters: Optional dictionary to filter rows (column=value)
    
    Example:
        df = api_load("https://jsonplaceholder.typicode.com/posts")
        df_filtered = api_load("https://jsonplaceholder.typicode.com/comments", {"postId": 1})
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Convert JSON to DataFrame
        if isinstance(data, list):
            df = pd.DataFrame(data)
        elif isinstance(data, dict):
            # Try to find a list inside dict
            for key, value in data.items():
                if isinstance(value, list):
                    df = pd.DataFrame(value)
                    break
            else:
                df = pd.DataFrame([data])
        else:
            print("⚠️ API did not return JSON data.")
            return None

        # Apply filters if provided
        if filters:
            for col, val in filters.items():
                if col in df.columns:
                    df = df[df[col] == val]

        print(f"✅ Loaded {len(df)} rows from {url}")
        return df

    except Exception as e:
        print("⚠️ API load error:", e)
        return None
