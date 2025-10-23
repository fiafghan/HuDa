from typing import Dict, Any, Optional, List


def process_pdf_tables(
    pdf_path: str,
    pages: Optional[str] = None,
    table_engine: str = "camelot",
    output_format: str = "csv"
) -> Dict[str, Any]:
    """
    Process PDF reports (extract tables) — placeholder intent

    Parameters
    ----------
    pdf_path : str
    pages : str | None
        e.g., "1,2,5" or "1-3".
    table_engine : str
        "camelot" | "tabula" | "pdfplumber".
    output_format : str
        "csv" | "json" | "parquet".
    """
    return {
        "type": "doc_process_pdf_tables",
        "pdf_path": pdf_path,
        "options": {"pages": pages, "table_engine": table_engine, "output_format": output_format},
        "preview": {"will_extract_tables": True}
    }
