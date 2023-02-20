from datetime import datetime
from uuid import UUID
from typing import List, Any

from zenduty.apiV2.serializer import JsonSerializable


class IntegrationObject(JsonSerializable):
    name: str
    creation_date: datetime
    summary: str
    unique_id: UUID
    service: UUID
    team: UUID
    integration_key: str
    is_enabled: bool
    integration_type: int

    def __init__(
        self,
        name: str,
        creation_date: datetime,
        summary: str,
        unique_id: UUID,
        service: UUID,
        team: UUID,
        integration_key: str,
        is_enabled: bool,
        integration_type: int,
    ) -> None:
        self.name = name
        self.creation_date = (
            creation_date
            if type(creation_date) is datetime
            else datetime.fromisoformat(creation_date.replace("Z", "+00:00"))
        )
        self.summary = summary
        self.unique_id = unique_id if isinstance(unique_id, UUID) else UUID(unique_id)
        self.service = service if isinstance(unique_id, UUID) else UUID(service)
        self.team = team if isinstance(unique_id, UUID) else UUID(team)
        self.integration_key = integration_key
        self.is_enabled = is_enabled
        self.integration_type = integration_type


class Event(JsonSerializable):
    integration_object: IntegrationObject
    summary: str
    incident: None
    creation_date: datetime
    message: str
    integration: UUID
    suppressed: bool
    entity_id: str
    payload: str
    alert_type: int
    unique_id: str
    images: List[Any]
    urls: List[Any]
    notes: List[Any]

    def __init__(
        self,
        integration_object: IntegrationObject,
        summary: str,
        incident: None,
        creation_date: datetime,
        message: str,
        integration: UUID,
        suppressed: bool,
        entity_id: str,
        payload: str,
        alert_type: int,
        unique_id: str,
        images: List[Any],
        urls: List[Any],
        notes: List[Any],
    ) -> None:
        self.integration_object = (
            integration_object
            if type(integration_object) is IntegrationObject
            else IntegrationObject(**integration_object)
        )
        self.summary = summary
        self.incident = incident
        self.creation_date = (
            creation_date
            if type(creation_date) is datetime
            else datetime.fromisoformat(creation_date.replace("Z", "+00:00"))
        )
        self.message = message
        self.integration = str(integration)
        self.suppressed = suppressed
        self.entity_id = entity_id
        self.payload = payload
        self.alert_type = alert_type
        self.unique_id = unique_id
        self.images = images
        self.urls = urls
        self.notes = notes
