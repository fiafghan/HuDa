from typing import Dict, Any, Optional, List


def dataset_natural_language_search(
    query: str,
    datasets: List[str],
    top_k: int = 5,
    use_embeddings: bool = True,
    language: str = "en"
) -> Dict[str, Any]:
    """
    Natural language search on datasets — placeholder intent

    Parameters
    ----------
    query : str
        Search question or statement.
    datasets : list[str]
        Identifiers/paths to datasets to search.
    top_k : int
        Number of results to return.
    use_embeddings : bool
        Whether to use semantic embeddings.
    language : str
        Query language code.
    """
    return {
        "type": "doc_dataset_nl_search",
        "query": query,
        "datasets": datasets,
        "options": {"top_k": top_k, "use_embeddings": use_embeddings, "language": language},
        "preview": {"will_search": True}
    }
