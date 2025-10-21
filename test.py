import polars as pl
from huda.geospatial import cluster_humanitarian_facilities  # change name if your file name is different

# Sample data for testing
df = pl.DataFrame({
    "latitude": [34.5553, 34.556, 34.557, 34.3482, 36.7280],
    "longitude": [69.2075, 69.208, 69.209, 62.1997, 66.8960],
    "facility": ["Kabul Hospital A", "Kabul Hospital B", "Clinic C", "Herat School", "Balkh School"],
})

# Create the clustered map
m = cluster_humanitarian_facilities(df, name_col="facility")

# Save it as an HTML file
m.save("testdata/facilities_cluster_afg.html")

print("✅ Map generated successfully! Open 'facilities_cluster_afg.html' in your browser.")
