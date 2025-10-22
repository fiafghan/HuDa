from typing import Dict, Any, Optional


def plot_targeted_vs_reached(
    targeted_col: str,
    reached_col: str,
    group_col: Optional[str] = None,
    title: Optional[str] = None
) -> Dict[str, Any]:
    """Plot Targeted vs Reached (placeholder spec)."""
    return {
        "type": "targeted_vs_reached",
        "title": title or "Targeted vs Reached",
        "encoding": {"targeted": targeted_col, "reached": reached_col, "group": group_col},
    }
