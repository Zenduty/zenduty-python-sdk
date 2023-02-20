from datetime import datetime

from zenduty.apiV2.serializer import JsonSerializable


class IncidentNote(JsonSerializable):
    unique_id: str
    incident: int
    user: str
    note: str
    user_name: str
    creation_date: datetime

    def __init__(
        self,
        unique_id: str,
        incident: int,
        user: str,
        note: str,
        user_name: str,
        creation_date: datetime,
    ) -> None:
        self.unique_id = unique_id
        self.incident = incident
        self.user = user
        self.note = note
        self.user_name = user_name
        self.creation_date = (
            creation_date
            if type(creation_date) is datetime
            else datetime.fromisoformat(creation_date.replace("Z", "+00:00"))
        )
