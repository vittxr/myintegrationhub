import typing
from app.habitica._habitica_http_client import habitica_http_client
from app.habitica._schema import HabiticaAPIResponse, HabiticaTask


async def get_habitica_tasks(
    type: typing.Literal[
        "habits", "dailys", "todos", "rewards", "completedTodos"
    ] = "todos",
) -> HabiticaAPIResponse[list[HabiticaTask]]:
    query_params = {"type": type}
    res = habitica_http_client.get("/v3/tasks/user", params=query_params)
    res_json = res.json()
    res_typed = typing.cast(HabiticaAPIResponse[list[HabiticaTask]], res_json)
    return res_typed["data"]
