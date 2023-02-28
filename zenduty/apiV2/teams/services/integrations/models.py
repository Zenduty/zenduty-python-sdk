from uuid import UUID
from datetime import datetime
import json
from typing import Optional
from ....serializer import serialize, JsonSerializable

from datetime import datetime
from uuid import UUID
from typing import Optional, List, Any


class IntegrationObject:
    name: str
    creation_date: datetime
    summary: str
    unique_id: UUID
    service: UUID
    team: UUID
    integration_key: UUID
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
        integration_key: UUID,
        is_enabled: bool,
        integration_type: int,
    ) -> None:
        self.name = name
        self.creation_date = creation_date
        self.summary = summary
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)
        self.service = service if type(service) is not str else UUID(service)
        self.team = team if type(team) is not str else UUID(team)
        self.integration_key = (
            integration_key
            if type(integration_key) is not str
            else UUID(integration_key)
        )
        self.is_enabled = is_enabled
        self.integration_type = integration_type


class IntegrationAlert:
    integration_object: IntegrationObject
    summary: str
    incident: Optional[int]
    creation_date: datetime
    message: str
    integration: UUID
    suppressed: bool
    entity_id: str
    alert_type: int
    unique_id: str
    images: List[Any]
    urls: List[Any]
    notes: List[Any]

    def __init__(
        self,
        integration_object: IntegrationObject,
        summary: str,
        incident: Optional[int],
        creation_date: datetime,
        message: str,
        integration: UUID,
        suppressed: bool,
        entity_id: str,
        alert_type: int,
        unique_id: str,
        images: List[Any],
        urls: List[Any],
        notes: List[Any],
    ) -> None:
        self.integration_object = integration_object
        self.summary = summary
        self.incident = incident
        self.creation_date = creation_date
        self.message = message
        self.integration = (
            integration if type(integration) is not str else UUID(integration)
        )
        self.suppressed = suppressed
        self.entity_id = entity_id
        self.alert_type = alert_type
        self.unique_id = unique_id
        self.images = images
        self.urls = urls
        self.notes = notes


class ApplicationReference:
    name: str
    icon_url: str
    summary: str
    description: str
    unique_id: UUID
    availability_plan_id: int
    setup_instructions: str
    extension: str
    application_type: int
    categories: str
    documentation_link: str

    def __init__(
        self,
        name: str,
        icon_url: str,
        summary: str,
        description: str,
        unique_id: UUID,
        availability_plan_id: int,
        setup_instructions: str,
        extension: str,
        application_type: int,
        categories: str,
        documentation_link: str,
    ) -> None:
        self.name = name
        self.icon_url = icon_url
        self.summary = summary
        self.description = description
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)
        self.availability_plan_id = availability_plan_id
        self.setup_instructions = setup_instructions
        self.extension = extension
        self.application_type = application_type
        self.categories = categories
        self.documentation_link = documentation_link

    def to_json(self):
        return json.dumps(self, default=serialize, sort_keys=True, indent=4)


class Integration(JsonSerializable):
    name: str
    description: str
    creation_date: datetime
    summary: str
    unique_id: UUID
    service: UUID
    application: UUID
    application_reference: ApplicationReference
    integration_key: UUID
    created_by: str
    is_enabled: bool
    create_incidents_for: int
    integration_type: int
    default_urgency: int
    webhook_url: str

    def __init__(
        self,
        name: str,
        creation_date: datetime,
        summary: str,
        unique_id: UUID,
        service: UUID,
        application: UUID,
        application_reference: ApplicationReference,
        integration_key: UUID,
        created_by: str,
        is_enabled: bool,
        create_incidents_for: int,
        integration_type: int,
        default_urgency: int,
        webhook_url: str,
        description: Optional[str] = "",
        **kwargs
    ) -> None:
        self.name = name
        self.description = description
        self.creation_date = creation_date
        self.summary = summary
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)
        self.service = service if type(service) is not str else UUID(service)
        self.application = (
            application if type(application) is not str else UUID(application)
        )
        self.application_reference = (
            application_reference
            if type(application_reference) is not list[dict]
            else [ApplicationReference(**ar) for ar in application_reference]
        )
        self.integration_key = (
            integration_key
            if type(integration_key) is not str
            else UUID(integration_key)
        )
        self.created_by = created_by
        self.is_enabled = is_enabled
        self.create_incidents_for = create_incidents_for
        self.integration_type = integration_type
        self.default_urgency = default_urgency
        self.webhook_url = webhook_url
        if kwargs.get("auto_resolve_timeout", None) is not None:
            self.auto_resolve_timeout = kwargs.get("auto_resolve_timeout")

    def to_json(self):
        return json.dumps(self, default=serialize, sort_keys=True, indent=4)
