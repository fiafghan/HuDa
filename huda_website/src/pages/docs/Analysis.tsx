import React from 'react'
import DocsLayout from '../../layouts/DocsLayout'

export default function Analysis() {
  return (
    <DocsLayout title="Phase: Analysis">
      <p className="text-gray-700">We analyze the data for planning and decisions. Simple words. Afghan examples. Each block has What, When, Why, Parameters, Example, Output.</p>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="trend">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>time_series_trend_analysis(data, value_column, date_column="date", group_by=None, method="moving_average", window=3)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Smooth the line to see the real trend.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Monthly/weekly beneficiaries, cases.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Reduce noise, clearer decisions.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Parameters</h3>
            <ul className="text-sm text-gray-700 list-disc pl-6">
              <li><code>value_column</code>: numbers to smooth (e.g., <code>"beneficiaries"</code>).</li>
              <li><code>date_column</code>: date as text <code>YYYY-MM-DD</code>.</li>
              <li><code>group_by</code>: optional grouping (e.g., <code>["province"]</code>).</li>
              <li><code>method</code>: <code>"moving_average"</code>.</li>
              <li><code>window</code>: number of periods to average.</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.analysis.time_series_trend_analysis import time_series_trend_analysis
import polars as pl

df = pl.DataFrame({"date":["2024-01-01","2024-02-01","2024-03-01"], "beneficiaries":[100,150,200]})
print(time_series_trend_analysis(df, value_column="beneficiaries", window=2))`}</code></pre>
          </div>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> New column like <code>beneficiaries_trend_ma2</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="forecast">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>forecasting_needs(data, value_column, date_column="date", model="arima", forecast_periods=3)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Predict future months.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Planning proposals and allocations.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Prepare resources early.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>value_column</code>: values to forecast.</li>
          <li><code>model</code>: <code>"arima"</code> or <code>"prophet"</code>-style.</li>
          <li><code>forecast_periods</code>: months ahead.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.analysis.forecasting_needs import forecasting_needs
print(forecasting_needs(df, value_column="beneficiaries", forecast_periods=6))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> Adds a <code>forecast_model</code> column (placeholder).</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="correlation">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>correlation_analysis(data, columns, method="pearson")</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> How indicators move together.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Exploring relationships.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Find strong links to focus.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>columns</code>: numeric columns to compare.</li>
          <li><code>method</code>: <code>pearson</code> or <code>spearman</code>.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.analysis.correlation_analysis import correlation_analysis
print(correlation_analysis(df, columns=["in_need","funded"]))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> Correlation matrix (placeholder).</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="regression">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>regression_models(data, y, X, kind="linear|logistic", add_intercept=True)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Fit simple linear/logistic relationships.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Measure effect size of drivers.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Evidence-based planning.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>y</code>: dependent variable (0/1 for logistic).</li>
          <li><code>X</code>: list of predictors.</li>
          <li><code>kind</code>: <code>linear</code> or <code>logistic</code>.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.analysis.regression_models import regression_models
print(regression_models(df, y="reached", X=["in_need","funding"], kind="linear"))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> Placeholder dict of model inputs.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="clusters">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>cluster_analysis_regions(data, feature_columns, n_clusters=5, region_col=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Group similar provinces/districts.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Targeting strategies and typologies.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Simplify complex data.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>feature_columns</code>: numeric columns to cluster.</li>
          <li><code>n_clusters</code>: number of groups (k).</li>
          <li><code>region_col</code>: optional region name column.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.analysis.cluster_analysis_regions import cluster_analysis_regions
print(cluster_analysis_regions(df, feature_columns=["need","access"], n_clusters=4, region_col="province"))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> Adds <code>cluster</code> label (placeholder).</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="pca">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>pca_dimensionality_reduction(data, feature_columns, n_components=2)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Reduce many indicators to a few components.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Before clustering, mapping, dashboards.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Easier to visualize and understand.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>feature_columns</code>: numeric indicators.</li>
          <li><code>n_components</code>: number of components (2 by default).</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.analysis.pca_dimensionality_reduction import pca_dimensionality_reduction
print(pca_dimensionality_reduction(df, feature_columns=["need","coverage"], n_components=2))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> Adds <code>pc1</code>, <code>pc2</code> (placeholders).</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="inequality">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>inequality_measures(data, value_column, group_by=None, measures=["gini","theil"])</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Measure inequality across groups.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Equity analysis by province, district, group.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Find disparities to address.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>value_column</code>: numeric values to analyze.</li>
          <li><code>group_by</code>: optional groups (e.g., <code>["province"]</code>).</li>
          <li><code>measures</code>: <code>gini</code>, <code>theil</code>.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.analysis.inequality_measures import inequality_measures
print(inequality_measures(df, value_column="coverage", group_by=["province"]))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> Table of measures (placeholders).</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="impact">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>impact_analysis(data, outcome_col, treatment_col, covariates=None, method="diff_in_diff")</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Estimate intervention effects.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Program evaluation.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Know what worked.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>outcome_col</code>: result variable (e.g., income).</li>
          <li><code>treatment_col</code>: treated vs control flag.</li>
          <li><code>covariates</code>: optional adjustment columns.</li>
          <li><code>method</code>: estimation approach (default <code>diff_in_diff</code>).</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.analysis.impact_analysis import impact_analysis
print(impact_analysis(df, outcome_col="income", treatment_col="program"))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> Effect estimate (placeholder).</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="coverage-gap">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>coverage_gap_analysis(data, needs_columns, reached_columns, group_by=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Compare needs vs reached.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Monitoring and dashboards.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> See where assistance is low.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>needs_columns</code>: list of needs indicators.</li>
          <li><code>reached_columns</code>: matching reached indicators.</li>
          <li><code>group_by</code>: optional groups (province, etc.).</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.analysis.coverage_gap_analysis import coverage_gap_analysis
print(coverage_gap_analysis(df, ["need"],["reached"], group_by=["province"]))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> Coverage % and gap (placeholders).</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="needs-funding-gap">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>needs_vs_funding_gap_analysis(data, needs_col, funding_col, group_by=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Compare needs and funding.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Allocation and advocacy.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Show funding gaps.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>needs_col</code>: total needs value.</li>
          <li><code>funding_col</code>: funding amount.</li>
          <li><code>group_by</code>: optional grouping.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.analysis.needs_vs_funding_gap_analysis import needs_vs_funding_gap_analysis
print(needs_vs_funding_gap_analysis(df, needs_col="need", funding_col="funding"))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> Gap metric (placeholder).</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="seasonality">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>seasonality_detection(data, value_column, date_column="date", group_by=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Find repeating seasonal patterns.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> At least 12 months of data.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Plan by season.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>value_column</code>: values to analyze.</li>
          <li><code>group_by</code>: optional per-province analysis.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.analysis.seasonality_detection import seasonality_detection
print(seasonality_detection(df, value_column="beneficiaries"))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> Seasonality flag/summary (placeholder).</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="anomaly">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>anomaly_detection(data, value_column, date_column="date", group_by=None, method="zscore", threshold=3.0)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Detect unusual spikes or drops.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Monitoring dashboards.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Early warning and QC.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>method</code>: detection method (e.g., <code>zscore</code>).</li>
          <li><code>threshold</code>: sensitivity value (higher = fewer alerts).</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.analysis.anomaly_detection import anomaly_detection
print(anomaly_detection(df, value_column="beneficiaries"))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> <code>is_anomaly_placeholder</code> flag.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="displacement">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>predicting_displacement_flows(data, source_cols=None, target_cols=None, features=None, horizon_periods=3)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Predict future movement between locations.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Anticipate new arrivals.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Better preparedness.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>source_cols</code>/<code>target_cols</code>: from-to fields.</li>
          <li><code>features</code>: drivers like conflict index.</li>
          <li><code>horizon_periods</code>: steps ahead.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.analysis.predicting_displacement_flows import predicting_displacement_flows
print(predicting_displacement_flows(df, horizon_periods=3))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> Adds <code>pred_horizon_placeholder</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="mortality">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>mortality_morbidity_analysis(data, death_col=None, illness_col=None, population_col=None, per=10000)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Compute death/illness rates per population.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Health monitoring.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Comparable indicators.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>death_col</code>/<code>illness_col</code>: counts columns.</li>
          <li><code>population_col</code>: denominator.</li>
          <li><code>per</code>: per N people (e.g., 10,000).</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.analysis.mortality_morbidity_analysis import mortality_morbidity_analysis
print(mortality_morbidity_analysis(df, death_col="deaths", illness_col="cases", population_col="population"))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> Rate columns (placeholders).</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="food-security">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>food_security_phase_classification(data, indicator_columns, scheme="IPC-like")</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Assign simple phases based on indicators.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Food security assessments.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Communicate complexity simply.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>indicator_columns</code>: columns used for phase.</li>
          <li><code>scheme</code>: classification scheme name.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.analysis.food_security_phase_classification import food_security_phase_classification
print(food_security_phase_classification(df, indicator_columns=["rCSI","FCS"]))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> Adds <code>food_security_phase_placeholder</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="shelter">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>shelter_adequacy_analysis(data, condition_col, occupancy_col=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Assess shelter condition and overcrowding.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Shelter needs assessments.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Identify inadequate housing.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>condition_col</code>: quality of shelter.</li>
          <li><code>occupancy_col</code>: persons per room (optional).</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.analysis.shelter_adequacy_analysis import shelter_adequacy_analysis
print(shelter_adequacy_analysis(df, condition_col="shelter_condition", occupancy_col="ppr"))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> <code>shelter_adequacy_score_placeholder</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="health-access">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>health_facility_accessibility_analysis(data, travel_time_col=None, distance_col=None, thresholds_minutes=60)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Access by time/distance to facility.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Health access studies.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Find underserved areas.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>travel_time_col</code>/<code>distance_col</code>: access measures.</li>
          <li><code>thresholds_minutes</code>: acceptable time threshold.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.analysis.health_facility_accessibility_analysis import health_facility_accessibility_analysis
print(health_facility_accessibility_analysis(df, travel_time_col="time_to_facility"))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> <code>has_acceptable_access_placeholder</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="education">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>education_access_analysis(data, enrollment_col=None, attendance_col=None, population_school_age_col=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Enrollment/attendance vs school-age population.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Education monitoring.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Find gaps for children.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>enrollment_col</code>/<code>attendance_col</code>: counts.</li>
          <li><code>population_school_age_col</code>: denominator.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.analysis.education_access_analysis import education_access_analysis
print(education_access_analysis(df, enrollment_col="enrolled", attendance_col="attended", population_school_age_col="school_age"))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> Enrollment/attendance rates (placeholders).</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="livelihoods">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>livelihood_resilience_analysis(data, asset_columns=None, shock_columns=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Summarize resilience from assets and shocks.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Early recovery and resilience programming.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Identify vulnerable households/areas.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>asset_columns</code>: list of asset indicators.</li>
          <li><code>shock_columns</code>: list of shock indicators.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.analysis.livelihood_resilience_analysis import livelihood_resilience_analysis
print(livelihood_resilience_analysis(df, asset_columns=["owns_land","livestock"], shock_columns=["drought","flood"]))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> <code>resilience_score_placeholder</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="gender">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>gender_disaggregated_analysis(data, gender_col="gender", value_columns=None, group_by=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Compare indicators by gender.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Gender mainstreaming and reporting.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Ensure equitable assistance.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>gender_col</code>: column name with gender values.</li>
          <li><code>value_columns</code>: numeric columns to summarize.</li>
          <li><code>group_by</code>: additional grouping.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.analysis.gender_disaggregated_analysis import gender_disaggregated_analysis
print(gender_disaggregated_analysis(df, gender_col="gender", value_columns=["reached"], group_by=["province"]))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> Gender breakdown table (placeholder).</p>
      </section>
    </DocsLayout>
  )
}
