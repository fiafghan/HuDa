from huda.validation_and_quality import humanatarian_index_validation_against_standards 
import polars as pl

df = pl.DataFrame({
        "province": ["Kabul", "Herat", "Balkh"],
        "water_liters_per_person_per_day": [12, 18, 10],
        "ipc_phase": [3, 6, 2],
        "coverage_percent": [95, 105, -2],
    })
violations_sphere = humanatarian_index_validation_against_standards(df, standards="sphere")
print(violations_sphere)

