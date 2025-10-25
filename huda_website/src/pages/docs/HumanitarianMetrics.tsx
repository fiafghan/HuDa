import React from 'react'
import DocsLayout from '../../layouts/DocsLayout'

export default function HumanitarianMetrics() {
  return (
    <DocsLayout title="Phase: Humanitarian Metrics">
      <p className="text-gray-700">Standard indicators for humanitarian reporting. Simple Afghan-focused examples. Each block has What, When, Why, Parameters, Example, Output.</p>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="pin">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">population_in_need_percentage(data, in_need_col, population_col, group_by=None, percent=True)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> % of people in need out of population.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Situation overview and severity by area.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Shows scale of need relative to population.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>in_need_col</code>: count in need.</li>
          <li><code>population_col</code>: total population.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.humanitarian_metrics.population_in_need_percentage import population_in_need_percentage\nimport polars as pl\n\ndf = pl.DataFrame({"in_need":[1000], "population":[5000]})\nprint(population_in_need_percentage(df, in_need_col="in_need", population_col="population"))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> <code>pin_pct_placeholder</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="targeted-reached">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">targeted_vs_reached_percentage(data, targeted_col, reached_col, group_by=None, percent=True)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> % reached of targeted.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Monitoring progress against targets.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Shows implementation performance.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>targeted_col</code>: planned target.</li>
          <li><code>reached_col</code>: actual reached.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.humanitarian_metrics.targeted_vs_reached_percentage import targeted_vs_reached_percentage\nprint(targeted_vs_reached_percentage(df, targeted_col="target", reached_col="reached"))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> <code>pct_reached_of_targeted_placeholder</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="coverage-ratio">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">coverage_ratio(data, reached_col, targeted_col, group_by=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Coverage as reached/targeted.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Monitoring and endline reports.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> How much of the target is covered.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>reached_col</code>: reached count.</li>
          <li><code>targeted_col</code>: targeted count.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.humanitarian_metrics.coverage_ratio import coverage_ratio\nprint(coverage_ratio(df, reached_col="reached", targeted_col="target"))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> <code>coverage_ratio_placeholder</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="children-affected">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">children_affected_percentage(data, children_affected_col, population_col, group_by=None, percent=True)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> % of children affected.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Protection and child-focused reporting.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Highlights child-specific needs.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>children_affected_col</code>: affected children.</li>
          <li><code>population_col</code>: population (or child population).</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.humanitarian_metrics.children_affected_percentage import children_affected_percentage\nprint(children_affected_percentage(df, children_affected_col="children_affected", population_col="population"))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> <code>pct_children_affected_placeholder</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="women-affected">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">women_affected_percentage(data, women_affected_col, population_col, group_by=None, percent=True)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> % of women affected.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Gender reporting.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Highlights women-specific needs.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>women_affected_col</code>: affected women.</li>
          <li><code>population_col</code>: population (or female population).</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.humanitarian_metrics.women_affected_percentage import women_affected_percentage\nprint(women_affected_percentage(df, women_affected_col="women_affected", population_col="population"))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> <code>pct_women_affected_placeholder</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="idps-refugees-affected">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">idps_refugees_affected_percentage(data, idps_col=None, refugees_col=None, population_col=None, total_affected_col=None, percent=True)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> % of IDPs/refugees affected.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Displacement-focused reporting.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Track vulnerability among displaced.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>idps_col</code>, <code>refugees_col</code>: counts.</li>
          <li><code>population_col</code> or <code>total_affected_col</code>: denominator.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.humanitarian_metrics.idps_refugees_affected_percentage import idps_refugees_affected_percentage\nprint(idps_refugees_affected_percentage(df, idps_col="idps", refugees_col="refugees", total_affected_col="affected"))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> <code>pct_idps_refugees_affected_placeholder</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="fcs">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">food_consumption_score(data, food_group_cols, weights=None, group_by=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Simple FCS-like score.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Household food security surveys.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Summarize dietary diversity and frequency.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>food_group_cols</code>: dict of food group - column of days.</li>
          <li><code>weights</code>: optional weights per group.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.humanitarian_metrics.food_consumption_score import food_consumption_score\ncols = {"cereals":"cereals_days","legumes":"legumes_days"}\nprint(food_consumption_score(df, food_group_cols=cols))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> <code>fcs_placeholder</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="rcsi">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">coping_strategy_index(data, strategy_cols, weights=None, group_by=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> rCSI-like coping index.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Food security and shocks assessments.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Show reliance on negative coping.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>strategy_cols</code>: dict of strategy - column.</li>
          <li><code>weights</code>: optional weights per strategy.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.humanitarian_metrics.coping_strategy_index import coping_strategy_index\ncols = {"borrow_food":"borrow_days","reduce_meals":"reduce_days"}\nprint(coping_strategy_index(df, strategy_cols=cols))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> <code>coping_index_placeholder</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="livelihood-coping">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">livelihood_coping_strategies(data, strategy_cols, group_by=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Sum of livelihood coping strategies.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Resilience and food security monitoring.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Track stress/crisis/emergency strategies.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>strategy_cols</code>: list of strategy columns.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.humanitarian_metrics.livelihood_coping_strategies import livelihood_coping_strategies\nprint(livelihood_coping_strategies(df, strategy_cols=["sell_assets","child_labor"]))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> <code>livelihood_coping_total_placeholder</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="wash-access">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">wash_access_indicators(data, improved_water_col=None, improved_sanitation_col=None, population_col=None, percent=True)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> % with access to improved water/sanitation.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> WASH assessments.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Basic service access tracking.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>improved_water_col</code>, <code>improved_sanitation_col</code>: counts.</li>
          <li><code>population_col</code>: denominator.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.humanitarian_metrics.wash_access_indicators import wash_access_indicators\nprint(wash_access_indicators(df, improved_water_col="water_access", improved_sanitation_col="san_access", population_col="population"))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> <code>pct_improved_water_placeholder</code>, <code>pct_improved_sanitation_placeholder</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="health-density">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">health_facility_density_per_10k(data, facility_count_col, population_col, group_by=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Facilities per 10,000 population.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Service availability comparisons.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Normalized by population.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>facility_count_col</code>: number of facilities.</li>
          <li><code>population_col</code>: population.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.humanitarian_metrics.health_facility_density_per_10k import health_facility_density_per_10k\nprint(health_facility_density_per_10k(df, facility_count_col="clinics", population_col="population"))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> <code>health_facilities_per_10k_placeholder</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="education-density">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">education_facility_density_per_10k(data, facility_count_col, population_col, group_by=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Schools per 10,000 population.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Education facility availability.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Normalized by population.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>facility_count_col</code>: number of schools.</li>
          <li><code>population_col</code>: population.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.humanitarian_metrics.education_facility_density_per_10k import education_facility_density_per_10k\nprint(education_facility_density_per_10k(df, facility_count_col="schools", population_col="population"))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> <code>education_facilities_per_10k_placeholder</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="malnutrition-rates">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">malnutrition_rates(data, gam_col=None, sam_col=None, mam_col=None, population_u5_col=None, percent=True)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> GAM, SAM, MAM rates among U5.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Nutrition monitoring.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Track malnutrition burden.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>gam_col</code>, <code>sam_col</code>, <code>mam_col</code>: case counts.</li>
          <li><code>population_u5_col</code>: U5 population.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.humanitarian_metrics.malnutrition_rates import malnutrition_rates\nprint(malnutrition_rates(df, gam_col="gam", sam_col="sam", mam_col="mam", population_u5_col="u5_pop"))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> <code>gam_rate_placeholder</code>, <code>sam_rate_placeholder</code>, <code>mam_rate_placeholder</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="cmr">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">crude_mortality_rate(data, deaths_col, population_col, period_days=None, per=10000)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> CMR per 10,000 (optionally period-normalized).</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Health/emergency comparisons.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Standardized severity indicator.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>deaths_col</code>: death counts.</li>
          <li><code>population_col</code>: population at risk.</li>
          <li><code>period_days</code>: optional period days.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.humanitarian_metrics.crude_mortality_rate import crude_mortality_rate\nprint(crude_mortality_rate(df, deaths_col="deaths", population_col="population", period_days=30))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> <code>cmr_placeholder</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="u5mr">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">under_five_mortality_rate(data, under5_deaths_col, population_u5_col, period_days=None, per=10000)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> U5MR per 10,000 (optionally period-normalized).</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Health/emergency comparisons.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Standardized child severity indicator.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>under5_deaths_col</code>: U5 death counts.</li>
          <li><code>population_u5_col</code>: U5 population.</li>
          <li><code>period_days</code>: optional period days.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.humanitarian_metrics.under_five_mortality_rate import under_five_mortality_rate\nprint(under_five_mortality_rate(df, under5_deaths_col="u5_deaths", population_u5_col="u5_pop", period_days=30))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> <code>u5mr_placeholder</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="conflict-incidents">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">conflict_incident_counts(data, incident_id_col=None, date_column=None, group_by=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Count security/conflict incidents.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Protection and access monitoring.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Track intensity and distribution.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>incident_id_col</code>: unique id (optional).</li>
          <li><code>group_by</code>: list of grouping columns.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.humanitarian_metrics.conflict_incident_counts import conflict_incident_counts\nprint(conflict_incident_counts(df, incident_id_col="incident_id"))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> <code>incident_count_placeholder</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="displaced-per-1000">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">people_displaced_per_1000(data, displaced_col, population_col, group_by=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Displaced per 1,000 population.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Displacement monitoring.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Normalized comparison across areas.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>displaced_col</code>: number displaced.</li>
          <li><code>population_col</code>: population.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.humanitarian_metrics.people_displaced_per_1000 import people_displaced_per_1000\nprint(people_displaced_per_1000(df, displaced_col="displaced", population_col="population"))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> <code>displaced_per_1000_placeholder</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="access-index">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">humanitarian_access_constraints_index(data, constraint_cols, weights=None, group_by=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Combined index of access constraints.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Access monitoring and planning.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Simple score to compare barriers.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>constraint_cols</code>: dict of constraint - column.</li>
          <li><code>weights</code>: optional weights.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.humanitarian_metrics.humanitarian_access_constraints_index import humanitarian_access_constraints_index\ncols = {"security":"sec_level","terrain":"mountainous"}\nprint(humanitarian_access_constraints_index(df, constraint_cols=cols))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> <code>access_constraints_index_placeholder</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="funding-ratio">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">funding_received_vs_requested(data, received_col, requested_col, group_by=None, percent=True)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Funding progress vs request.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Appeals and donor reporting.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Show gaps and progress.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>received_col</code>: amount received.</li>
          <li><code>requested_col</code>: amount requested.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.humanitarian_metrics.funding_received_vs_requested import funding_received_vs_requested\nprint(funding_received_vs_requested(df, received_col="received", requested_col="requested"))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> <code>pct_received_placeholder</code>, <code>funding_gap_placeholder</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="donor-tracking">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">donor_contribution_tracking(data, donor_col, amount_col, group_by=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Sum contributions by donor.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Financial tracking.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Monitor top donors and totals.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>donor_col</code>: donor name.</li>
          <li><code>amount_col</code>: amount value.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.humanitarian_metrics.donor_contribution_tracking import donor_contribution_tracking\nprint(donor_contribution_tracking(df, donor_col="donor", amount_col="amount"))`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> Same table with aggregation to be implemented later.</p>
      </section>
    </DocsLayout>
  )
}
