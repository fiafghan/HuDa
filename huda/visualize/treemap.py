from typing import Dict, Any, Optional


def treemap(
    category_col: str,
    value_col: str,
    group_col: Optional[str] = None,
    title: Optional[str] = None
) -> Dict[str, Any]:
    """Treemap (placeholder spec)."""
    return {
        "type": "treemap",
        "title": title or "Treemap",
        "encoding": {"category": category_col, "value": value_col, "group": group_col},
    }
