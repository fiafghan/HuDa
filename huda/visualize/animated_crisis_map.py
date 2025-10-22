from typing import Dict, Any, Optional


def animated_crisis_map(
    geojson_col: str,
    time_col: str,
    value_col: str,
    title: Optional[str] = None
) -> Dict[str, Any]:
    """Animated Crisis Progression Map (placeholder spec)."""
    return {
        "type": "animated_map",
        "title": title or "Animated Crisis Map",
        "encoding": {"geo": geojson_col, "time": time_col, "value": value_col},
    }
