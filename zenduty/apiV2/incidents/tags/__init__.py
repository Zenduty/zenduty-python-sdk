import json
from uuid import UUID

from ...client import ZendutyClient, ZendutyClientRequestMethod
from ..models import Incident
from .models import Tag


class IncidentTagClient:
    def __init__(self, client: ZendutyClient, incident: Incident):
        self._incident = incident
        self._client = client

    def get_all_tags(self) -> list[Tag]:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/incidents/%s/tags/" % self._incident.incident_number,
            success_code=200,
        )
        return [Tag(**r) for r in response]

    def get_tag_by_id(self, tag_id: UUID) -> Tag:
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
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint="/api/incidents/%d/tags/%s/"
            % (self._incident.incident_number, str(tag.unique_id)),
            success_code=204,
        )
