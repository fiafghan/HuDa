import React from 'react'
import DocsLayout from '../../layouts/DocsLayout'

export default function Validation() {
  return (
    <DocsLayout title="Phase: Validation & Quality">
      <p className="text-gray-700">We check the data. Very simple English. Afghan survey style. Colorful and copyable code.</p>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="country-code">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>country_code_validation(data, country_column, group_by_cols=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Check if country codes are valid ISO-2 (like AF, US).</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> You have a column with country codes in forms.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Avoid wrong codes before merging or reporting.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Parameters</h3>
            <ul className="text-sm text-gray-700 list-disc pl-6">
              <li><code>data</code>: CSV path, Pandas, or Polars table.</li>
              <li><code>country_column</code>: column with ISO-2 codes (example: <code>"country"</code>).</li>
              <li><code>group_by_cols</code>: optional list to count Valid/Invalid per group (example: <code>["province"]</code>).</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.validation_and_quality.country_code_validation import country_code_validation
import polars as pl

df = pl.DataFrame({"province":["Kabul","Herat"], "country":["AF","XX"]})
print(country_code_validation(df, country_column="country"))`}</code></pre>
          </div>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> Same table plus <code>valid_flag</code> (= Valid/Invalid). If grouped, a count table.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="date-range">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>date_range_validation(data, date_columns, group_by_cols=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Check dates are not before 1900 and not in the future.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Survey date fields look suspicious (e.g., 1800 or future).</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Prevent bad timelines in dashboards and joins.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Parameters</h3>
            <ul className="text-sm text-gray-700 list-disc pl-6">
              <li><code>data</code>: CSV path, Pandas, or Polars table.</li>
              <li><code>date_columns</code>: list of columns to validate (strings like <code>"YYYY-MM-DD"</code> are auto-parsed).</li>
              <li><code>group_by_cols</code>: optional list to count Valid/Invalid per group.</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.validation_and_quality.date_range_validation import date_range_validation
import polars as pl

df = pl.DataFrame({"survey_date":["2023-01-01","1800-01-01"]})
print(date_range_validation(df, date_columns=["survey_date"]))`}</code></pre>
          </div>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> Adds <code>{`{column}_valid_flag`}</code> for each date column; or grouped counts.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="mandatory">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>mandatory_fields_check(data, required_columns)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Check required columns are present and not empty.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Before merging or exporting datasets.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Avoid nulls or missing critical identifiers.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Parameters</h3>
            <ul className="text-sm text-gray-700 list-disc pl-6">
              <li><code>data</code>: CSV path, Pandas, or Polars table.</li>
              <li><code>required_columns</code>: list of must-have columns (example: <code>["hh_id","province"]</code>).</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.validation_and_quality.mandatory_fields_check import mandatory_fields_check
import polars as pl

df = pl.DataFrame({"hh_id":[1,2], "province":["Kabul", None]})
print(mandatory_fields_check(df, required_columns=["hh_id","province"]))`}</code></pre>
          </div>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> A result table or flags depending on module design (see function docstring).</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="negative-values">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>negative_values_detection_where_they_should_not_exist(data, columns)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Find negatives in columns that must be non-negative (e.g., age, counts).</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> After data collection or before aggregations.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Prevent wrong sums/averages from negative values.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Parameters</h3>
            <ul className="text-sm text-gray-700 list-disc pl-6">
              <li><code>data</code>: CSV path, Pandas, or Polars table.</li>
              <li><code>columns</code>: list of numeric columns that must be &gt;= 0.</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.validation_and_quality.negative_values_detection_where_they_should_not_exist import negative_values_detection_where_they_should_not_exist
import polars as pl

df = pl.DataFrame({"age":[25,-2,30]})
print(negative_values_detection_where_they_should_not_exist(df, columns=["age"]))`}</code></pre>
          </div>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> Flags or a filtered table of invalid rows (see function docstring).</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="targeted-reached">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>targeted_vs_reached_inconsistency_detection(data, targeted_col, reached_col)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Flag when reached &gt; targeted.</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.validation_and_quality.targeted_vs_reached_inconsistency_detection import targeted_vs_reached_inconsistency_detection
import polars as pl

df = pl.DataFrame({"targeted":[100,200], "reached":[150,180]})
print(targeted_vs_reached_inconsistency_detection(df, targeted_col="targeted", reached_col="reached"))`}</code></pre>
        </div>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="summary-profile">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>generate_summary_statistics_per_dataset(...) • automatic_data_profiling_report(...)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Quick stats of dataset. Auto data profiling report for QA.</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.validation_and_quality.generate_summary_statistics_per_dataset import generate_summary_statistics_per_dataset
from huda.validation_and_quality.automatic_data_profiling_report import automatic_data_profiling_report
import polars as pl

df = pl.DataFrame({"x":[1,2,3,4], "y":[10,20,30,40]})
print(generate_summary_statistics_per_dataset(df))
# profiling = automatic_data_profiling_report(df)  # returns a structure/report per module design`}</code></pre>
        </div>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="standards">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>humanatarian_index_validation_against_standards(data, ...)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Validate humanitarian indicators against standard thresholds.</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.validation_and_quality.humanatarian_index_validation_against_standards import humanatarian_index_validation_against_standards
# Example depends on your column names and thresholds; see module docstring.`}</code></pre>
        </div>
      </section>
    </DocsLayout>
  )
}
