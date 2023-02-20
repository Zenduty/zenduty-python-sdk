import json
from uuid import UUID
from ...client import ZendutyClient, ZendutyClientRequestMethod
from .._models import Team
from .models import IncidentRole


class IncidentRoleClient:
    def __init__(self, client: ZendutyClient, team: Team):
        self._client = client
        self._team = team

    def get_all_roles(self) -> list[IncidentRole]:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/roles/" % str(self._team.unique_id),
            success_code=200,
        )
        return [IncidentRole(**r) for r in response]

    def get_incident_role_by_id(self, role_id: UUID) -> IncidentRole:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/roles/%s/"
            % (str(self._team.unique_id), str(role_id)),
            success_code=200,
        )
        return IncidentRole(**response)

    def create_incident_role(
        self, title: str, description: str, rank: int = 1, **kwargs
    ) -> IncidentRole:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/account/teams/%s/services/" % str(self._team.unique_id),
            request_payload={
                "description": description,
                "title": title,
                "rank": rank,
            },
            success_code=201,
        )
        return IncidentRole(**response)

    def update_incident_role(self, role: IncidentRole) -> IncidentRole:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint="/api/account/teams/%s/roles/%s/"
            % (str(self._team.unique_id), str(role.unique_id)),
            request_payload=json.loads(role.to_json()),
            success_code=200,
        )
        return IncidentRole(**response)

    def delete_incident_role(self, role: IncidentRole):
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint="/api/account/teams/%s/roles/%s/"
            % (str(self._team.unique_id), str(role.unique_id)),
            success_code=204,
        )
