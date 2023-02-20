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
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/priority/" % str(self._team.unique_id),
            success_code=200,
        )
        return [Priority(**r) for r in response]

    def get_priority_by_id(self, priority_id: UUID) -> Priority:
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
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint="/api/account/teams/%s/priority/%s/"
            % (str(self._team.unique_id), str(priority.unique_id)),
            request_payload=json.loads(priority.to_json()),
            success_code=200,
        )
        return Priority(**response)

    def delete_priority(self, priority: Priority):
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint="/api/account/teams/%s/priority/%s/"
            % (str(self._team.unique_id), str(priority.unique_id)),
            success_code=204,
        )
