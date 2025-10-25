import React from 'react'
import DocsLayout from '../../layouts/DocsLayout'

export default function Automation() {
  return (
    <DocsLayout title="Phase: Automation & Workflows">
      <p className="text-gray-700">Automation intent specs for reports, dashboards, ETL, and governance. Each function returns a lightweight spec; execution is out of scope. Sections include What/When/Why, Parameters, Example, and Output.</p>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="monthly-report">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>automate_monthly_report(report_name, data_sources, schedule="0 7 1 * *", deliver_to=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Schedule monthly report builds.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Regular situation reports.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Consistency and timeliness.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.automation import automate_monthly_report\nspec = automate_monthly_report(\n    report_name=\"Monthly SITREP\",\n    data_sources=[\"/data/indicators.csv\", \"/data/funding.csv\"],\n    schedule=\"0 7 1 * *\",\n    deliver_to=[\"ops@org.org\"]\n)\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"automation_monthly_report\",\n  \"report_name\": \"Monthly SITREP\",\n  \"data_sources\": [\"/data/indicators.csv\", \"/data/funding.csv\"],\n  \"schedule\": \"0 7 1 * *\",\n  \"deliver_to\": [\"ops@org.org\"],\n  \"preview\": {\"will_generate\": true, \"assets\": [\"pdf\", \"html\"], \"sections\": [\"overview\", \"indicators\", \"annexes\"]}\n}`}</code></pre>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="snapshot-dashboards">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>automate_snapshot_dashboards(dashboard_name, charts, schedule="0 8 * * 1", deliver_to=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Weekly snapshot dashboard export.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Monday summaries.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Quick situational awareness.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.automation import automate_snapshot_dashboards\nfrom huda.visualize import bar_chart\ncharts = [bar_chart({\"a\":[1],\"b\":[2]}, \"a\",\"b\")]\nspec = automate_snapshot_dashboards(\"Weekly Snapshot\", charts, schedule=\"0 8 * * 1\", deliver_to=[\"dash@org.org\"])\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"automation_snapshot_dashboards\",\n  \"dashboard_name\": \"Weekly Snapshot\",\n  \"charts_count\": 1,\n  \"schedule\": \"0 8 * * 1\",\n  \"deliver_to\": [\"dash@org.org\"],\n  \"preview\": {\"will_generate\": true, \"format\": \"html\"}\n}`}</code></pre>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="dataset-downloads">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>automate_dataset_downloads(sources, destination_dir, schedule="0 */6 * * *", auth_env_vars=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Scheduled API downloads.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Frequent updates (e.g., 6h).</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Keep data fresh.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.automation import automate_dataset_downloads\nspec = automate_dataset_downloads(\n    sources=[\"https://api.org/v1/data\"],\n    destination_dir=\"/data/cache\",\n    schedule=\"0 */6 * * *\",\n    auth_env_vars={\"API_TOKEN\":\"ENV_API_TOKEN\"}\n)\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"automation_dataset_downloads\",\n  \"sources\": [\"https://api.org/v1/data\"],\n  \"destination_dir\": \"/data/cache\",\n  \"schedule\": \"0 */6 * * *\",\n  \"auth_env_vars\": {\"API_TOKEN\": \"ENV_API_TOKEN\"},\n  \"preview\": {\"will_download\": true, \"count_sources\": 1}\n}`}</code></pre>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="scheduled-etl">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>scheduled_etl_pipeline(name, extract_steps, transform_steps, load_steps, schedule="0 2 * * *")</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Daily ETL orchestration for repeatable pipelines.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Regular indicator builds and dataset refreshes.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Reliability, auditability, and consistency.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.automation import scheduled_etl_pipeline\nspec = scheduled_etl_pipeline(\n    name=\"daily_indicators\",\n    extract_steps=[{\"type\":\"download\", \"uri\":\"https://api.org/indicators\"}],\n    transform_steps=[{\"type\":\"clean\"}],\n    load_steps=[{\"type\":\"to_sql\", \"table\":\"indicators\"}],\n    schedule=\"0 2 * * *\"\n)\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"automation_scheduled_etl\",\n  \"name\": \"daily_indicators\",\n  \"schedule\": \"0 2 * * *\",\n  \"etl\": {\"extract\": [{\"type\": \"download\", \"uri\": \"https://api.org/indicators\"}], \"transform\": [{\"type\": \"clean\"}], \"load\": [{\"type\": \"to_sql\", \"table\": \"indicators\"}]},\n  \"preview\": {\"extract\": 1, \"transform\": 1, \"load\": 1}\n}`}</code></pre>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="dataset-vcs">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>dataset_version_control(dataset_id, storage_uri, strategy="snapshot", retain_versions=12)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Version datasets and keep prior copies.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Compliance, reproducibility, or rollback needs.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Traceability and governance.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.automation import dataset_version_control\nspec = dataset_version_control(\"hhs2025\", storage_uri=\"s3://bucket/datasets/hhs2025\", strategy=\"snapshot\", retain_versions=12)\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"automation_dataset_version_control\",\n  \"dataset_id\": \"hhs2025\",\n  \"storage_uri\": \"s3://bucket/datasets/hhs2025\",\n  \"options\": {\"strategy\": \"snapshot\", \"retain_versions\": 12},\n  \"preview\": {\"enabled\": true}\n}`}</code></pre>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="data-lineage">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>data_lineage_tracking(dataset_id, sources, transformations, destinations)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Track where data came from and how it changed.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Audits, debugging, and dependency analysis.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Accountability and faster troubleshooting.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.automation import data_lineage_tracking\nspec = data_lineage_tracking(\n    dataset_id=\"hhs2025\",\n    sources=[\"raw.csv\"],\n    transformations=[\"clean\",\"aggregate\"],\n    destinations=[\"indicators.csv\"]\n)\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"automation_data_lineage\",\n  \"dataset_id\": \"hhs2025\",\n  \"lineage\": {\"sources\": [\"raw.csv\"], \"transformations\": [\"clean\", \"aggregate\"], \"destinations\": [\"indicators.csv\"]},\n  \"preview\": {\"sources\": 1, \"steps\": 2, \"destinations\": 1}\n}`}</code></pre>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="change-detection">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>change_detection_in_datasets(dataset_id, baseline_version, current_version, keys=None, threshold=0.0)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Compare two dataset versions and quantify differences.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> New waves, corrections, or updates are published.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Quality assurance and alerting on unexpected changes.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.automation import change_detection_in_datasets\nspec = change_detection_in_datasets(\n    dataset_id=\"hhs2025\", baseline_version=\"v1.0\", current_version=\"v1.1\", keys=[\"hh_id\"], threshold=0.05\n)\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"automation_change_detection\",\n  \"dataset_id\": \"hhs2025\",\n  \"versions\": {\"baseline\": \"v1.0\", \"current\": \"v1.1\"},\n  \"options\": {\"keys\": [\"hh_id\"], \"threshold\": 0.05},\n  \"preview\": {\"will_compare\": true}\n}`}</code></pre>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="auto-refresh">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>auto_refresh_visualizations(dashboard_name, refresh_interval_minutes=60, data_sources=None, notify_on_refresh=False)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Schedule dashboard refreshes.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Live reporting and near-real-time views.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Keeps visuals up to date without manual steps.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.automation import auto_refresh_visualizations\nspec = auto_refresh_visualizations(\"Ops Dashboard\", refresh_interval_minutes=30, notify_on_refresh=True)\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"automation_auto_refresh_visualizations\",\n  \"dashboard_name\": \"Ops Dashboard\",\n  \"refresh_interval_minutes\": 30,\n  \"data_sources\": [],\n  \"options\": {\"notify_on_refresh\": true},\n  \"preview\": {\"will_schedule\": true}\n}`}</code></pre>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="reusable-templates">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>save_reusable_templates(template_name, components, storage_uri, version=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Save and version reusable analysis components.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Standardize workflows across teams or projects.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Promotes reuse and consistency.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.automation import save_reusable_templates\ncomponents = [{\"type\":\"chart\",\"name\":\"coverage_bar\"}]\nspec = save_reusable_templates(\"coverage_pack\", components, storage_uri=\"s3://bucket/templates\", version=\"1.0.0\")\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"automation_reusable_templates\",\n  \"template_name\": \"coverage_pack\",\n  \"components_count\": 1,\n  \"storage_uri\": \"s3://bucket/templates\",\n  \"version\": \"1.0.0\",\n  \"preview\": {\"saved\": true}\n}`}</code></pre>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="batch-processing">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>batch_processing_datasets(job_name, inputs, processing_steps, parallelism=4, retry_on_fail=True)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Run the same processing steps across multiple inputs.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Backfills and bulk updates.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Efficiency and throughput for large jobs.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.automation import batch_processing_datasets\nsteps = [{\"type\":\"clean\"}, {\"type\":\"dedupe\"}]\nspec = batch_processing_datasets(\"backfill_q3\", inputs=[\"a.csv\",\"b.csv\"], processing_steps=steps, parallelism=8)\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"automation_batch_processing\",\n  \"job_name\": \"backfill_q3\",\n  \"inputs_count\": 2,\n  \"parallelism\": 8,\n  \"options\": {\"retry_on_fail\": true},\n  \"steps\": [{\"type\": \"clean\"}, {\"type\": \"dedupe\"}],\n  \"preview\": {\"will_process\": true}\n}`}</code></pre>
      </section>
    </DocsLayout>
  )
}

