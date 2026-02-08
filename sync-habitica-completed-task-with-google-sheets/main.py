import asyncio
from app.gsheets import create_sheet
from app.habitica import get_habitica_tasks
from app.config import config


def build_habitica_data_for_gsheet(
    tasks: list[dict],
) -> list[list[str | int | float]]:
    header = [col_name for col_name, _ in config.HABITICA_GSHEET_COLUMNS]
    rows: list[list[str | int | float]] = [header]
    for task in tasks:
        row = []
        for _, key in config.HABITICA_GSHEET_COLUMNS:
            value = task.get(key, "")
            if value is None:
                value = ""
            row.append(value)
        rows.append(row)
    return rows


async def main():
    completed_habitica_tasks = await get_habitica_tasks(type="completedTodos")
    print(completed_habitica_tasks)
    completed_habitica_tasks_list = build_habitica_data_for_gsheet(
        completed_habitica_tasks
    )
    await create_sheet(
        sheet_name="db",
        values=completed_habitica_tasks_list,
        range="A1:Z9999",
    )


if __name__ == "__main__":
    asyncio.run(main())
