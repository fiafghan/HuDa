from pstats import Stats
from huda.validation_and_quality import generate_summary_statistics_per_dataset 
import polars as pl

df = pl.DataFrame({
    "province": ["Kabul", "Herat", "Balkh"],
    "targeted": [1000, 800, 600],
    "reached": [1200, 700, 600],
})

print (df)

Stats = generate_summary_statistics_per_dataset(
    df 

    )

print (Stats)


