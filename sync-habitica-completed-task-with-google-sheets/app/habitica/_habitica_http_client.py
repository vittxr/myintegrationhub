import httpx
from app.config import config

base_headers: dict[str, str] = {
    "Content-Type": "application/json",
    "x-api-key": config.HABITICA_API_KEY or "",
    "x-api-user": config.HABITICA_USER_ID or "",
    "x-client": (config.HABITICA_USER_ID or "") + " - " + config.APP_NAME,
}


habitica_http_client = httpx.Client(
    headers=base_headers, base_url=config.HABITICA_BASE_URL
)
