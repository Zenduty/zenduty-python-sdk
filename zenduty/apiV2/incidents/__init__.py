import json
from uuid import UUID

from .notes import IncidentNoteClient
from .tags import IncidentTagClient
from ..client import ZendutyClient, ZendutyClientRequestMethod
from .models import Incident
from ..events.models import Event


class __IncidentItr__:
    """The incident list iterator implementation for paginated incidents"""

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
        """The constructor for an incident client

        Args:
            client (ZendutyClient): The zenduty client to connect to Zenduty APIs
        """
        self._client = client

    def get_note_client(self, incident: Incident) -> IncidentNoteClient:
        """Reutrns the Incident Notes client

        Args:
            incident (Incident): the incident object for which the notes client has to be fetched

        Returns:
            IncidentNoteClient: The IncidentNoteClient object is returned which can be used to perform various operations on incident notes.
        """
        return IncidentNoteClient(self._client, incident)

    def get_tags_client(self, incident: Incident) -> IncidentTagClient:
        """Reutrns the Incident Tags client

        Args:
            incident (Incident): the incident object for which the tags client has to be fetched

        Returns:
            IncidentTagClient: The IncidentTagClient object is returned which can be used to perform various operations on incident tags.
        """

        return IncidentTagClient(self._client, incident)

    def get_all_incidents(self) -> __IncidentItr__:
        """Returns a iterator for all the incidents

        Returns:
            __IncidentItr__: the iterator for incidents list
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/incidents/",
            success_code=200,
        )
        return __IncidentItr__(self._client, response["results"], response["next"])

    def get_incident_by_incident_number(self, incident_number: int) -> Incident:
        """Return a Incident by incident number

        Args:
            incident_number (int): the incident number for which to retrieve the incident

        Returns:
            Incident: The returned Incident object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/incidents/%d/" % incident_number,
            success_code=200,
        )
        return Incident(**response)

    def create_incident(
        self,
        summary: str,
        title: str,
        service: UUID,
        assigned_to: UUID,
        escalation_policy: UUID,
        sla: UUID,
        team_priority: UUID,
        status: int = 1,
        **kwargs
    ) -> Incident:
        """Create a new incident

        Args:
            summary (str): A string that represents the Incident object's summary
            status (int): An integer that represents the Incident object's status. 1 is triggered, 2 is acknowledged and 3 is resolved
            title (str): A string that represents the Incident object's title
            service (UUID): A system-generated string that represents the Service object's unique_id
            assigned_to (UUID): A system-generated string that represents the User object's username
            escalation_policy (UUID): A system-generated string that represents the Escalation Policy object's unique_id
            sla (UUID): A system-generated string that represents the SLA object's unique_id
            team_priority (UUID): A system-generated string that represents the Priority object's unique_id

        Returns:
            Incident: Incident object created
        """        
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
        """Updates the incident object attributes with the specified incident number

        Args:
            incident (Incident): Incident object with updated fields

        Returns:
            Incident: The updated incident object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint="/api/incidents/%d/" % incident.incident_number,
            request_payload=json.loads(incident.to_json()),
            success_code=200,
        )
        return Incident(**response)

    def get_alerts_for_incident(self, incident_number: int) -> list[Event]:
        """Get alerts for an incident

        Args:
            incident_number (int): The incident number for which to find the incident

        Returns:
            list[Event]: _description_
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/incidents/%d/alerts/" % incident_number,
            success_code=200,
        )
        return [Event(**r) for r in response]
