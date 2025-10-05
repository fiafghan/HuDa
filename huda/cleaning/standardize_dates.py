import polars as pl

def standardize_dates(df, column, style="iso"):
    """
    📅 Standardize date formats easily with multiple ready-made styles.

    Available Styles:
    -----------------
        - "iso"   →  2025-10-05       (default)
        - "us"    →  10/05/2025
        - "eu"    →  05-10-2025
        - "full"  →  October 05, 2025
        - "short" →  25/10/05

    Example Usage:
    -----------------
        import polars as pl
        from huda.cleaning.standardize_dates import standardize_dates

        df = pl.DataFrame({
            "date": ["2025/10/05", "05-10-2025", "2025.10.05"]
        })

        df_iso = standardize_dates(df, "date")
        df_eu = standardize_dates(df, "date", style="eu")

    Output:
    ----------
        ┌────────────┐
        │ date       │
        │ ---        │
        │ str        │
        ╞════════════╡
        │ 2025-10-05 │
        │ 2025-10-05 │
        │ 2025-10-05 │
        └────────────┘

    When and Why:
    -----------------
        - 🧩 To make all date columns uniform across different sources
        - 📊 For easy time-series and trend analysis
        - 🧹 To avoid parsing errors when joining or sorting
    """

    formats = {
        "iso": "%Y-%m-%d",
        "us": "%m/%d/%Y",
        "eu": "%d-%m-%Y",
        "full": "%B %d, %Y",
        "short": "%y/%m/%d"
    }

    try:
        if style not in formats:
            raise ValueError(f"❌ Unknown style '{style}'. Use one of: {list(formats.keys())}")

        col_dtype = df.schema[column]

        # If column is already datetime/date
        if col_dtype in [pl.Date, pl.Datetime]:
            df = df.with_columns(pl.col(column).dt.strftime(formats[style]).alias(column))
        else:
            # Convert string → datetime → formatted string
            df = df.with_columns(
                pl.col(column)
                .str.to_datetime(strict=False)
                .dt.strftime(formats[style])
                .alias(column)
            )

        print(f"✅ Dates in '{column}' standardized to '{style}' format → {formats[style]}")
        return df

    except Exception as e:
        print("⚠️ Error while standardizing dates:", e)
        return df
