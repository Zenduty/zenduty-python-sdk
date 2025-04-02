import json
import logging
from uuid import UUID
from datetime import datetime
from typing import List, Any, Union

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
        **kwargs
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
        if kwargs:
            logging.info(f'Received unexpected return values for {self.__class__.__name__}: {list(kwargs.keys())}')


class Payload:
    status: str
    severity: str
    project: str

    def __init__(self, status: str, severity: str, project: str, **kwargs) -> None:
        self.status = status
        self.severity = severity
        self.project = project
        if kwargs:
            logging.info(f'Received unexpected return values for {self.__class__.__name__}: {list(kwargs.keys())}')

    def to_json(self) -> str:
        return json.dumps(self.__dict__)


class URL:
    link_url: str
    link_text: str

    def __init__(self, link_url: str, link_text: str, **kwargs) -> None:
        self.link_url = link_url
        self.link_text = link_text
        if kwargs:
            logging.info(f'Received unexpected return values for {self.__class__.__name__}: {list(kwargs.keys())}')

    def to_json(self) -> str:
        return json.dumps(self.__dict__)


class Event(JsonSerializable):
    integration_object: IntegrationObject
    summary: str
    incident: None
    creation_date: datetime
    message: str
    integration: UUID
    suppressed: bool
    entity_id: str
    alert_type: int
    unique_id: str
    images: List[Any]
    notes: List[Any]
    payload: Payload
    urls: List[URL]
    incident_created: bool

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
        alert_type: int,
        unique_id: str,
        images: List[Any],
        notes: List[Any],
        urls: List[Union[URL, dict]],
        payload: Union[Payload, dict] = None,
        incident_created: bool = None,
        **kwargs
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
        self.alert_type = alert_type
        self.unique_id = unique_id
        self.images = images
        self.notes = notes
        self.payload = payload
        self.urls = urls
        self.incident_created = incident_created
        if kwargs:
            logging.info(f'Received unexpected return values for {self.__class__.__name__}: {list(kwargs.keys())}')
