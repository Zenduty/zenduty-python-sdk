from uuid import UUID
from datetime import datetime

from zenduty.apiV2.serializer import JsonSerializable


class TaskTemplate(JsonSerializable):
    unique_id: UUID
    team: UUID
    name: str
    creation_date: datetime
    summary: str
    due_immediately: int

    def __init__(
        self,
        unique_id: UUID,
        team: UUID,
        name: str,
        creation_date: datetime,
        summary: str,
        due_immediately: int,
    ) -> None:
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)
        self.team = team if type(team) is not str else UUID(team)
        self.name = name
        self.creation_date = (
            creation_date
            if type(creation_date) is datetime
            else datetime.fromisoformat(creation_date.replace("Z", "+00:00"))
        )
        self.summary = summary
        self.due_immediately = due_immediately
