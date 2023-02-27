import json
from uuid import UUID

from ...client import ZendutyClient, ZendutyClientRequestMethod
from ..models import Incident
from .models import Tag


class IncidentTagClient:
    def __init__(self, client: ZendutyClient, incident: Incident):
        """Constructor for IncidentTagClient

        Args:
            client (ZendutyClient): The zenduty client to use
            incident (Incident): incident object on which the operation is to be performed
        """
        self._incident = incident
        self._client = client

    def get_all_tags(self) -> list[Tag]:
        """Lists all tags on the incident

        Returns:
            list[Tag]: List of all tags on the incident
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/incidents/%s/tags/" % self._incident.incident_number,
            success_code=200,
        )
        return [Tag(**r) for r in response]

    def get_tag_by_id(self, tag_id: UUID) -> Tag:
        """Returns a Tag object for a given tag unique identifier

        Args:
            tag_id (UUID): unique identifier for the tag

        Returns:
            Tag: The Tag object for the given tag identifier
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/incidents/%d/tags/%s/"
            % (self._incident.incident_number, str(tag_id)),
            success_code=200,
        )
        return Tag(**response)

    def create_tag(
        self,
        team_tag: UUID,
    ) -> Tag:
        """Creates a tag on the incident

        Args:
            team_tag (UUID): Team tag UUID you want to associate with the incident tag

        Returns:
            Tag: The created tag object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/incidents/%d/tags/" % self._incident.incident_number,
            request_payload={
                "team_tag": team_tag,
            },
            success_code=201,
        )
        return Tag(**response)

    # def update_incident_note(self, note: Tag) -> Tag:
    #     response = self._client.execute(
    #         method=ZendutyClientRequestMethod.PUT,
    #         endpoint="/api/incidents/%d/tags/%s/"
    #         % (self._incident.incident_number, note.unique_id),
    #         request_payload=json.loads(note.to_json()),
    #         success_code=200,
    #     )
    #     return Tag(**response)

    def delete_tag(self, tag: Tag) -> None:
        """Delete a specific tag

        Args:
            tag (Tag): The tag object to be deleted
        """
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint="/api/incidents/%d/tags/%s/"
            % (self._incident.incident_number, str(tag.unique_id)),
            success_code=204,
        )
