import React from 'react'
import DocsLayout from '../../layouts/DocsLayout'

export default function Transformation() {
  return (
    <DocsLayout title="Phase: Transformation">
      <p className="text-gray-700">We change/reshape the data. Very simple English. Afghan examples.</p>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="pivot-unpivot">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>pivot_unpivot(data, index, columns, values, operation="pivot|unpivot")</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Change table shape: wide long.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> You have columns like <em>beneficiaries_jan, beneficiaries_feb</em> and want one "month" column, or the opposite.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Easier charts and analysis. Many tools prefer long format.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Parameters</h3>
            <ul className="text-sm text-gray-700 list-disc pl-6">
              <li><code>data</code>: CSV path, Pandas or Polars table.</li>
              <li><code>index</code>: id columns to keep (example: <code>["province"]</code>).</li>
              <li><code>columns</code>: only for pivot (example: <code>"month"</code>).</li>
              <li><code>values</code>: columns to pivot/unpivot (example: <code>["beneficiaries_jan","beneficiaries_feb"]</code>).</li>
              <li><code>operation</code>: <code>"pivot"</code> or <code>"unpivot"</code>.</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.transformation.pivot_unpivot import pivot_unpivot
import polars as pl

df = pl.DataFrame({
  "province": ["Kabul","Herat","Kandahar"],
  "beneficiaries_jan": [120,200,250],
  "beneficiaries_feb": [150,180,300],
})

long_df = pivot_unpivot(df, index=["province"], values=["beneficiaries_jan","beneficiaries_feb"], operation="unpivot")
print(long_df)`}</code></pre>
          </div>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> A Polars table in the new shape. For unpivot, you get columns like <code>variable</code> and <code>value</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="percentage">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>percentage_calculation(data, numerator_columns, denominator_column, suffix="_pct")</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Create percentage columns like <em>in_need_pct</em>.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> You have totals (population) and parts (people_in_need).</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Percent is easier to compare than raw counts across provinces.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Parameters</h3>
            <ul className="text-sm text-gray-700 list-disc pl-6">
              <li><code>data</code>: CSV or Polars table.</li>
              <li><code>numerator_columns</code>: list of columns (example: <code>["people_in_need"]</code>).</li>
              <li><code>denominator_column</code>: total column (example: <code>"population"</code>).</li>
              <li><code>suffix</code>: default <code>_pct</code>.</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.transformation.percentage_calculation import percentage_calculation
import polars as pl

df = pl.DataFrame({
  "province": ["Kabul","Herat","Kandahar"],
  "population": [4500000,1000000,1200000],
  "people_in_need": [900000,150000,200000],
})
print(percentage_calculation(df, ["people_in_need"], "population"))`}</code></pre>
          </div>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> Same table plus new columns like <code>people_in_need_pct</code> with percentages.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="per-pop">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>population_based_normalization(data, value_columns, population_column, per=1000)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Convert counts to per-<code>per</code> people (per 1,000 by default).</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Comparing provinces with different population sizes.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Fair comparisons (rates).</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.transformation.population_based_normalization import population_based_normalization
import polars as pl

df = pl.DataFrame({
  "province": ["Kabul","Herat","Kandahar"],
  "population": [4500000,1000000,1200000],
  "patients": [23000,5000,8000],
})
print(population_based_normalization(df, ["patients"], "population", per=1000))`}</code></pre>
        </div>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="time-series">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>average_rolling(...) & monthly_yearly_growth(...)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Smooth with moving average; compute month-over-month or year-over-year growth.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Time series of beneficiaries or cases.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> See trends clearly.</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.transformation.average_rolling import average_rolling
from huda.transformation.monthly_yearly_growth import monthly_yearly_growth
import polars as pl

df = pl.DataFrame({"date":["2024-01-01","2024-02-01","2024-03-01"], "beneficiaries":[100,150,200]})
print(average_rolling(df, value_columns=["beneficiaries"], window=2))
print(monthly_yearly_growth(df, value_column="beneficiaries", date_column="date", period="monthly"))`}</code></pre>
        </div>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="standardization">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>age_group_standardization(...) • gender_group_standardization(...) • categorical_code_to_label(...)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Make consistent age bins, gender labels, and code-to-label mapping.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Datasets have different age/gender/codes styles.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Clean categories for grouping and charts.</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.transformation.age_group_standardization import age_group_standardization
from huda.transformation.gender_group_standardization import gender_group_standardization
from huda.transformation.categorical_code_to_label import categorical_code_to_label
import polars as pl

df = pl.DataFrame({"age":[2,17,35,70], "gender":["M","F","Male","female"], "sector":[1,2,1,3]})
print(age_group_standardization(df, age_column="age"))
print(gender_group_standardization(df, gender_column="gender"))
print(categorical_code_to_label(df, code_column="sector", mapping={1:"Food",2:"Shelter",3:"Education"}))`}</code></pre>
        </div>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="indices">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>needs_coverage_calculation(...) • averages_weighted_population(...) • severity_index_calculation(...) • z_score_calculation(...)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Build coverage %, indices, and z-scores for anomalies.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> You need summarized indicators for reporting.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Clear decision-making and quality checks.</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.transformation.needs_coverage_calculation import needs_coverage_calculation
from huda.transformation.averages_weighted_population import averages_weighted_population
from huda.transformation.severity_index_calculation import severity_index_calculation
from huda.transformation.z_score_calculation import z_score_calculation
import polars as pl

df = pl.DataFrame({
  "population":[5_000_000,2_000_000],
  "food_needs":[1000,800], "food_provided":[800,500],
  "water_needs":[5000,4000], "water_provided":[4000,2500],
})
print(needs_coverage_calculation(df, ["food_needs","water_needs"], ["food_provided","water_provided"]))
print(z_score_calculation(df.with_columns(pl.col("food_needs").alias("amount")), column="amount"))`}</code></pre>
        </div>
      </section>
    </DocsLayout>
  )
}
