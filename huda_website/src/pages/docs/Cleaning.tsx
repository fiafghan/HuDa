import React from 'react'
import DocsLayout from '../../layouts/DocsLayout'

export default function Cleaning() {
  return (
    <DocsLayout title="Phase: Cleaning">
      <p className="text-gray-700">We clean the data. Very simple English. Short steps. Afghan survey examples. Each block shows: What, When, Why, Parameters, Example, Output.</p>

      {/* normalize_columns */}
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="normalize-columns">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>normalize_columns(df)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Make column names clean (lowercase, underscores, no symbols).</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Columns are messy like <em>"Country Name ", "Population(2025)"</em>.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Easy to use in code and merging.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Parameters</h3>
            <p className="text-sm text-gray-700">Only <code>df</code> (your table).</p>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.cleaning.normalize_columns import normalize_columns

import polars as pl
df = pl.DataFrame({
    "Country Name ": ["Afghanistan", "Syria"],
    "Population(2025)": [12345, 67890],
    "Food-Security": ["High", "Low"],
})

df_clean = normalize_columns(df)
print(df_clean)`}</code></pre>
          </div>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> New column names are simple, like <code>country_name</code>, <code>population2025</code>, <code>food_security</code>.</p>
      </section>

      {/* translate_categories */}
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="translate-categories">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>translate_categories(df, columns=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Make categories same (Yes/No, Male/Female, Active/Inactive) from multi-language forms (Dari/Pashto/English).</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Values are mixed like “بلی/Yes/Y/نخیر/No”.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Easy analysis and charts.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Parameters</h3>
            <ul className="text-sm text-gray-700 list-disc pl-6">
              <li><code>df</code>: your table</li>
              <li><code>columns</code>: None → all columns, or one column name, or a list of columns</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.cleaning.translate_categories import translate_categories

import polars as pl
df = pl.DataFrame({
    "response": ["Yes", "بلی", "نخیر", "Y", "N"],
    "gender": ["زن", "مرد", "Female", "Male", "F"],
})

df_clean = translate_categories(df, columns=["response", "gender"])
print(df_clean)`}</code></pre>
          </div>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> Clean text like <code>Yes/No</code>, <code>Male/Female</code>.</p>
      </section>

      {/* numbers_standardization */}
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="standardize-numbers">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>standardize_numbers(df, columns=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Turn messy numbers ("1,200", "۱٬۲۰۰", "3.5M", "2k") into real numbers.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Data from many sources/languages.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Correct sums/averages and plots.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Parameters</h3>
            <ul className="text-sm text-gray-700 list-disc pl-6">
              <li><code>columns</code>: None → all columns, or one column, or list of columns</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.cleaning.numbers_standardization import standardize_numbers

import polars as pl
df = pl.DataFrame({
    "price": ["1,200", "۱٬۵۰۰", "2.000,50", "N/A"],
    "population": ["2,345,000", "۳٬۴۵۶٬۷۸۹", "500k", "1.2 B"],
})

df_clean = standardize_numbers(df)
print(df_clean)`}</code></pre>
          </div>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> Floats like <code>1200.0</code>, <code>3456789.0</code>.</p>
      </section>

      {/* dates_standardization */}
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="standardize-dates">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>dates_standardization(df, column, style="iso|us|eu|full|short")</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Make date formats the same (like 2025-10-05).</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Your dates look different ("05-10-2025", "2025/10/05").</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Safe sorting, joining, and time series.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Parameters</h3>
            <ul className="text-sm text-gray-700 list-disc pl-6">
              <li><code>column</code>: which column has dates</li>
              <li><code>style</code>: one of <code>iso, us, eu, full, short</code></li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.cleaning.dates_standardization import dates_standardization

import polars as pl
df = pl.DataFrame({"date": ["2025/10/05", "05-10-2025", "2025.10.05"]})

print(dates_standardization(df, "date", style="iso"))
print(dates_standardization(df, "date", style="eu"))`}</code></pre>
          </div>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> Date strings in the format you pick.</p>
      </section>

      {/* drop_missing / duplicate */}
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="missing-duplicates">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>drop_missing(df, column=None) & duplicate(df, columns=None, keep="first|last|False")</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Remove empty rows; remove or keep duplicates.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold mb-2">Parameters</h3>
            <ul className="text-sm text-gray-700 list-disc pl-6">
              <li><code>drop_missing: column</code> (None = any null in row)</li>
              <li><code>duplicate: columns</code> (None = all), <code>keep</code> = first/last/False</li>
            </ul>
            <h3 className="text-sm font-semibold mt-4">When/Why</h3>
            <p className="text-sm text-gray-700">Clean table, avoid double counting.</p>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.cleaning.drop_missing import drop_missing
from huda.cleaning.duplicate import duplicate

import polars as pl
df = pl.DataFrame({"name": ["Ali", None, "Sara"], "year": [2025, 2025, 2025]})

df1 = drop_missing(df, column="name")
df2 = duplicate(df1, columns=["name","year"], keep="first")
print(df2)`}</code></pre>
          </div>
        </div>
      </section>

      {/* fill_* and forward/backward */}
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="fill-values">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>fill_mean/median/mode & forward_fill/backward_fill</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Fill missing values using simple rules.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Few gaps in numeric or text columns.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Parameters</h3>
            <ul className="text-sm text-gray-700 list-disc pl-6">
              <li><code>fill_mean/median/mode(df, column)</code></li>
              <li><code>forward_fill/backward_fill(df, column)</code> for time data</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.cleaning.fill_mean import fill_mean
from huda.cleaning.fill_median import fill_median
from huda.cleaning.fill_mode import fill_mode
from huda.cleaning.forward_fill import forward_fill
from huda.cleaning.backward_fill import backward_fill

import polars as pl
df = pl.DataFrame({"age": [20, None, 30], "temp": [20, None, 25]})

print(fill_mean(df, "age"))
print(fill_median(df, "age"))
print(fill_mode(pl.DataFrame({"city":["Kabul", None, "Kabul"]}), "city"))
print(forward_fill(df, "temp"))
print(backward_fill(df, "temp"))`}</code></pre>
          </div>
        </div>
      </section>

      {/* outlier_handler / outlier_isolation */}
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="outliers">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>outlier_handler(df, columns=None, method="iqr|zscore", factor=1.5) & outlier_isolation(df, columns=None, contamination=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Detect and remove extreme values.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Numbers look wrong (like 100 years old = 1000).</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Stop bad numbers from breaking stats.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Parameters</h3>
            <ul className="text-sm text-gray-700 list-disc pl-6">
              <li><code>outlier_handler</code>: <code>columns</code> (None/all), <code>method</code> (iqr|zscore), <code>factor</code> (1.5 default)</li>
              <li><code>outlier_isolation</code>: <code>columns</code> (None/all), <code>contamination</code> auto if None</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.cleaning.outlier_handler import outlier_handler
from huda.cleaning.outlier_isolation import outlier_isolation

import polars as pl
df = pl.DataFrame({"age": [20,22,19,100,21,23], "income":[3000,3200,3100,99999,3050,3150]})

print(outlier_handler(df))
print(outlier_isolation(df))`}</code></pre>
          </div>
        </div>
      </section>

      {/* combine_datasets / admin_boundaries / geocode */}
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="combine-admin-geocode">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>combine_datasets(df1, df2, on, how) — admin_boundaries(...) — geocode(df, location_col=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Merge tables, fix province/district spellings, find lat/lon for places.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Parameters</h3>
            <ul className="text-sm text-gray-700 list-disc pl-6">
              <li><code>combine_datasets</code>: <code>on</code> join key, <code>how</code> = inner|left|right|outer</li>
              <li><code>admin_boundaries</code>: <code>country_col</code>, <code>adm1_col</code>, <code>adm2_col</code>, <code>threshold</code></li>
              <li><code>geocode</code>: <code>location_col</code> (auto if None)</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.cleaning.combine_datasets import combine_datasets
from huda.cleaning.admin_boundaries import admin_boundaries
from huda.cleaning.geocode import geocode

import polars as pl
df1 = pl.DataFrame({"country":["Afghanistan","Syria"], "population":[39_000_000,18_000_000]})
df2 = pl.DataFrame({"country":["Afghanistan","Pakistan"], "gdp":[20.1,310.0]})
print(combine_datasets(df1, df2, on="country", how="outer"))

adm = pl.DataFrame({"country":["Afghanistan","Afganistan"], "province":["Kabul","Kabol"], "district":["Kabul","Kabool"]})
print(admin_boundaries(adm))

places = pl.DataFrame({"province":["Kabul","Herat"]})
print(geocode(places, location_col="province"))`}</code></pre>
          </div>
        </div>
      </section>
    </DocsLayout>
  )
}
