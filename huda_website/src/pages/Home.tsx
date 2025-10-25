import React from 'react'
import Header from '../components/Header'
import Sidebar from '../components/Sidebar'
import Footer from '../components/Footer'
import { Link } from 'react-router-dom'
import CodeEnhancer from '../components/CodeEnhancer'

export default function Home() {
  return (
    <div className="mdp min-h-screen">
      <Header />
      <Sidebar />
      <div className="md:pl-72">
        <main className="max-w-7xl mx-auto px-4 md:px-6 py-8">
          <section id="overview" className="mb-8">
            <div className="relative overflow-hidden rounded-xl bg-gradient-to-r from-indigo-600 via-sky-600 to-emerald-600 p-[1px] shadow-md mb-4">
              <div className="rounded-[11px] bg-white/90 backdrop-blur-sm">
                <div className="px-5 md:px-7 py-6 md:py-8">
                  <h1 className="text-2xl md:text-3xl font-bold tracking-tight text-gray-900">HuDa Library</h1>
                  <p className="text-gray-700">Humanitarian data utilities — simple, fast, consistent.</p>
                </div>
              </div>
            </div>
            <div className="prose max-w-none">
              <h2 className="text-xl font-semibold mb-2">Overview</h2>
              <p className="text-gray-700">HuDa is a Python library to speed up humanitarian data analysis. It helps you open, clean, transform, validate, and visualize datasets with practical functions designed for field surveys, 5W, and monitoring data.</p>
              <ul className="list-disc pl-6 text-gray-700 mt-3 space-y-1">
                <li><span className="font-semibold">Consistent:</span> same design patterns across modules.</li>
                <li><span className="font-semibold">Fast:</span> leverages Polars/Pandas where needed.</li>
                <li><span className="font-semibold">Practical:</span> built on real humanitarian workflows.</li>
              </ul>
            </div>
          </section>

          <section id="installation" className="mb-8">
            <h2 className="text-xl font-semibold mb-2">Installation</h2>
            <div className="rounded-lg border border-amber-200 bg-amber-50 p-4 text-amber-800">
              <div className="flex items-center gap-2 font-medium">Under development</div>
              <p className="mt-2 text-sm">The installation guide will be provided later. Use the sections below to explore the docs.</p>
            </div>
          </section>

          <div className="grid gap-6">
            <section id="opening" className="content-section">
              <h3 className="text-lg font-semibold mb-1">Phase: Opening</h3>
              <p className="text-gray-700">Open files (CSV, Excel, JSON). Simple English. Afghan survey examples.</p>
              <Link to="/docs/opening" className="text-sm text-indigo-700 hover:text-indigo-900 underline">Open full Opening docs</Link>
            </section>

            <section id="cleaning" className="content-section">
              <h3 className="text-lg font-semibold mb-1">Phase: Cleaning</h3>
              <p className="text-gray-700">Standardize names, translate categories, fix numbers/dates, remove missing/duplicates, handle outliers, merge and geocode.</p>
              <Link to="/docs/cleaning" className="text-sm text-indigo-700 hover:text-indigo-900 underline">Open full Cleaning docs</Link>
            </section>

            <section id="transformation" className="content-section">
              <h3 className="text-lg font-semibold mb-1">Phase: Transformation</h3>
              <p className="text-gray-700">Aggregate, reshape, standardize, and compute indexes.</p>
              <Link to="/docs/transformation" className="text-sm text-indigo-700 hover:text-indigo-900 underline">Open full Transformation docs</Link>
            </section>

            <section id="validation" className="content-section">
              <h3 className="text-lg font-semibold mb-1">Phase: Validation & Quality</h3>
              <p className="text-gray-700">Validate columns, check ranges, enforce standards, and auto profile.</p>
              <Link to="/docs/validation-quality" className="text-sm text-indigo-700 hover:text-indigo-900 underline">Open full Validation & Quality docs</Link>
            </section>

            <section id="geospatial" className="content-section">
              <h3 className="text-lg font-semibold mb-1">Phase: Geospatial</h3>
              <p className="text-gray-700">Create maps and overlays using Folium and GeoJSON layers.</p>
              <Link to="/docs/geospatial" className="text-sm text-indigo-700 hover:text-indigo-900 underline">Open full Geospatial docs</Link>
            </section>

            <section id="analysis" className="content-section">
              <h3 className="text-lg font-semibold mb-1">Phase: Analysis</h3>
              <p className="text-gray-700">Time series, forecasting, and correlations. (content coming soon)</p>
              <Link to="/docs/analysis" className="text-sm text-indigo-700 hover:text-indigo-900 underline">Open full Analysis docs</Link>
            </section>

            <section id="visualization" className="content-section">
              <h3 className="text-lg font-semibold mb-1">Phase: Visualization</h3>
              <p className="text-gray-700">Bar/Line/Pie, Histograms, Box Plots, Stacked & Multi-series charts, Heatmaps, Bubble, Sankey, Treemaps, Radar, Dashboards, Time slider, Animated maps, and more.</p>
              <Link to="/docs/visualization" className="text-sm text-indigo-700 hover:text-indigo-900 underline">Open full Visualization docs</Link>
            </section>

            <section id="automation" className="content-section">
              <h3 className="text-lg font-semibold mb-1">Phase: Automation & Workflows</h3>
              <p className="text-gray-700">Monthly reports, snapshots, downloads, scheduled ETL, versioning, lineage, change detection, and templates.</p>
              <Link to="/docs/automation" className="text-sm text-indigo-700 hover:text-indigo-900 underline">Open full Automation & Workflows docs</Link>
            </section>

            <section id="interoperability" className="content-section">
              <h3 className="text-lg font-semibold mb-1">Phase: Interoperability</h3>
              <p className="text-gray-700">Export and share: CSV, Excel, JSON, Parquet, SQL, Stata/SPSS, GIS, HDX datasets, HTML dashboards, API integration.</p>
              <Link to="/docs/interoperability" className="text-sm text-indigo-700 hover:text-indigo-900 underline">Open full Interoperability docs</Link>
            </section>

            <section id="ml4humanitarian" className="content-section">
              <h3 className="text-lg font-semibold mb-1">Phase: ML for Humanitarian Data</h3>
              <p className="text-gray-700">Displacement, food insecurity, mortality, crisis severity, misinformation, funding, supply chain, survey anomalies, crisis text classification, and early warning.</p>
              <Link to="/docs/ml4humanitarian" className="text-sm text-indigo-700 hover:text-indigo-900 underline">Open full ML for Humanitarian Data docs</Link>
            </section>

            <section id="document-processing" className="content-section">
              <h3 className="text-lg font-semibold mb-1">Phase: Text & Document Processing</h3>
              <p className="text-gray-700">PDF/Word extraction, indicator extraction, NL dataset search, translation, NER, sentiment, needs classification, keywords, knowledge graphs.</p>
              <Link to="/docs/document-processing" className="text-sm text-indigo-700 hover:text-indigo-900 underline">Open full Text & Document Processing docs</Link>
            </section>

            <section id="humanitarian-metrics" className="content-section">
              <h3 className="text-lg font-semibold mb-1">Phase: Humanitarian-Specific Metrics</h3>
              <p className="text-gray-700">Standard indicators: PIN, coverage, FCS/rCSI, WASH access, facility densities, mortality, displacement, access, funding.</p>
              <Link to="/docs/humanitarian-metrics" className="text-sm text-indigo-700 hover:text-indigo-900 underline">Open full Humanitarian Metrics docs</Link>
            </section>
          </div>
        </main>
        <Footer />
        <CodeEnhancer />
      </div>
    </div>
  )
}
