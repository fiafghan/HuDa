import React from 'react'
import DocsLayout from '../../layouts/DocsLayout'

export default function DocumentProcessing() {
  return (
    <DocsLayout title="Phase: Text & Document Processing">
      <p className="text-gray-700">Each function returns a lightweight intent spec; it does not perform extraction or NLP itself. Use with your preferred tools. Every card includes What/When/Why/Parameters, a Python Example, and the returned Output preview.</p>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="pdf-tables">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">process_pdf_tables(pdf_path, pages=None, table_engine="camelot", output_format="csv")</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Extract tabular data from PDFs.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Situation reports and annexes.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Convert tables to data.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.document_processing import process_pdf_tables\nspec = process_pdf_tables("/reports/sitrep.pdf", pages="1-3", table_engine="camelot", output_format="csv")\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  "type": "doc_process_pdf_tables",\n  "pdf_path": "/reports/sitrep.pdf",\n  "options": {"pages": "1-3", "table_engine": "camelot", "output_format": "csv"},\n  "preview": {"will_extract_tables": true}\n}`}</code></pre>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="word-reports">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">process_word_reports(docx_path, extract_tables=True, extract_paragraphs=True, output_format="json")</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Extract text and tables from DOCX.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Shared partner reports.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Structure unstructured content.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.document_processing import process_word_reports\nspec = process_word_reports("/reports/partner.docx", extract_tables=True, extract_paragraphs=True, output_format="json")\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  "type": "doc_process_word_reports",\n  "docx_path": "/reports/partner.docx",\n  "options": {"extract_tables": true, "extract_paragraphs": true, "output_format": "json"},\n  "preview": {"will_extract": true}\n}`}</code></pre>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="extract-indicators">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">extract_indicators_from_text(texts, indicators=None, language="en", use_regex=True)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Find indicator mentions.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Parsing narrative reports.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Build indicator datasets.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.document_processing import extract_indicators_from_text\ntexts = ["Coverage reached 60% in province A.", "FCS median 45."]\nspec = extract_indicators_from_text(texts, indicators=["coverage","fcs"], language="en")\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  "type": "doc_extract_indicators",\n  "language": "en",\n  "inputs": 2,\n  "options": {"use_regex": true, "indicators": ["coverage","fcs"]},\n  "preview": {"will_extract_mentions": true}\n}`}</code></pre>
      </section>
      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="nl-search">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">dataset_natural_language_search(query, datasets, top_k=5, use_embeddings=True, language="en")</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Query datasets in natural language.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Exploratory analysis.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Faster discovery.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.document_processing import dataset_natural_language_search\nspec = dataset_natural_language_search(\"Which districts have lowest coverage?\", [\"/data/coverage.csv\"], top_k=3)\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"doc_dataset_nl_search\",\n  \"query\": \"Which districts have lowest coverage?\",\n  \"datasets\": [\"/data/coverage.csv\"],\n  \"options\": {\"top_k\": 3, \"use_embeddings\": true, \"language\": \"en\"},\n  \"preview\": {\"will_search\": true}\n}`}</code></pre>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="translate-indicators">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">translate_indicators(texts, source_lang="en", target_langs=["fa","ps","ar","fr"], domain="humanitarian")</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Translate indicator terms.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Multilingual reporting.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Consistent terminology.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.document_processing import translate_indicators\nspec = translate_indicators([\"coverage\",\"needs\"], source_lang=\"en\", target_langs=[\"fa\",\"ps\"]) \nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"doc_translate_indicators\",\n  \"source_lang\": \"en\",\n  \"target_langs\": [\"fa\",\"ps\"],\n  \"inputs\": 2,\n  \"options\": {\"domain\": \"humanitarian\"},\n  \"preview\": {\"will_translate\": true}\n}`}</code></pre>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="ner">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">named_entity_recognition(texts, language="en", entity_types=None, model_type="transformer")</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Tag orgs and locations.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Extract structured entities.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Build knowledge bases.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.document_processing import named_entity_recognition\nspec = named_entity_recognition([\"WFP delivered in Kandahar\"], language=\"en\", entity_types=[\"ORG\",\"LOC\"])\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"doc_named_entity_recognition\",\n  \"language\": \"en\",\n  \"inputs\": 1,\n  \"options\": {\"entity_types\": [\"ORG\",\"LOC\"], \"model_type\": \"transformer\"},\n  \"preview\": {\"will_tag_entities\": true}\n}`}</code></pre>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="sentiment">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">sentiment_analysis_reports(texts, language="en", model_type="transformer", aggregate=True)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Score sentiment in reports.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Field reporting, community feedback.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Monitor perception and risk.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.document_processing import sentiment_analysis_reports\nspec = sentiment_analysis_reports([\"Access improved but gaps remain.\"], language=\"en\", aggregate=True)\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"doc_sentiment_analysis\",\n  \"language\": \"en\",\n  \"inputs\": 1,\n  \"options\": {\"model_type\": \"transformer\", \"aggregate\": true},\n  \"preview\": {\"will_score_sentiment\": true}\n}`}</code></pre>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="needs-classification">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">classify_needs_by_sector(texts, label_set=["food","wash","health","shelter","protection","education"], language="en", model_type="transformer")</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Classify needs text to sectors.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Needs assessments.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Rapid thematic tagging.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.document_processing import classify_needs_by_sector\nspec = classify_needs_by_sector([\"Households lack access to safe water.\"], label_set=[\"wash\",\"health\"]) \nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"doc_classify_needs_by_sector\",\n  \"language\": \"en\",\n  \"labels\": [\"wash\",\"health\"],\n  \"inputs\": 1,\n  \"options\": {\"model_type\": \"transformer\"},\n  \"preview\": {\"will_classify\": true}\n}`}</code></pre>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="crisis-keywords">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">extract_crisis_keywords(texts, language="en", method="textrank", top_k=20)</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Key phrases from text.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Thematic analysis.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Summarize large volumes.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.document_processing import extract_crisis_keywords\nspec = extract_crisis_keywords([\"Roads blocked due to floods; aid delayed.\"], method=\"textrank\", top_k=10)\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"doc_extract_crisis_keywords\",\n  \"language\": \"en\",\n  \"inputs\": 1,\n  \"options\": {\"method\": \"textrank\", \"top_k\": 10},\n  \"preview\": {\"will_extract_keywords\": true}\n}`}</code></pre>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="knowledge-graph">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-1">build_humanitarian_knowledge_graph(entities, relations, schema=None, export_format="graphml")</div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Build entity-relation graphs.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Linking orgs, places, events.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Reasoning and discovery.</p>
        <h3 className="text-sm font-semibold mt-2">Example</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`from huda.document_processing import build_humanitarian_knowledge_graph\nentities = [{\"id\":\"org1\",\"type\":\"ORG\",\"name\":\"WFP\"},{\"id\":\"loc1\",\"type\":\"LOC\",\"name\":\"Kandahar\"}]\nrelations = [(\"org1\",\"operates_in\",\"loc1\")]\nspec = build_humanitarian_knowledge_graph(entities, relations, export_format=\"graphml\")\nprint(spec)`}</code></pre>
        <h3 className="text-sm font-semibold mt-2">Output</h3>
        <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`{\n  \"type\": \"doc_build_knowledge_graph\",\n  \"counts\": {\"entities\": 2, \"relations\": 1},\n  \"export_format\": \"graphml\",\n  \"schema\": {},\n  \"preview\": {\"will_construct_graph\": true}\n}`}</code></pre>
      </section>
    </DocsLayout>
  )
}
