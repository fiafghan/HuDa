# netcdf_loader.py
import xarray as xr
import polars as pl

def open_netcdf(file_path, variable=None):
    """
    📘 Load NetCDF file easily and convert to Polars DataFrame for analysis.

    Parameters:
        - file_path: path to your .nc file
        - variable: optional, name of the variable to extract (e.g., "temperature")

    Example usage:
    -------------------------
        df = open_netcdf("sample_data.nc", variable="temperature")
        print(df)

    ✅ This will convert NetCDF data into a table ready for analysis.
    """
    try:
        ds = xr.open_dataset(file_path)
        print("✅ NetCDF file opened successfully!")

        if variable:
            if variable in ds:
                data = ds[variable].to_dataframe().reset_index()
            else:
                print(f"⚠️ Variable '{variable}' not found. Loading all variables.")
                data = ds.to_dataframe().reset_index()
        else:
            data = ds.to_dataframe().reset_index()

        df = pl.from_pandas(data)
        print(f"✅ Data converted to Polars DataFrame: {df.shape}")
        return df

    except FileNotFoundError:
        print("⚠️ File not found. Check the path.")
        return None
    except Exception as e:
        print("⚠️ Something went wrong while loading the NetCDF file.")
        print("Error:", e)
        return None
