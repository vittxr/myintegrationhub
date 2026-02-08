from typing import Any
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build  # type: ignore
from app.config import config

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
RANGE = "!A{rows_qty_1}:L{rows_qty_2}"

credentials = Credentials.from_service_account_file(  # type: ignore
    filename=config.GOOGLE_SHEETS_CREDENTIALS_PATH, scopes=SCOPES
)
service: Any = build("sheets", "v4", credentials=credentials)  # type: ignore
