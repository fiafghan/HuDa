import React from 'react'
import DocsLayout from '../../layouts/DocsLayout'

export default function ML4Humanitarian() {
  return (
    <DocsLayout title="Phase: ML for Humanitarian Data">
      <p className="text-gray-700">Each function returns a lightweight ML intent spec — it does not train or predict. Use these specs to orchestrate pipelines in your chosen ML stack. Every card includes What/When/Why/Parameters, a Python Example, and the returned Output.</p>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="predict-displacement">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">predict_displacement_flows(features, target="displaced_next_week", model_type="xgboost", horizon_days=7, spatial_granularity="district")</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Forecast short-term displacement flows.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Preparedness and surge planning.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Anticipatory action.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.ml4humanitarian import predict_displacement_flows\nspec = predict_displacement_flows(features=[\"incidents\",\"rainfall\",\"market_price\"], horizon_days=7)\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"ml_predict_displacement_flows\",\n  \"model_type\": \"xgboost\",\n  \"features_count\": 3,\n  \"target\": \"displaced_next_week\",\n  \"horizon_days\": 7,\n  \"spatial_granularity\": \"district\",\n  \"preview\": {\"will_train\": true, \"expected_outputs\": [\"predictions\",\"feature_importance\",\"cv_metrics\"]}\n}`}</code></pre>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="classify-severity">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">classify_crisis_severity(features, label_scheme="5-class", model_type="lgbm", spatial_granularity="province")</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Classify severity tiers.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Severity mapping exercises.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Harmonize and compare severity.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.ml4humanitarian import classify_crisis_severity\nspec = classify_crisis_severity(features=[\"needs\",\"incidents\",\"access_constraints\"], label_scheme=\"5-class\")\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"ml_classify_crisis_severity\",\n  \"model_type\": \"lgbm\",\n  \"features_count\": 3,\n  \"label_scheme\": \"5-class\",\n  \"spatial_granularity\": \"province\",\n  \"preview\": {\"will_train\": true, \"expected_outputs\": [\"labels\",\"probabilities\",\"confusion_matrix\"]}\n}`}</code></pre>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="misinfo-trends">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">detect_misinformation_trends(text_sources, language="en", model_type="transformer", window_days=7)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Track misinformation narratives.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Risk communication.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Counter-harm and awareness.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.ml4humanitarian import detect_misinformation_trends\nspec = detect_misinformation_trends(text_sources=[\"/data/social.jsonl\"], language=\"fa\", window_days=14)\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"ml_detect_misinformation_trends\",\n  \"model_type\": \"transformer\",\n  \"language\": \"fa\",\n  \"sources_count\": 1,\n  \"window_days\": 14,\n  \"preview\": {\"will_infer\": true, \"expected_outputs\": [\"trend_series\",\"keywords\",\"examples\"]}\n}`}</code></pre>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="funding-shortfalls">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">predict_funding_shortfalls(features, target="funding_gap_next_quarter", model_type="lgbm", horizon_days=90)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Forecast funding gaps.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Resource mobilization planning.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Anticipate shortfalls.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.ml4humanitarian import predict_funding_shortfalls\nspec = predict_funding_shortfalls(features=[\"pledges\",\"historical_disbursements\",\"appeal_revisions\"], horizon_days=90)\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"ml_predict_funding_shortfalls\",\n  \"model_type\": \"lgbm\",\n  \"features_count\": 3,\n  \"target\": \"funding_gap_next_quarter\",\n  \"horizon_days\": 90,\n  \"preview\": {\"will_train\": true, \"expected_outputs\": [\"predictions\",\"feature_importance\",\"cv_metrics\"]}\n}`}</code></pre>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="supply-chain">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">predict_supply_chain_bottlenecks(features, target="lead_time_delay", model_type="xgboost", horizon_days=14)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Predict logistics delays.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Operations planning.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Mitigate bottlenecks.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.ml4humanitarian import predict_supply_chain_bottlenecks\nspec = predict_supply_chain_bottlenecks(features=[\"road_access\",\"border_wait\",\"warehouse_stock\",\"orders\"])\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"ml_predict_supply_chain_bottlenecks\",\n  \"model_type\": \"xgboost\",\n  \"features_count\": 4,\n  \"target\": \"lead_time_delay\",\n  \"horizon_days\": 14,\n  \"preview\": {\"will_train\": true, \"expected_outputs\": [\"predictions\",\"feature_importance\",\"cv_metrics\"]}\n}`}</code></pre>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="survey-anomalies">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">detect_anomalies_in_surveys(feature_cols, method="isolation_forest", contamination=0.02, group_col=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Flag suspicious survey records.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Data quality control.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Ensure reliability.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.ml4humanitarian import detect_anomalies_in_surveys\nspec = detect_anomalies_in_surveys(feature_cols=[\"fcs\",\"rcsi\",\"hh_size\"], method=\"isolation_forest\", contamination=0.03, group_col=\"enumerator\")\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"ml_detect_survey_anomalies\",\n  \"method\": \"isolation_forest\",\n  \"features_count\": 3,\n  \"contamination\": 0.03,\n  \"group_col\": \"enumerator\",\n  \"preview\": {\"will_detect\": true, \"expected_outputs\": [\"anomaly_flags\",\"scores\",\"summary_by_group\"]}\n}`}</code></pre>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="crisis-text">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">crisis_event_text_classification(label_set, language="en", model_type="transformer", max_seq_length=256)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Classify crisis-related texts.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Triage reports and social content.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Faster situational awareness.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.ml4humanitarian import crisis_event_text_classification\nspec = crisis_event_text_classification(label_set=[\"displacement\",\"access\",\"wash\"], language=\"ps\", model_type=\"transformer\")\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"ml_crisis_text_classification\",\n  \"model_type\": \"transformer\",\n  \"labels\": [\"displacement\",\"access\",\"wash\"],\n  \"language\": \"ps\",\n  \"max_seq_length\": 256,\n  \"preview\": {\"will_train\": true, \"expected_outputs\": [\"labels\",\"probabilities\",\"examples\"]}\n}`}</code></pre>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="ews-modeling">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">early_warning_system_model(signals, target_event="crisis_escalation", model_type="ensemble", lead_time_days=14)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Model and score early warnings.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Anticipatory action triggers.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Timely alerts.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.ml4humanitarian import early_warning_system_model\nspec = early_warning_system_model(signals=[\"rainfall_anomaly\",\"market_volatility\",\"incidents\"], lead_time_days=21)\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"ml_early_warning_system\",\n  \"model_type\": \"ensemble\",\n  \"signals_count\": 3,\n  \"target_event\": \"crisis_escalation\",\n  \"lead_time_days\": 21,\n  \"preview\": {\"will_train\": true, \"expected_outputs\": [\"alert_scores\",\"thresholds\",\"precision_recall\"]}\n}`}</code></pre>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="predict-fci">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">predict_food_insecurity_levels(features, target="fci_next_month", model_type="lgbm", horizon_days=30, classification_scheme="ipc")</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Predict food insecurity levels.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> IPC planning, projections.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Targeting and prioritization.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.ml4humanitarian import predict_food_insecurity_levels\nspec = predict_food_insecurity_levels(features=[\"fcs\",\"rcsi\",\"rainfall\",\"wages\"], classification_scheme=\"ipc\")\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"ml_predict_food_insecurity\",\n  \"model_type\": \"lgbm\",\n  \"features_count\": 4,\n  \"target\": \"fci_next_month\",\n  \"horizon_days\": 30,\n  \"classification_scheme\": \"ipc\",\n  \"preview\": {\"will_train\": true, \"expected_outputs\": [\"predictions\",\"feature_importance\",\"cv_metrics\"]}\n}`}</code></pre>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="predict-mortality">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">predict_mortality_risks(features, target="mortality_rate_next_month", model_type="xgboost", horizon_days=30, age_group=None)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Predict mortality risks.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Health monitoring and alerts.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Prioritize lifesaving interventions.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.ml4humanitarian import predict_mortality_risks\nspec = predict_mortality_risks(features=[\"health_fac_per_10k\",\"sam_rate\",\"outbreaks\"], age_group=\"u5\")\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"ml_predict_mortality_risks\",\n  \"model_type\": \"xgboost\",\n  \"features_count\": 3,\n  \"target\": \"mortality_rate_next_month\",\n  \"horizon_days\": 30,\n  \"age_group\": \"u5\",\n  \"preview\": {\"will_train\": true, \"expected_outputs\": [\"predictions\",\"feature_importance\",\"cv_metrics\"]}\n}`}</code></pre>
      </section>
    </DocsLayout>
  )
}
