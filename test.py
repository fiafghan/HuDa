from huda.validation_and_quality import validate_humanitarian_indicators_against_standards 
import polars as pl

df = pl.DataFrame({
        "province": ["Kabul", "Herat", "Balkh"],
        "water_liters_per_person_per_day": [12, 18, 10],
        "ipc_phase": [3, 6, 2],
        "coverage_percent": [95, 105, -2],
    })
violations_sphere = validate_humanitarian_indicators_against_standards(df, standards="sphere")
violations_ipc = validate_humanitarian_indicators_against_standards(df, standards="ipc")
print(violations_sphere)
print(violations_ipc)

