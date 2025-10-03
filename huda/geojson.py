# geojson_loader_fixed.py
import polars as pl
import geopandas as gpd

def open_geojson(file_path):
    """
    Load a GeoJSON file easily into Polars DataFrame for analysis.

    Returns:
        - gdf: GeoPandas GeoDataFrame (with geometry)
        - df: Polars DataFrame (only attributes, safe for Polars)
    
    Example usage:
    ----------------------
    gdf, df = open_geojson("test_afghanistan.geojson")
    print(gdf.head())  # GeoPandas with geometry
    print(df.head())   # Polars with attributes only
    """
    try:
        # Load GeoJSON
        gdf = gpd.read_file(file_path)
        print("✅ GeoJSON loaded successfully as GeoDataFrame!")
        print(f"Rows: {len(gdf)}, Columns: {len(gdf.columns)}")

        # Extract only non-geometry columns for Polars
        attribute_columns = [col for col in gdf.columns if col != "geometry"]
        df = pl.from_pandas(gdf[attribute_columns])

        return gdf, df

    except FileNotFoundError:
        print("⚠️ File not found. Please check the file name and path.")
        return None, None
    except Exception as e:
        print("⚠️ Something went wrong while loading the GeoJSON file.")
        print("Error:", e)
        return None, None
