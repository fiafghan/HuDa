from typing import Dict, Any, Optional


def api_integration_output(
    endpoint_url: str,
    method: str = "POST",
    headers: Optional[Dict[str, str]] = None,
    auth_type: Optional[str] = None,
    auth_token_env: Optional[str] = None
) -> Dict[str, Any]:
    """
    API integration for outputs (placeholder intent)

    Returns a spec describing an API call to deliver outputs to another system.
    Does not perform real HTTP requests and does not include secrets.

    Parameters
    ----------
    endpoint_url : str
        Target API endpoint.
    method : str, default "POST"
        HTTP method, e.g., GET/POST/PUT.
    headers : dict[str,str] | None
        Optional headers (no secrets).
    auth_type : str | None
        Optional auth method description (e.g., "Bearer").
    auth_token_env : str | None
        Environment variable name where token is stored.
    """
    return {
        "type": "api_integration",
        "endpoint_url": endpoint_url,
        "method": method,
        "headers": headers or {},
        "auth": {"type": auth_type, "token_env": auth_token_env},
        "preview": {"will_send_payload": True},
    }
