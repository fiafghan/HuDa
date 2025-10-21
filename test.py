import polars as pl
from huda.geospatial import display_refugee_camp_locations

# ساختن داده نمونه
df = pl.DataFrame({
    "latitude": [34.5, 34.35],
    "longitude": [69.2, 62.2],
    "camp_name": ["Kabul IDP Camp", "Herat Camp"],
})

# ساخت نقشه
m = display_refugee_camp_locations(df)

# ذخیره به فایل HTML
m.save("camps_afg.html")
