import React from 'react'
import DocsLayout from '../../layouts/DocsLayout'

export default function Interoperability() {
  return (
    <DocsLayout title="Phase: Interoperability">
      <p className="text-gray-700">Export and sharing interfaces. Each function returns a lightweight intent spec; no files are written. Use these specs with your renderer/uploader. Every card includes What/When/Why/Parameters, a Python example, and the returned Output preview.</p>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="export-csv">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">export_csv(data, path, include_header=True, delimiter=",", encoding="utf-8")</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Prepare a CSV export intent.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Sharing tabular data across tools.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Universal, simple format.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.Interoperability import export_csv
import polars as pl

df = pl.DataFrame({"a":[1,2], "b":["x","y"]})
spec = export_csv(df, path="/tmp/data.csv")
print(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{
  "type": "export_csv",
  "path": "/tmp/data.csv",
  "options": {"include_header": true, "delimiter": ",", "encoding": "utf-8"},
  "preview": {"rows": 2, "columns": ["a", "b"]}
}`}</code></pre>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="export-excel">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">export_excel(data, path, sheet_name="Sheet1", include_header=True)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Prepare an Excel export intent.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Analysts using Excel workflows.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Multi-sheet, formatting-friendly.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.Interoperability import export_excel
spec = export_excel(df, path="/tmp/data.xlsx", sheet_name="Summary")
print(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{
  "type": "export_excel",
  "path": "/tmp/data.xlsx",
  "options": {"sheet_name": "Summary", "include_header": true},
  "preview": {"rows": 2, "columns": ["a", "b"]}
}`}</code></pre>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="export-json">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">export_json(data, path, orient="records", indent=2)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Prepare a JSON export intent.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> APIs, web apps, pipelines.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Flexible and widely supported.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.Interoperability import export_json
spec = export_json(df, path="/tmp/data.json", orient="records", indent=2)
print(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{
  "type": "export_json",
  "path": "/tmp/data.json",
  "options": {"orient": "records", "indent": 2},
  "preview": {"rows": 2, "columns": ["a", "b"]}
}`}</code></pre>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="export-parquet">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">export_parquet(data, path, compression="snappy")</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Prepare a Parquet export intent.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Columnar analytics and storage.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Efficient and typed.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.Interoperability import export_parquet
spec = export_parquet(df, path="/tmp/data.parquet", compression="snappy")
print(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{
  "type": "export_parquet",
  "path": "/tmp/data.parquet",
  "options": {"compression": "snappy"},
  "preview": {"rows": 2, "columns": ["a", "b"]}
}`}</code></pre>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="export-sql">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">export_sql_database(data, connection_uri, table_name, if_exists="replace")</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Prepare a SQL export intent.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Data marts, dashboards, integration.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Centralize and query at scale.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.Interoperability import export_sql_database\nspec = export_sql_database(df, connection_uri=\"postgresql://user:pass@host:5432/db\", table_name=\"huda_export\", if_exists=\"replace\")\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"export_sql\",\n  \"connection_uri\": \"postgresql://user:pass@host:5432/db\",\n  \"table_name\": \"huda_export\",\n  \"options\": {\"if_exists\": \"replace\"},\n  \"preview\": {\"rows\": 2, \"columns\": [\"a\", \"b\"]}\n}`}</code></pre>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="export-stata-spss">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">export_stata(data, path, version=118) | export_spss(data, path)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Prepare Stata/SPSS export intents.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Household microdata analysis.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Compatibility with statistical tools.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.Interoperability import export_stata, export_spss\nspec1 = export_stata(df, path=\"/tmp/data.dta\", version=118)\nspec2 = export_spss(df, path=\"/tmp/data.sav\")\nprint(spec1) ; print(spec2)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"export_stata\",\n  \"path\": \"/tmp/data.dta\",\n  \"options\": {\"version\": 118},\n  \"preview\": {\"rows\": 2, \"columns\": [\"a\", \"b\"]}\n}\n{\n  \"type\": \"export_spss\",\n  \"path\": \"/tmp/data.sav\",\n  \"options\": {},\n  \"preview\": {\"rows\": 2, \"columns\": [\"a\", \"b\"]}\n}`}</code></pre>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="export-gis">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">export_shapefile(data, path, geometry_col="geometry", crs_epsg=4326) | export_geojson(data, path, geometry_col="geometry", crs_epsg=4326)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Prepare GIS export intents.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Sharing spatial datasets.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Integrate with GIS software.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.Interoperability import export_shapefile, export_geojson\nspec1 = export_shapefile(df, path=\"/tmp/data.shp\", geometry_col=\"geom\")\nspec2 = export_geojson(df, path=\"/tmp/data.geojson\", geometry_col=\"geom\")\nprint(spec1) ; print(spec2)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"export_shapefile\",\n  \"path\": \"/tmp/data.shp\",\n  \"options\": {\"geometry_col\": \"geom\", \"crs_epsg\": 4326},\n  \"preview\": {\"rows\": 2, \"columns\": [\"a\", \"b\"]}\n}\n{\n  \"type\": \"export_geojson\",\n  \"path\": \"/tmp/data.geojson\",\n  \"options\": {\"geometry_col\": \"geom\", \"crs_epsg\": 4326},\n  \"preview\": {\"rows\": 2, \"columns\": [\"a\", \"b\"]}\n}`}</code></pre>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="export-hdx">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">export_hdx_dataset(data, dataset_name, organization, license_name="cc-by", private=False)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Prepare HDX dataset upload intent.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Publishing on HDX.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Share humanitarian data widely.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.Interoperability import export_hdx_dataset\nspec = export_hdx_dataset(df, dataset_name=\"huda-afg\", organization=\"huda-org\")\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"export_hdx\",\n  \"dataset_name\": \"huda-afg\",\n  \"organization\": \"huda-org\",\n  \"options\": {\"license\": \"cc-by\", \"private\": false},\n  \"preview\": {\"rows\": 2, \"columns\": [\"a\", \"b\"]}\n}`}</code></pre>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="share-html">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">share_dashboard_html(dashboard_spec, path, embed_assets=True, title=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Prepare a static HTML dashboard export intent.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Offline sharing or hosting.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Zero dependencies for recipients.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.Interoperability import share_dashboard_html\nfrom huda.visualize import bar_chart, interactive_dashboard\ncharts = [bar_chart(df, \"a\",\"a\")]\ndashboard = interactive_dashboard(charts=charts)\nspec = share_dashboard_html(dashboard, path=\"/tmp/dashboard.html\", embed_assets=True)\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"share_dashboard_html\",\n  \"path\": \"/tmp/dashboard.html\",\n  \"title\": \"HuDa Dashboard\",\n  \"options\": {\"embed_assets\": true},\n  \"preview\": {\"charts\": 1, \"widgets\": 0}\n}`}</code></pre>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="api-integration">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">api_integration_output(endpoint_url, method="POST", headers=None, auth_type=None, auth_token_env=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Prepare an API call intent to push outputs.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Automating pipelines and syncs.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Integrate with external systems.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.Interoperability import api_integration_output\nspec = api_integration_output(\n    endpoint_url=\"https://api.example.org/upload\",\n    method=\"POST\",\n    headers={\"Content-Type\":\"application/json\"},\n    auth_type=\"Bearer\",\n    auth_token_env=\"API_TOKEN\"\n)\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"api_integration\",\n  \"endpoint_url\": \"https://api.example.org/upload\",\n  \"method\": \"POST\",\n  \"headers\": {\"Content-Type\":\"application/json\"},\n  \"auth\": {\"type\": \"Bearer\", \"token_env\": \"API_TOKEN\"},\n  \"preview\": {\"will_send_payload\": true}\n}`}</code></pre>
      </section>
    </DocsLayout>
  )
}
