from typing import Dict, Any, List, Optional


def radar_chart(
    axis_cols: List[str],
    series_col: Optional[str] = None,
    title: Optional[str] = None
) -> Dict[str, Any]:
    """Radar/Spider Chart (placeholder spec)."""
    return {
        "type": "radar",
        "title": title or "Radar Chart",
        "encoding": {"axes": axis_cols, "series": series_col},
    }
