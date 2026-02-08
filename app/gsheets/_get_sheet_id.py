from app.gsheets._service import (
    service,  # ignore
)


async def get_sheet_id(spreadsheet_id: str | None, sheet_title: str) -> str | None:
    """
    Fetches the sheet ID for a given sheet title from a Google Sheets spreadsheet.

    Args:
        sheet_title (str): The title of the sheet for which to retrieve the ID.

    Returns:
        str | None: The ID of the sheet if found, otherwise None.
    """
    spreadsheet = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    sheet_id: str | None = None
    for sheet in spreadsheet["sheets"]:
        if sheet["properties"]["title"] == sheet_title:
            sheet_id = sheet["properties"]["sheetId"]
            break

    return sheet_id
