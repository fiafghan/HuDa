from typing import Dict, Any, List, Optional


def compare_countries(
    country_col: str,
    metric_cols: List[str],
    title: Optional[str] = None
) -> Dict[str, Any]:
    """Compare Multiple Countries (placeholder spec)."""
    return {
        "type": "compare_countries",
        "title": title or "Compare Countries",
        "encoding": {"country": country_col, "metrics": metric_cols},
    }
