import polars as pl
import pycountry

def country_standardization(df, column, output="iso3"):
    """
    🌍 Standardize country names or codes to a unified format (ISO-2 or ISO-3).

    Supported Outputs:
    -------------------
        - "iso3" → Standard 3-letter country code (e.g., "AFG", "USA", "DEU")
        - "iso2" → 2-letter code (e.g., "AF", "US", "DE")
        - "name" → Full official English country name (e.g., "Afghanistan", "United States")

    Example Usage:
    -------------------
        import polars as pl
        from huda.standardize_country import standardize_country

        df = pl.DataFrame({
            "country": ["Afghanistan", "AF", "afg", "United States", "us"]
        })

        df_clean = standardize_country(df, "country", output="iso3")

    Output:
    -------------------
        ┌────────────┐
        │ country    │
        │ ---        │
        │ str        │
        ╞════════════╡
        │ AFG        │
        │ AFG        │
        │ AFG        │
        │ USA        │
        │ USA        │
        └────────────┘

    When & Why:
    -------------------
        ✅ **When:**
            - When your dataset has inconsistent country names or codes.
            - When you merge datasets from multiple sources (e.g., UN, WHO, OCHA).

        🌍 **Why:**
            - Standardized country codes prevent mismatches during joins or grouping.
            - ISO codes are recognized worldwide for analytics, dashboards, and maps.
            - Makes it easier to connect your data with global references (like population, HDI, etc.)

    """

    def get_standard_country(value):
        if not value:
            return None
        value = str(value).strip().title()
        try:
            # Try direct name match
            country = pycountry.countries.get(name=value)
            if not country:
                # Try alpha-2 or alpha-3 code lookup
                country = pycountry.countries.get(alpha_2=value.upper()) or pycountry.countries.get(alpha_3=value.upper())

            if not country:
                # Try common_name or official_name fallback
                for c in pycountry.countries:
                    if value.lower() in [getattr(c, "name", "").lower(),
                                         getattr(c, "official_name", "").lower(),
                                         getattr(c, "common_name", "").lower()]:
                        country = c
                        break

            if not country:
                return None  # Unknown country

            if output == "iso3":
                return country.alpha_3
            elif output == "iso2":
                return country.alpha_2
            elif output == "name":
                return country.name
            else:
                return None
        except Exception:
            return None

    try:
        df_clean = df.with_columns(
            pl.col(column).map_elements(get_standard_country, return_dtype=pl.String).alias(column)
        )
        print(f"✅ Country column '{column}' standardized to '{output}' format.")
        return df_clean

    except Exception as e:
        print("⚠️ Error while standardizing country names:", e)
        return df
