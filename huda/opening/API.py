import requests
import polars as pl

def open_api(url, filters=None):
    """
    Load data from a REST API URL directly into a Polars DataFrame and optionally filter it.

    Parameters:
        - url: Full API URL including endpoint
        - filters: Optional dictionary to filter rows (column=value)

    Example usage:
    ----------------------
        # Load all posts
        df = api_load("https://jsonplaceholder.typicode.com/posts")
        print(df)

        # Load comments filtered by postId = 1
        df_filtered = api_load("https://jsonplaceholder.typicode.com/comments", {"postId": 1})
        print(df_filtered)
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Convert JSON to Polars DataFrame
        if isinstance(data, list):
            df = pl.DataFrame(data)
        elif isinstance(data, dict):
            # Try to find a list inside dict
            for key, value in data.items():
                if isinstance(value, list):
                    df = pl.DataFrame(value)
                    break
            else:
                df = pl.DataFrame([data])
        else:
            print("⚠️ API did not return JSON data.")
            return None

        # Apply filters if provided
        if filters:
            for col, val in filters.items():
                if col in df.columns:
                    df = df.filter(pl.col(col) == val)

        print(f"✅ Loaded {df.height} rows from {url}")
        return df

    except Exception as e:
        print("⚠️ API load error:", e)
        return None
