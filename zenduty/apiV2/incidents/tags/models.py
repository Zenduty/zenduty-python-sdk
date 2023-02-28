from datetime import datetime
from uuid import UUID
from zenduty.apiV2.serializer import JsonSerializable


class Tag(JsonSerializable):
    unique_id: UUID
    incident: int
    team_tag: UUID
    name: str
    color: str
    tag_id: UUID
    creation_date: datetime

    def __init__(
        self,
        unique_id: UUID,
        incident: int,
        team_tag: UUID,
        name: str,
        color: str,
        tag_id: UUID,
        creation_date: datetime,
    ) -> None:
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)
        self.incident = incident
        self.team_tag = team_tag if type(team_tag) is not str else UUID(team_tag)
        self.name = name
        self.color = color
        self.tag_id = tag_id if type(tag_id) is not str else UUID(tag_id)
        self.creation_date = (
            creation_date
            if type(creation_date) is datetime
            else datetime.fromisoformat(creation_date.replace("Z", "+00:00"))
        )
