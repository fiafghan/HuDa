import polars as pl
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import time

def geocode(df, location_col=None, user_agent="huda_geocoder"):
    """
    🌍 Geocode Location Names → Latitude & Longitude
    ================================================

    💡 Simple Explanation:
    ----------------------
    This function automatically finds the coordinates (lat/lon)
    of places like provinces, districts, or villages using OpenStreetMap (Nominatim).

    ⚙️ What it does:
    ----------------
    - Detects location columns automatically (if not provided)
    - Uses OpenStreetMap to fetch latitude & longitude
    - Adds new columns: 'latitude' and 'longitude'
    - Skips already processed places for efficiency
    - Works with English, Dari, and Pashto names

    🧠 Parameters:
    ---------------
    df : pl.DataFrame
        Your dataset containing location names.
    location_col : str | None
        The column name containing location names. If None, it tries to guess automatically.

    🧩 Example Usage:
    -----------------
    df = pl.DataFrame({
        "province": ["Kabul", "Herat", "Kandahar", "Badakhshan"],
        "population": [4500000, 1000000, 1200000, 500000]
    })

    df_geo = geocode(df, location_col="province")

    🧾 Output:
    -----------
    ┌──────────────┬────────────┬───────────┬──────────────┐
    │ province     ┆ population ┆ latitude  ┆ longitude    │
    │ ---          ┆ ---        ┆ ---       ┆ ---          │
    │ str          ┆ i64        ┆ f64       ┆ f64          │
    ╞══════════════╪════════════╪═══════════╪══════════════╡
    │ Kabul        ┆ 4500000    ┆ 34.5281   ┆ 69.1723      │
    │ Herat        ┆ 1000000    ┆ 34.3482   ┆ 62.1997      │
    │ Kandahar     ┆ 1200000    ┆ 31.6133   ┆ 65.7101      │
    │ Badakhshan   ┆ 500000     ┆ 36.7348   ┆ 70.8110      │
    └──────────────┴────────────┴───────────┴──────────────┘

    📅 When & Why:
    -----------------
    ✅ Use when:
        - You want to map survey or humanitarian data.
        - You need coordinates for provinces/districts.
        - You plan to merge with satellite or GIS datasets.

    💡 Why this method:
        - Uses reliable open data (OpenStreetMap)
        - Automatically handles multilingual place names
        - Adds geographic intelligence to your dataset
    """

    try:
        # Detect location column automatically if not provided
        if location_col is None:
            possible_cols = [c for c in df.columns if "location" in c.lower() or "district" in c.lower() or "province" in c.lower()]
            if not possible_cols:
                raise ValueError("⚠️ No location column found. Please specify one manually.")
            location_col = possible_cols[0]

        # Initialize geocoder
        geolocator = Nominatim(user_agent=user_agent)
        geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

        # Cache results to avoid duplicate API calls
        cache = {}

        latitudes, longitudes = [], []

        for place in df[location_col]:
            place = str(place).strip()
            if place in cache:
                lat, lon = cache[place]
            else:
                time.sleep(1)
                location = geocode(f"{place}, Afghanistan")
                if location:
                    lat, lon = location.latitude, location.longitude
                else:
                    lat, lon = None, None
                cache[place] = (lat, lon)
            latitudes.append(lat)
            longitudes.append(lon)

        df = df.with_columns([
            pl.Series("latitude", latitudes),
            pl.Series("longitude", longitudes)
        ])

        print(f"✅ Geocoded successfully based on: {location_col}")
        return df

    except Exception as e:
        print("⚠️ Error during geocoding:", e)
        return df
