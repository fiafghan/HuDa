from huda.validation_and_quality import targeted_vs_reached_inconsistency_detection 
import polars as pl

df = pl.DataFrame({
    "province": ["Kabul", "Herat", "Balkh"],
    "targeted": [1000, 800, 600],
    "reached": [1200, 700, 600],
})

print (df)

flagged = targeted_vs_reached_inconsistency_detection(
    df,
    reached_cols=["reached"],
    targeted_cols=["targeted"],

    )

print (flagged)


