from uuid import UUID
from datetime import datetime

from zenduty.apiV2.serializer import JsonSerializable


class Priority(JsonSerializable):
    unique_id: UUID
    name: str
    description: str
    creation_date: datetime
    color: str
    team: int

    def __init__(
        self,
        unique_id: UUID,
        name: str,
        description: str,
        creation_date: datetime,
        color: str,
        team: int,
    ) -> None:
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)
        self.name = name
        self.description = description
        self.creation_date = (
            creation_date
            if type(creation_date) is datetime
            else datetime.fromisoformat(creation_date.replace("Z", "+00:00"))
        )
        self.color = color
        self.team = team
