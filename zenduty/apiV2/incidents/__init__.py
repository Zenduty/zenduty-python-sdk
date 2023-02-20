import json
from uuid import UUID

from .notes import IncidentNoteClient
from .tags import IncidentTagClient
from ..client import ZendutyClient, ZendutyClientRequestMethod
from .models import Incident
from ..events.models import Event


class IncidentClient:
    def __init__(self, client: ZendutyClient):
        self._client = client

    def get_note_client(self, incident: Incident) -> IncidentNoteClient:
        return IncidentNoteClient(self._client, incident)

    def get_tags_client(self, incident: Incident) -> IncidentTagClient:
        return IncidentTagClient(self._client, incident)

    def get_all_incidents(self) -> list[Incident]:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/incidents/",
            success_code=200,
        )
        return [Incident(**r) for r in response]

    def get_incident_by_incident_number(self, incident_number: int) -> Incident:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/incidents/%d/" % incident_number,
            success_code=200,
        )
        return Incident(**response)

    def create_incident(
        self,
        summary: str,
        status: str,
        title: str,
        service: UUID,
        assigned_to: UUID,
        escalation_policy: UUID,
        sla: UUID,
        team_priority: UUID,
    ) -> Incident:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/incidents/",
            request_payload={
                "summary": summary,
                "status": status,
                "title": title,
                "service": str(service),
                "assigned_to": str(assigned_to),
                "escalation_policy": str(escalation_policy),
                "sla": str(sla),
                "team_priority": str(team_priority),
            },
            success_code=201,
        )
        return Incident(**response)

    def update_incident(self, incident: Incident) -> Incident:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint="/api/incidents/%d/" % incident.incident_number,
            request_payload=json.loads(incident.to_json()),
            success_code=200,
        )
        return Incident(**response)

    def get_alerts_for_incident(self, incident_number: int) -> list[Event]:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/incidents/%d/alerts/" % incident_number,
            success_code=200,
        )
        return [Event(**r) for r in response]
