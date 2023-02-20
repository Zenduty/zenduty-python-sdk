from uuid import UUID
from typing import List, Optional, Union
from datetime import datetime

from zenduty.apiV2.serializer import JsonSerializable


class IncidentIncident(JsonSerializable):
    unique_id: str
    title: str
    incident_number: int

    def __init__(self, unique_id: str, title: str, incident_number: int) -> None:
        self.unique_id = unique_id
        self.title = title
        self.incident_number = incident_number


class IncidentElement(JsonSerializable):
    unique_id: UUID
    incident: IncidentIncident

    def __init__(
        self, unique_id: UUID, incident: Union[IncidentIncident, dict]
    ) -> None:
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)
        self.incident = (
            incident
            if type(incident) is IncidentIncident
            else IncidentIncident(**incident)
        )


class Postmortem(JsonSerializable):
    unique_id: UUID
    author: str
    status: str
    postmortem_data: str
    incidents: List[IncidentElement]
    author_name: str
    title: str
    download_status: int
    amazon_link: Optional[str]
    creation_date: Optional[datetime]

    # noinspection PyArgumentList
    def __init__(
        self,
        unique_id: UUID,
        author: str,
        status: str,
        postmortem_data: str,
        incidents: Union[List[IncidentElement], List[dict]],
        author_name: str,
        title: str,
        download_status: int,
        amazon_link: str,
        creation_date: datetime,
    ) -> None:
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)
        self.author = author
        self.status = status
        self.postmortem_data = postmortem_data
        self.incidents = (
            incidents
            if type(incidents) is list[IncidentElement]
            else [IncidentElement(**i) for i in incidents]
        )
        self.author_name = author_name
        self.title = title
        self.download_status = download_status
        self.amazon_link = amazon_link
        self.creation_date = (
            creation_date
            if type(creation_date) is datetime
            else datetime.fromisoformat(creation_date.replace("Z", "+00:00"))
        )
