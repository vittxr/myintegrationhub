import typing
from app.config import config
from app.gsheets._service import service


async def has_sheet_header_row(sheet_name: str, header_data: list[str]) -> bool:
    """
    Check if the first row has the header row
    """
    res = (
        service.spreadsheets()
        .values()
        .get(
            spreadsheetId=config.GS_SPREADSHEET_ID,
            range=f"'{sheet_name}'!A1:Z1",
        )
        .execute()
    )
    values: list[typing.Any] = res.get("values") or [None]
    res = values[0] == header_data
    return res
