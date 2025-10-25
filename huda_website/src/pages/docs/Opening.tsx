import React from 'react'
import DocsLayout from '../../layouts/DocsLayout'

export default function Opening() {
  return (
    <DocsLayout title="Phase: Opening">
      <p className="text-gray-700">Here you open files. Very simple English. Short steps. Afghan survey examples.</p>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>open_csv(file_path, initial_filters=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Open a CSV file into a table.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> You have .csv file (for example: survey results).</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Quick and safe. It finds the text encoding for you.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Parameters</h3>
            <ul className="text-sm text-gray-700 list-disc pl-6">
              <li><code>file_path</code>: path of the CSV. Example: <code>"data/afg_survey.csv"</code>.</li>
              <li><code>initial_filters</code>: filter rows at start. Example: <code>{'{'}"country":"Afghanistan", "year":2025{'}'}</code>.</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.opening.csv import open_csv

df = open_csv(
    "data/afg_survey.csv",
    initial_filters={"country": "Afghanistan", "year": 2025}
)
# df is a table you can use`}</code></pre>
          </div>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> A Polars table (DataFrame). It only keeps rows you asked for in <code>initial_filters</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>open_excel(file_path, initial_filters=None, sheet_name=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Open an Excel file into a table.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> You have .xlsx / .xls with one or more sheets.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Easy filters at start. No coding pain.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Parameters</h3>
            <ul className="text-sm text-gray-700 list-disc pl-6">
              <li><code>file_path</code>: path of the Excel. Example: <code>"data/afg_survey.xlsx"</code>.</li>
              <li><code>initial_filters</code>: filter rows at start. Example: <code>{'{'}"province":"Kabul"{'}'}</code>.</li>
              <li><code>sheet_name</code>: which sheet to read. Example: <code>"data"</code> or <code>0</code> for first sheet.</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.opening.excel import open_excel

df = open_excel(
    "data/afg_survey.xlsx",
    sheet_name="data",
    initial_filters={"province": "Kabul"}
)
# df is a table from the "data" sheet, only Kabul rows`}</code></pre>
          </div>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> A Polars table. If you pass filters, it keeps only those rows.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>open_json(file_path, initial_filters=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Open a JSON file. If it looks like a table, you get a table. If not, you get Python JSON.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> You have .json files from surveys or APIs.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Simple. Works for table JSON or nested JSON.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Parameters</h3>
            <ul className="text-sm text-gray-700 list-disc pl-6">
              <li><code>file_path</code>: path of the JSON. Example: <code>"data/afg_households.json"</code>.</li>
              <li><code>initial_filters</code>: if JSON became a table, filter rows at start. Example: <code>{'{'}"district":"Herat"{'}'}</code>.</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.opening.json import open_json

# Table-like JSON
df_or_data = open_json(
    "data/afg_households.json",
    initial_filters={"district": "Herat"}
)
# If it is a table, you get a Polars table filtered to Herat.
# If not a table, you get Python JSON data.`}</code></pre>
          </div>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> A Polars table (if table-like) or a Python JSON object (if not table-like).</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>open_geojson(file_path)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Open a GeoJSON map file.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> You have region boundaries or shapes (provinces, districts).</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> You get two things: a GeoPandas map (with geometry) and a Polars table (attributes only).</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Parameters</h3>
            <ul className="text-sm text-gray-700 list-disc pl-6">
              <li><code>file_path</code>: path of the GeoJSON. Example: <code>"data/afg_provinces.geojson"</code>.</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.opening.geojson import open_geojson

gdf, df = open_geojson("data/afg_provinces.geojson")
print(gdf.head())  # map with geometry
print(df.head())   # attributes table`}</code></pre>
          </div>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> (<code>gdf</code>) GeoPandas map + (<code>df</code>) Polars table without geometry.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>open_parquet(file_path, columns=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Open a Parquet file (fast columnar format).</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Your data team gives Parquet files (very common).</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Very fast. You can load only some columns.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Parameters</h3>
            <ul className="text-sm text-gray-700 list-disc pl-6">
              <li><code>file_path</code>: path of the Parquet. Example: <code>"data/humanitarian.parquet"</code>.</li>
              <li><code>columns</code>: list of columns to keep. Example: <code>["province","population"]</code>.</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.opening.parquet import open_parquet

df_all = open_parquet("data/humanitarian.parquet")
df_some = open_parquet("data/humanitarian.parquet", columns=["province","population"])`}</code></pre>
          </div>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> A Polars table with all or selected columns.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>open_sqlite(db_path, table_name)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Read data from a SQLite database file.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> You have a small .db file from a colleague.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Simple and local. No server needed.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Parameters</h3>
            <ul className="text-sm text-gray-700 list-disc pl-6">
              <li><code>db_path</code>: path to the .db file. Example: <code>"data/afg.db"</code>.</li>
              <li><code>table_name</code>: name of the table. Example: <code>"needs_table"</code>.</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.opening.sqlite import open_sqlite

df = open_sqlite("data/afg.db", "needs_table")
print(df)`}</code></pre>
          </div>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> A Polars table with all rows from the table.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>open_postgres(host, port, user, password, database, table_name)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Read data from a PostgreSQL server.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Your IT provides a Postgres database.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Common in organizations, stable and reliable.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Parameters</h3>
            <ul className="text-sm text-gray-700 list-disc pl-6">
              <li><code>host, port, user, password, database</code>: connection details. Example: <code>("localhost", 5432, ...)</code>.</li>
              <li><code>table_name</code>: table to read. Example: <code>"needs_table"</code>.</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.opening.postgres import open_postgres

df = open_postgres(
    host="localhost", port=5432,
    user="postgres", password="1234", database="humanitarian_db",
    table_name="needs_table"
)
print(df)`}</code></pre>
          </div>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> A Polars table with rows from the table.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>open_mysql(host, port, user, password, database, table_name)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Read data from a MySQL server.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Your systems use MySQL/MariaDB.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Widely used and supported.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Parameters</h3>
            <ul className="text-sm text-gray-700 list-disc pl-6">
              <li><code>host, port, user, password, database</code>: connection details.</li>
              <li><code>table_name</code>: table to read.</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.opening.mysql import open_mysql

df = open_mysql("localhost", 3306, "root", "1234", "humanitarian_mysql", "needs_table")
print(df)`}</code></pre>
          </div>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> A Polars table with rows from the table.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>open_netcdf(file_path)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Open a NetCDF file (grids like climate).</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> You get climate/flood/rainfall rasters.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Convert to a table for quick analysis.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Parameters</h3>
            <ul className="text-sm text-gray-700 list-disc pl-6">
              <li><code>file_path</code>: path of the NetCDF. Example: <code>"data/rainfall.nc"</code>.</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
# Example usage (depends on your netcdf.py function signature)
from huda.opening.netcdf import open_netcdf

df = open_netcdf("data/rainfall.nc")
print(df.head())`}</code></pre>
          </div>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> A Polars table with values extracted from the NetCDF (example structure).</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>open_spss(file_path)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Open an SPSS .sav file.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Survey firms share .sav files.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Convert to a normal table for analysis.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Parameters</h3>
            <ul className="text-sm text-gray-700 list-disc pl-6">
              <li><code>file_path</code>: path to .sav. Example: <code>"data/household.sav"</code>.</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.opening.spss import open_spss

df = open_spss("data/household.sav")
print(df)`}</code></pre>
          </div>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> A Polars table of the survey.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>open_stata(file_path)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Open a Stata .dta file.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Partners share .dta data.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Convert to a normal table for analysis.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Parameters</h3>
            <ul className="text-sm text-gray-700 list-disc pl-6">
              <li><code>file_path</code>: path to .dta. Example: <code>"data/household.dta"</code>.</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.opening.stata import open_stata

df = open_stata("data/household.dta")
print(df)`}</code></pre>
          </div>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> A Polars table of the survey.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>open_xml(file_path)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Open an XML file.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Old systems export XML.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Turn XML into a table when possible.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Parameters</h3>
            <ul className="text-sm text-gray-700 list-disc pl-6">
              <li><code>file_path</code>: path to .xml. Example: <code>"data/old_system.xml"</code>.</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.opening.xml import open_xml

df_or_tree = open_xml("data/old_system.xml")
print(df_or_tree)`}</code></pre>
          </div>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> A Polars table or a parsed XML structure (depends on content).</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>detect_encoding(file_path)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Guess the file text encoding (UTF-8, etc.).</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> CSV opens with strange letters.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Helps read text correctly.</p>
        <div className="grid md:grid-cols-2 gap-6 mt-4">
          <div>
            <h3 className="text-sm font-semibold">Example</h3>
            <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.opening.encoding_detector import detect_encoding

enc = detect_encoding("data/afg_survey.csv")
print(enc)`}</code></pre>
          </div>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> A text like "utf-8" to use when opening files.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>Opening API (module quick view)</span>
        </div>
        <p className="text-gray-700 text-sm">You can import functions directly from their files as shown above. This keeps things simple and clear.</p>
      </section>
    </DocsLayout>
  )
}
