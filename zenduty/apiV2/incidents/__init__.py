from uuid import UUID
from .models import Incident
from .tags import IncidentTagClient
from .notes import IncidentNoteClient
from zenduty.apiV2.events import Event
from zenduty.apiV2.client import ZendutyClient, ZendutyClientRequestMethod

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
            Incident_id (str): the incident  object for which the notes client has to be fetched

        Returns:
            IncidentNoteClient: The IncidentNoteClient object is returned which can be used to perform various operations on incident notes.
        """
        return IncidentNoteClient(self._client, incident)

    def get_tags_client(self, incident: Incident) -> IncidentTagClient:
        """Reutrns the Incident Tags client

        Args:
            Incident_id (str): the incident  for which the tags client has to be fetched

        Returns:
            IncidentTagClient: The IncidentTagClient object is returned which can be used to perform various operations on incident tags.
        """
        return IncidentTagClient(self._client, incident)

    def get_all_incidents(
        self,
        page=1,
        page_size=10,
        all_teams=1,
        escalation_policy_ids=None,
        from_date=None,
        postmortem_filter=-1,
        priority_ids=None,
        priority_name=None,
        service_ids=None,
        sla_ids=None,
        status=1,
        tag_ids=None,
        team_ids=None,
        to_date=None,
        user_ids=None,
    ) -> list[Incident]:
        """Returns the list of incidents with optional filters"""
        payload = {
            "status": status,
            "all_teams": all_teams,
            "postmortem_filter": postmortem_filter,
            "page": page,
            "page_size": page_size,
        }
        if escalation_policy_ids is not None:
            payload["escalation_policy_ids"] = escalation_policy_ids
        if from_date:
            payload["from_date"] = from_date
        if priority_ids is not None:
            payload["priority_ids"] = priority_ids
        if priority_name:
            payload["priority_name"] = priority_name
        if service_ids is not None:
            payload["service_ids"] = service_ids
        if sla_ids is not None:
            payload["sla_ids"] = sla_ids
        if tag_ids is not None:
            payload["tag_ids"] = tag_ids
        if team_ids is not None:
            payload["team_ids"] = team_ids
        if to_date:
            payload["to_date"] = to_date
        if user_ids is not None:
            payload["user_ids"] = user_ids

        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/incidents/filter/?page=%s&page_size=%s" % (page, page_size),
            request_payload=payload,
            success_code=200,
        )
        for incident in response.get("results", []):
            incident['summary'] = ""
            incident['incident_key'] = ""
            incident['service'] = None
            incident['urgency'] = 0
            incident['merged_with'] = None
            incident['escalation_policy'] = None
            incident['escalation_policy_object'] = None
            incident['context_window_start'] = None
            incident['context_window_end'] = None
            incident['team_priority'] = None
            incident['parent_incident'] = None
            incident['postmortem_assignee'] = None
            incident['service_object'] = None

        return [Incident(**incident) for incident in response.get("results", [])]

    def get_incident_by_unique_id_or_incident_number(self, incident_id: str) -> Incident:
        """Return a Incident by its unique_id

        Args:
            incident_id (str): the incident number or incident unique id for which to retrieve the incident

        Returns:
            Incident: The returned Incident object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/incidents/%s/" % incident_id,
            success_code=200,
        )
        return Incident(**response)

    def create_incident(self, title: str, service: UUID, summary: str = None, escalation_policy: UUID = None, assigned_to: str = None,  sla: str = None, team_priority: str = None) -> Incident:
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
        request_payload={"title": title, "service": (service)}
        if summary:
            request_payload["summary"] = summary
        if assigned_to:
            request_payload["assigned_to"] = assigned_to
        if escalation_policy:
            request_payload["escalation_policy"] = escalation_policy
        if sla:
            request_payload["sla"] = sla
        if team_priority:
            request_payload["team_priority"] = team_priority
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/incidents/",
            request_payload=request_payload,
            success_code=201,
        )
        return Incident(**response)

    def update_incident(
        self,
        incident_id: Incident,
        service: UUID,
        title: str = None,
        summary: str = None,
        status: int = None,
    ) -> Incident:
        """Updates the incident object attributes with the specified incident number. Uses existing values if new ones are not provided.

        Args:
            incident_id (str): The incident number or incident unique id of the incident to update.
            title (str, optional): New title for the incident. Defaults to None.
            summary (str, optional): New summary for the incident. Defaults to None.
            status (int, optional): New status for the incident. Defaults to None.

        Returns:
            Incident: The updated incident object.
        """
        current_incident = self.get_incident_by_unique_id_or_incident_number(incident_id)

        if title is None:
            title = current_incident.title
        if summary is None:
            summary = current_incident.summary
        if status is None:
            status = current_incident.status

        request_payload = {"title": title, "summary": summary, "status": status, "service": service}

        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint=f"/api/incidents/{incident_id}/",
            request_payload=request_payload,
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
        return [Event(**r) for r in response["results"]]
