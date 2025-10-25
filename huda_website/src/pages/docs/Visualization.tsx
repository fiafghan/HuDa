import React from 'react'
import DocsLayout from '../../layouts/DocsLayout'

export default function Visualization() {
  return (
    <DocsLayout title="Phase: Visualization">
      <p className="text-gray-700">Lightweight placeholder chart specs for common visuals. Each function returns a minimal spec dict. Rendering/export is left to frontend or a renderer. Data inputs accept CSV path, Pandas DataFrame, or Polars DataFrame.</p>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="bar-chart">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">bar_chart(data, category_col, value_col, orientation="vertical", stacked=False, color_col=None, title=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Categorical bar chart.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Compare categories.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Simple comparison, optionally stacked or colored.</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.visualize import bar_chart\nimport polars as pl\n\ndf = pl.DataFrame({\"province\":[\"A\",\"B\"], \"reached\":[1200,900]})\nspec = bar_chart(df, category_col=\"province\", value_col=\"reached\")`}</code></pre>
        </div>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="line-chart">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">line_chart(data, x_col, y_col, series_col=None, title=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Time/sequence line.</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.visualize import line_chart\nspec = line_chart(df, x_col=\"date\", y_col=\"value\", series_col=\"cluster\")`}</code></pre>
        </div>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="pie-chart">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">pie_chart(data, category_col, value_col, title=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Part-to-whole distribution.</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.visualize import pie_chart\nspec = pie_chart(df, category_col=\"cluster\", value_col=\"funding\")`}</code></pre>
        </div>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="histogram">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">histogram(data, value_col, bins=10, title=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Distribution of a numeric variable.</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.visualize import histogram\nspec = histogram(df, value_col=\"fcs\", bins=20)`}</code></pre>
        </div>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="box-plot">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">box_plot(data, category_col, value_col, title=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Spread across categories.</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.visualize import box_plot\nspec = box_plot(df, category_col=\"province\", value_col=\"fcs\")`}</code></pre>
        </div>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="stacked-bar">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">stacked_bar_chart(data, category_col, value_col, stack_col, title=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Stacked composition per category.</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.visualize import stacked_bar_chart\nspec = stacked_bar_chart(df, category_col=\"province\", value_col=\"value\", stack_col=\"cluster\")`}</code></pre>
        </div>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="multi-line">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">multi_series_line_chart(data, x_col, y_col, series_col, title=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Multiple lines by series.</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.visualize import multi_series_line_chart\nspec = multi_series_line_chart(df, x_col=\"date\", y_col=\"value\", series_col=\"cluster\")`}</code></pre>
        </div>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="heatmap">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">heatmap(data, x_col, y_col, value_col, title=None, scale="sequential")</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Correlation or intensity matrix.</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.visualize import heatmap\nspec = heatmap(df, x_col=\"province\", y_col=\"indicator\", value_col=\"score\")`}</code></pre>
        </div>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="bubble">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">bubble_chart(data, x_col, y_col, size_col, color_col=None, title=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Scatter with size and color.</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.visualize import bubble_chart\nspec = bubble_chart(df, x_col="needs", y_col="funding", size_col="population", color_col="cluster")`}</code></pre>
        </div>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="sankey">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">sankey_diagram(source_col, target_col, value_col, title=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Flow of aid/resources.</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.visualize import sankey_diagram
spec = sankey_diagram(source_col="donor", target_col="cluster", value_col="amount")`}</code></pre>
        </div>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="treemap">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">treemap(category_col, value_col, group_col=None, title=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Sector allocations.</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.visualize import treemap\nspec = treemap(category_col=\"sector\", value_col=\"amount\", group_col=\"province\")`}</code></pre>
        </div>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="radar">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">radar_chart(axis_cols, series_col=None, title=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Multi-sector needs profile.</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.visualize import radar_chart\nspec = radar_chart(axis_cols=[\"fcs\",\"rcsi\",\"wash\",\"health\"])`}</code></pre>
        </div>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="dashboard">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">interactive_dashboard(widgets=None, charts=None, layout="grid", title=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Combine charts and filters.</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.visualize import interactive_dashboard, bar_chart\nwidgets = [{\"type\":\"select\",\"field\":\"province\"}]\ncharts = [bar_chart(df, \"province\",\"reached\")]\nspec = interactive_dashboard(widgets=widgets, charts=charts)`}</code></pre>
        </div>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="time-slider">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">time_slider(time_col, title=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Interactive time control.</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.visualize import time_slider\nspec = time_slider(time_col=\"date\")`}</code></pre>
        </div>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="animated-crisis-map">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">animated_crisis_map(geojson_col, time_col, value_col, title=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Animated map over time.</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.visualize import animated_crisis_map\nspec = animated_crisis_map(geojson_col=\"geom\", time_col=\"date\", value_col=\"incidents\")`}</code></pre>
        </div>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="compare-countries">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">compare_countries(country_col, metric_cols, title=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Compare multiple countries.</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.visualize import compare_countries\nspec = compare_countries(country_col=\"country\", metric_cols=[\"needs\",\"funding\"])`}</code></pre>
        </div>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="funding-vs-needs">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">plot_funding_vs_needs(funding_col, needs_col, group_col=None, title=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Compare funding to needs.</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.visualize import plot_funding_vs_needs\nspec = plot_funding_vs_needs(funding_col=\"funding\", needs_col=\"needs\", group_col=\"province\")`}</code></pre>
        </div>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="targeted-vs-reached">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">plot_targeted_vs_reached(targeted_col, reached_col, group_col=None, title=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Target vs actual reached.</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.visualize import plot_targeted_vs_reached\nspec = plot_targeted_vs_reached(targeted_col=\"target\", reached_col=\"reached\", group_col=\"cluster\")`}</code></pre>
        </div>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="gaps-colored">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">show_gaps_colored(need_col, reached_col, color_scheme="red-yellow-green", title=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Color-coded gaps.</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.visualize import show_gaps_colored\nspec = show_gaps_colored(need_col=\"needs\", reached_col=\"reached\")`}</code></pre>
        </div>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="export-plots">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">export_plots(chart_spec, formats=["png"], filename_base="chart")</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Export chart spec (placeholder).</p>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.visualize import export_plots, bar_chart\nspec = bar_chart(df, category_col=\"province\", value_col=\"reached\")\nexport = export_plots(spec, formats=[\"png\",\"svg\",\"pdf\"], filename_base=\"my_chart\")`}</code></pre>
        </div>
      </section>
    </DocsLayout>
  )
}
