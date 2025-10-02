import pandas as pd
import json

def open_json(file_path):
    """
    Open JSON file easily!
    - file_path: path to your JSON file
    
    Works for normal JSON files and converts them into a table (DataFrame).
    """
    try:
        # Try reading as a JSON table directly
        df = pd.read_json(file_path)
        print("✅ JSON file opened successfully as a table!")
        print(f"Rows: {len(df)}, Columns: {len(df.columns)}")
        return df
    except ValueError:
        # If pandas fails, read as general JSON
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print("✅ JSON loaded successfully as Python data (not a table).")
            return data
        except FileNotFoundError:
            print("⚠️ Oops! File not found. Check the file name and path.")
            return None
        except Exception as e:
            print("⚠️ Something went wrong while opening the JSON file.")
            print("Error:", e)
            return None
    except FileNotFoundError:
        print("⚠️ Oops! File not found. Check the file name and path.")
        return None
