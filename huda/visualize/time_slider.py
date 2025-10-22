from typing import Dict, Any, Optional


def time_slider(
    time_col: str,
    title: Optional[str] = None
) -> Dict[str, Any]:
    """Time Slider (placeholder spec)."""
    return {
        "type": "time_slider",
        "title": title or "Time Slider",
        "encoding": {"time": time_col},
    }
