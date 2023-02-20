from uuid import UUID
from datetime import datetime
from zenduty.apiV2.serializer import JsonSerializable


class IncidentRole(JsonSerializable):
    unique_id: UUID
    team: UUID
    title: str
    description: str
    creation_date: datetime
    rank: int

    def __init__(
        self,
        unique_id: UUID,
        team: UUID,
        title: str,
        description: str,
        creation_date: datetime,
        rank: int,
    ) -> None:
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)
        self.team = team if type(team) is not str else UUID(team)
        self.title = title
        self.description = description
        self.creation_date = (
            creation_date
            if type(creation_date) is datetime
            else datetime.fromisoformat(creation_date.replace("Z", "+00:00"))
        )
        self.rank = rank
