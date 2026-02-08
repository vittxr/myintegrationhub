from app.config import config
from app.gsheets._service import service


async def get_sheet_last_row(
    sheet_name: str,
):
    """
    Get the last non-empty row of a Google Sheet in constant time.

    Fetches a fixed-size batch from the end of the sheet (last 1000 rows) and finds
    the last non-empty row within that batch. This ensures constant execution time
    regardless of total rows in the sheet.
    """
    spreadsheet = (
        service.spreadsheets().get(spreadsheetId=config.GS_SPREADSHEET_ID).execute()
    )

    last_row = 1
    for sheet in spreadsheet.get("sheets", []):
        if sheet["properties"]["title"] == sheet_name:
            last_row = sheet["properties"]["gridProperties"]["rowCount"]
            break

    # Fetch a fixed-size batch from the end (last 1000 rows)
    # This ensures constant time - always fetches exactly 1000 rows max
    batch_size = 1000
    start_row = max(1, last_row - batch_size + 1)

    res = (
        service.spreadsheets()
        .values()
        .get(
            spreadsheetId=config.GS_SPREADSHEET_ID,
            range=f"{sheet_name}!A{start_row}:Z{last_row}",
        )
        .execute()
    )

    values = res.get("values")
    if not values or len(values) == 0:
        return None

    for i in range(len(values) - 1, -1, -1):
        row = values[i]
        if row and any(cell and str(cell).strip() for cell in row):
            return row

    return None
