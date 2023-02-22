import json
from ...client import ZendutyClient, ZendutyClientRequestMethod
from ..models import Incident
from .models import IncidentNote


class __IncidentNoteItr__:
    def __init__(self, client: ZendutyClient, results: list, next: str, pos: int = 0):
        self._client = client
        self.results = results
        self.next = next
        self.pos = pos

    def __iter__(self):
        return self

    def __next__(self) -> IncidentNote:
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
        return IncidentNote(**v)


class IncidentNoteClient:
    def __init__(self, client: ZendutyClient, incident: Incident):
        """Constructor for IncidentNote

        Args:
            client (ZendutyClient): the zenduty client to connect to the Zenduty API
            incident (Incident): incident object for which the incident note client is required.
        """        
        self._incident = incident
        self._client = client

    def get_all_incident_notes(self) -> __IncidentNoteItr__:
        """Get all incident notes

        Returns:
            __IncidentNoteItr__: Incident notes interator object.
        """        
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/incidents/%s/note/" % self._incident.incident_number,
            success_code=200,
        )

        return __IncidentNoteItr__(self._client, response["results"], response["next"])

    def get_incident_note_by_id(self, incident_note_id: str) -> IncidentNote:
        """Get incident note by id of the note

        Args:
            incident_note_id (str): The id of the incident note

        Returns:
            IncidentNote: The incident note object
        """        
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/incidents/%d/note/%s/"
            % (self._incident.incident_number, incident_note_id),
            success_code=200,
        )
        return IncidentNote(**response)

    def create_incident_note(
        self,
        note: str,
    ) -> IncidentNote:
        """create a incident note

        Args:
            note (str): the note string

        Returns:
            IncidentNote: The created incident note object.
        """    
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/incidents/%d/note/" % self._incident.incident_number,
            request_payload={
                "note": note,
            },
            success_code=201,
        )
        return IncidentNote(**response)

    def update_incident_note(self, note: IncidentNote) -> IncidentNote:
        """Update a incident note object with given changes identified by unique identifier

        Args:
            note (IncidentNote): the incident note object to update

        Returns:
            IncidentNote: IncidentNote object
        """        
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint="/api/incidents/%d/note/%s/"
            % (self._incident.incident_number, note.unique_id),
            request_payload=json.loads(note.to_json()),
            success_code=200,
        )
        return IncidentNote(**response)

    def delete_incident_note(self, note: IncidentNote) -> None:
        """Delete a incident note object

        Args:
            note (IncidentNote): incident note object to delete
        """        
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint="/api/incidents/%d/note/%s/"
            % (self._incident.incident_number, note.unique_id),
            success_code=204,
        )
