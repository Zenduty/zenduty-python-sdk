from uuid import UUID
from datetime import datetime
from typing import List, Any
from ..serializer import serialize, JsonSerializable
import json


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
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)
        self.service = service if type(service) is not str else UUID(service)
        self.team = team if type(team) is not str else UUID(team)
        self.integration_key = integration_key
        self.is_enabled = is_enabled
        self.integration_type = integration_type


class IncidentAlert(JsonSerializable):
    integration_object: IntegrationObject
    summary: str
    incident: int
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
        incident: int,
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
        self.integration_object = (
            integration_object
            if isinstance(integration_object, IntegrationObject)
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


class EscalationPolicyObject(JsonSerializable):
    unique_id: UUID
    name: str

    def __init__(self, unique_id: UUID, name: str) -> None:
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)
        self.name = name

    def to_json(self):
        return json.dumps(self, default=serialize, sort_keys=True, indent=4)


class ServiceObject(JsonSerializable):
    name: str
    creation_date: datetime
    summary: str
    description: str
    unique_id: UUID
    auto_resolve_timeout: int
    created_by: str
    team_priority: UUID
    task_template: UUID
    acknowledgement_timeout: int
    status: int
    escalation_policy: UUID
    team: UUID
    sla: UUID
    collation_time: int
    collation: int
    under_maintenance: bool

    def __init__(
        self,
        name: str,
        creation_date: datetime,
        summary: str,
        description: str,
        unique_id: UUID,
        auto_resolve_timeout: int,
        created_by: str,
        team_priority: UUID,
        task_template: UUID,
        acknowledgement_timeout: int,
        status: int,
        escalation_policy: UUID,
        team: UUID,
        sla: UUID,
        collation_time: int,
        collation: int,
        under_maintenance: bool,
    ) -> None:
        self.name = name
        self.creation_date = (
            creation_date
            if type(creation_date) is datetime
            else datetime.fromisoformat(creation_date.replace("Z", "+00:00"))
        )
        self.summary = summary
        self.description = description
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)
        self.auto_resolve_timeout = auto_resolve_timeout
        self.created_by = created_by
        self.team_priority = (
            team_priority if type(team_priority) is not str else UUID(team_priority)
        )
        self.task_template = (
            task_template if type(task_template) is not str else UUID(task_template)
        )
        self.acknowledgement_timeout = acknowledgement_timeout
        self.status = status
        self.escalation_policy = (
            escalation_policy
            if type(escalation_policy) is not str
            else UUID(escalation_policy)
        )
        self.team = team if type(team) is not str else UUID(team)
        self.sla = sla if type(sla) is not str else UUID(sla)
        self.collation_time = collation_time
        self.collation = collation
        self.under_maintenance = under_maintenance


class SlaObject(JsonSerializable):
    unique_id: UUID
    name: str
    is_active: bool
    acknowledge_time: int
    resolve_time: int
    creation_date: datetime

    def __init__(
        self,
        unique_id: UUID,
        name: str,
        is_active: bool,
        acknowledge_time: int,
        resolve_time: int,
        creation_date: datetime,
    ) -> None:
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)
        self.name = name
        self.is_active = is_active
        self.acknowledge_time = acknowledge_time
        self.resolve_time = resolve_time
        self.creation_date = (
            creation_date
            if type(creation_date) is datetime
            else datetime.fromisoformat(creation_date.replace("Z", "+00:00"))
        )

    def to_json(self):
        return json.dumps(self, default=serialize, sort_keys=True, indent=4)


class TeamPriorityObject(JsonSerializable):
    unique_id: UUID
    name: str
    description: str
    color: str

    def __init__(
        self, unique_id: UUID, name: str, description: str, color: str
    ) -> None:
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)
        self.name = name
        self.description = description
        self.color = color

    def to_json(self):
        return json.dumps(self, default=serialize, sort_keys=True, indent=4)


class Incident(JsonSerializable):
    summary: str
    incident_number: int
    creation_date: datetime
    status: int
    unique_id: str
    service_object: ServiceObject
    title: str
    incident_key: str
    service: UUID
    urgency: int
    merged_with: None
    assigned_to: None
    escalation_policy: UUID
    escalation_policy_object: EscalationPolicyObject
    assigned_to_name: str
    resolved_date: None
    acknowledged_date: None
    context_window_start: None
    context_window_end: None
    tags: List[Any]
    sla: UUID
    sla_object: SlaObject
    team_priority: UUID
    team_priority_object: TeamPriorityObject

    def __init__(
        self,
        summary: str,
        incident_number: int,
        creation_date: datetime,
        status: int,
        unique_id: str,
        service_object: ServiceObject,
        title: str,
        incident_key: str,
        service: UUID,
        urgency: int,
        merged_with: None,
        assigned_to: None,
        escalation_policy: UUID,
        escalation_policy_object: EscalationPolicyObject,
        assigned_to_name: str,
        resolved_date: None,
        acknowledged_date: None,
        context_window_start: None,
        context_window_end: None,
        tags: List[Any],
        sla: UUID,
        sla_object: SlaObject,
        team_priority: UUID,
        team_priority_object: TeamPriorityObject,
    ) -> None:
        self.summary = summary
        self.incident_number = incident_number
        self.creation_date = (
            creation_date
            if type(creation_date) is datetime
            else datetime.fromisoformat(creation_date.replace("Z", "+00:00"))
        )
        self.status = status
        self.unique_id = unique_id
        self.service_object = (
            service_object
            if type(service_object) is not dict
            else ServiceObject(**service_object)
        )
        self.title = title
        self.incident_key = incident_key
        self.service = service if type(service) is not str else UUID(service)
        self.urgency = urgency
        self.merged_with = merged_with
        self.assigned_to = assigned_to
        self.escalation_policy = (
            escalation_policy
            if type(escalation_policy) is not str
            else UUID(escalation_policy)
        )
        self.escalation_policy_object = (
            escalation_policy_object
            if type(escalation_policy_object) is not dict
            else EscalationPolicyObject(**escalation_policy_object)
        )
        self.assigned_to_name = assigned_to_name
        self.resolved_date = resolved_date
        self.acknowledged_date = acknowledged_date
        self.context_window_start = context_window_start
        self.context_window_end = context_window_end
        self.tags = tags
        self.sla = sla if type(sla) is not str else UUID(sla)
        self.sla_object = (
            sla_object if type(sla_object) is not dict else SlaObject(**sla_object)
        )
        self.team_priority = (
            team_priority if type(team_priority) is not str else UUID(team_priority)
        )
        self.team_priority_object = (
            team_priority_object
            if type(team_priority_object) is not dict
            else TeamPriorityObject(**team_priority_object)
        )

    def to_json(self):
        return json.dumps(self, default=serialize, sort_keys=True, indent=4)
