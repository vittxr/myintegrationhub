from typing import Any

from app.config import config
from app.gsheets._service import service


async def append_sheet_data(
    sheet_name: str,
    values: list[list[str | int | float]],
    start_range: str,
) -> None:
    """
    Insert new rows at the given cell without removing existing data.

    Existing content starting at `start_range` is shifted down: the new rows
    are written at `start_range`, and all previous data in that range is
    written again immediately below the new rows.

    Args:
        sheet_name: Name of the sheet tab (e.g. "Sheet1").
        values: Rows to insert. Each inner list is a row of cell values.
        start_range: A1-style range where insertion starts (e.g. "A2").
            All existing data from this cell to the end of the sheet is
            read and re-written below the inserted rows.
    """
    read_range = f"{sheet_name}!{start_range}:ZZ"
    res = (
        service.spreadsheets()
        .values()
        .get(
            spreadsheetId=config.GS_SPREADSHEET_ID,
            range=read_range,
        )
        .execute()
    )
    existing: list[list[Any]] = res.get("values") or []
    combined = values + existing

    (
        service.spreadsheets()
        .values()
        .update(
            spreadsheetId=config.GS_SPREADSHEET_ID,
            range=f"{sheet_name}!{start_range}",
            valueInputOption="USER_ENTERED",
            body={"values": combined},
        )
        .execute()
    )
