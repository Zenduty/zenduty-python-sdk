import json
from uuid import UUID

from .notes import IncidentNoteClient
from .tags import IncidentTagClient
from ..client import ZendutyClient, ZendutyClientRequestMethod
from .models import Incident
from ..events.models import Event

class __IncidentItr__:
    def __init__(self, client: ZendutyClient, results: list, next: str, pos: int = 0):
        self._client = client
        self.results = results
        self.next = next
        self.pos = pos

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.results) == self.pos:
            if self.next is None:
                raise StopIteration
            val = 0
            for _ in range(0, 3):
                val = self.next.find("/", val + 1)
            response = self._client.execute(
                method=ZendutyClientRequestMethod.GET,
                endpoint=self.next[val:],
                success_code=200,
            )
            self.next = response["next"]
            self.pos = 0
            self.results = response["results"]
        v = self.results[self.pos]
        self.pos += 1
        return Incident(**v)



class IncidentClient:
    def __init__(self, client: ZendutyClient):
        self._client = client

    def get_note_client(self, incident: Incident) -> IncidentNoteClient:
        return IncidentNoteClient(self._client, incident)

    def get_tags_client(self, incident: Incident) -> IncidentTagClient:
        return IncidentTagClient(self._client, incident)

    def get_all_incidents(self) -> __IncidentItr__:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/incidents/",
            success_code=200,
        )
        return __IncidentItr__(self._client, response["results"], response["next"])

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
        **kwargs
    ) -> Incident:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/incidents/",
            request_payload={
                "summary": summary,
                "status": status,
                "title": title,
                "service": (service),
                "assigned_to": (assigned_to),
                "escalation_policy": (escalation_policy),
                "sla": (sla),
                "team_priority": (team_priority),
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
