from typing import Dict, Any, Optional, List


def extract_crisis_keywords(
    texts: List[str],
    language: str = "en",
    method: str = "textrank",
    top_k: int = 20
) -> Dict[str, Any]:
    """
    Extract crisis-relevant keywords — placeholder intent

    Parameters
    ----------
    texts : list[str]
    language : str
    method : str
        e.g., "textrank", "yake", "tfidf".
    top_k : int
        Number of keywords to return.
    """
    return {
        "type": "doc_extract_crisis_keywords",
        "language": language,
        "inputs": len(texts),
        "options": {"method": method, "top_k": top_k},
        "preview": {"will_extract_keywords": True}
    }
