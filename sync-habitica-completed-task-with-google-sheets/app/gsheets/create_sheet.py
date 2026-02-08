from app.config import config
from app.gsheets._service import service


async def create_sheet(
    sheet_name: str, values: list[list[str | int | float]], range: str
):
    service.spreadsheets().values().update(
        spreadsheetId=config.GS_SPREADSHEET_ID,
        range=f"{sheet_name}!{range}",
        valueInputOption="USER_ENTERED",
        body={"values": values},
    ).execute()
