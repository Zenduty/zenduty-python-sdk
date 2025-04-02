import logging
from uuid import UUID
from datetime import datetime
from zenduty.apiV2.serializer import JsonSerializable

class IncidentRole(JsonSerializable):
    unique_id: UUID
    title: str
    description: str
    creation_date: datetime
    rank: int
    team: UUID

    def __init__(
        self,
        unique_id: UUID,
        title: str,
        description: str,
        creation_date: datetime,
        rank: int,
        team: UUID = None,
        **kwargs
    ) -> None:
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)
        self.title = title
        self.description = description
        self.creation_date = (
            creation_date
            if type(creation_date) is datetime
            else datetime.fromisoformat(creation_date.replace("Z", "+00:00"))
        )
        self.rank = rank
        self.team = team if type(team) is not str else UUID(team)
        if kwargs:
            logging.info(f"We have unexpected return values for {self.__class__.__name__}: {list(kwargs.keys())}")
