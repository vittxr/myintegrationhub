from typing import TypedDict, TypeVar, Generic, Literal, Any

T = TypeVar("T")


class HabiticaAPIResponse(TypedDict, Generic[T]):
    success: bool
    data: T
    notifications: list[Any]


class GroupApproval(TypedDict, total=False):
    required: bool
    approved: bool
    requested: bool


class Group(TypedDict, total=False):
    assignedUsers: list[Any]
    approval: GroupApproval


class Reminder(TypedDict, total=False):
    time: str
    startDate: str
    id: str


class Repeat(TypedDict, total=False):
    su: bool
    s: bool
    f: bool
    th: bool
    w: bool
    t: bool
    m: bool


class HabiticaTask(TypedDict, total=False):
    _id: str
    userId: str
    alias: str
    text: str
    type: Literal["habit", "daily", "todo", "reward"]
    notes: str
    tags: list[str]
    value: int
    priority: int
    attribute: str
    challenge: dict[str, Any]
    group: Group
    reminders: list[Reminder]
    createdAt: str
    updatedAt: str
    updatedAt: str
    id: str
    checklist: list[Any]
    collapseChecklist: bool
    completed: bool
    history: list[Any]
    streak: int
    repeat: Repeat
    startDate: str
    everyX: int
    frequency: str
