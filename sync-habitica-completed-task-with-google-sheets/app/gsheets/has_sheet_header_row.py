import typing
from app.config import config
from app.gsheets._service import service


async def has_sheet_header_row(sheet_name: str, skip_header: bool = True):
    """
    Get the first non-empty row of a Google Sheet in constant time.
    """
    _range = "A2:Z2" if skip_header else "A1:Z1"
    res = (
        service.spreadsheets()
        .values()
        .get(
            spreadsheetId=config.GS_SPREADSHEET_ID,
            range=f"'{sheet_name}'!{_range}",
        )
        .execute()
    )

    values: list[typing.Any] = res.get("values")
    return values[0] if values else None
