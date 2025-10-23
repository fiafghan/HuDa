from typing import Dict, Any, Optional, List


def named_entity_recognition(
    texts: List[str],
    language: str = "en",
    entity_types: Optional[List[str]] = None,
    model_type: str = "transformer"
) -> Dict[str, Any]:
    """
    Named entity recognition (organizations, locations) — placeholder intent

    Parameters
    ----------
    texts : list[str]
    language : str
    entity_types : list[str] | None
        e.g., ["ORG","LOC","GPE","PERSON"].
    model_type : str
        e.g., 'transformer', 'spacy', 'crf'.
    """
    return {
        "type": "doc_named_entity_recognition",
        "language": language,
        "inputs": len(texts),
        "options": {"entity_types": entity_types or ["ORG","LOC"], "model_type": model_type},
        "preview": {"will_tag_entities": True}
    }
