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
        """Get all the incident roles in a team

        Returns:
            list[IncidentRole]: List of all the incident roles
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/roles/" % str(self._team.unique_id),
            success_code=200,
        )
        return [IncidentRole(**r) for r in response]

    def get_incident_role_by_id(self, role_id: UUID) -> IncidentRole:
        """Get a incident role by ID

        Args:
            role_id (UUID): role id for the incident role

        Returns:
            IncidentRole: Incident role object
        """
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
        """Create a incident role by title, description, rank

        Args:
            title (str): An arbitary string that represents the Incident Role object's title
            description (str): An arbitary string that represents the Incident Role object's description
            rank (int, optional): An integer that represents the Incident Role object's rank. Defaults to 1.

        Returns:
            IncidentRole: Created incident role
        """
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
        """Update the incident role

        Args:
            role (IncidentRole): Incident role to update

        Returns:
            IncidentRole: Updated incident role
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint="/api/account/teams/%s/roles/%s/"
            % (str(self._team.unique_id), str(role.unique_id)),
            request_payload=json.loads(role.to_json()),
            success_code=200,
        )
        return IncidentRole(**response)

    def delete_incident_role(self, role: IncidentRole):
        """Delete a incident role

        Args:
            role (IncidentRole): Incident role to delete
        """
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint="/api/account/teams/%s/roles/%s/"
            % (str(self._team.unique_id), str(role.unique_id)),
            success_code=204,
        )
