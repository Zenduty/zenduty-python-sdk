import json
from uuid import UUID
from ...client import ZendutyClient, ZendutyClientRequestMethod
from .._models import Team
from .models import Priority


class PriorityClient:
    def __init__(self, client: ZendutyClient, team: Team):
        self._client = client
        self._team = team

    def get_all_priorities(self) -> list[Priority]:
        """Get all the priorities for a the team

        Returns:
            list[Priority]: List of priorities
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/priority/" % str(self._team.unique_id),
            success_code=200,
        )
        return [Priority(**r) for r in response]

    def get_priority_by_id(self, priority_id: UUID) -> Priority:
        """Get a prioirity by ID

        Args:
            priority_id (UUID): priority id for fetching the priority.

        Returns:
            Priority: Priority object fetched
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/priority/%s/"
            % (str(self._team.unique_id), str(priority_id)),
            success_code=200,
        )
        return Priority(**response)

    def create_priority(
        self, name: str, description: str, color: str, **kwargs
    ) -> Priority:
        """Create a priority for a team

        Args:
            name (str): name of the priority
            description (str): description of the priority
            color (str): color of the priority

        Returns:
            Priority: Created Priority Object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/account/teams/%s/priority/" % str(self._team.unique_id),
            request_payload={
                "name": name,
                "description": description,
                "color": color,
            },
            success_code=201,
        )
        return Priority(**response)

    def update_priority(self, priority: Priority) -> Priority:
        """Update a priority object

        Args:
            priority (Priority): Priority object to update

        Returns:
            Priority: updated priority object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint="/api/account/teams/%s/priority/%s/"
            % (str(self._team.unique_id), str(priority.unique_id)),
            request_payload=json.loads(priority.to_json()),
            success_code=200,
        )
        return Priority(**response)

    def delete_priority(self, priority: Priority):
        """Delete a priority object

        Args:
            priority (Priority): deleted priority object
        """
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint="/api/account/teams/%s/priority/%s/"
            % (str(self._team.unique_id), str(priority.unique_id)),
            success_code=204,
        )
