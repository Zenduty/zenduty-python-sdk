import json
from uuid import UUID
from ...client import ZendutyClient, ZendutyClientRequestMethod
from .._models import Team
from .models import Postmortem


class PostmortemClient:
    def __init__(self, client: ZendutyClient, team: Team):
        self._client = client
        self._team = team

    def get_all_postmortem(self) -> list[Postmortem]:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/postmortem/" % str(self._team.unique_id),
            success_code=200,
        )
        return [Postmortem(**r) for r in response]

    def get_postmortem_by_id(self, postmortem_id: UUID) -> Postmortem:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/postmortem/%s/"
            % (str(self._team.unique_id), str(postmortem_id)),
            success_code=200,
        )
        return Postmortem(**response)

    def create_postmortem(
        self,
        author: str,
        status: str,
        postmortem_data: str,
        incidents: list[str],
        title: str,
        download_status: int = 0,
        **kwargs
    ) -> Postmortem:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/account/teams/%s/postmortem/" % str(self._team.unique_id),
            request_payload={
                "author": author,
                "status": status,
                "postmortem_data": postmortem_data,
                "incidents": [{"incident": i} for i in incidents],
                "title": title,
                "download_status": download_status,
            },
            success_code=201,
        )
        return self.get_postmortem_by_id(UUID(response["unique_id"]))

    def update_postmortem(self, postmortem: Postmortem) -> Postmortem:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint="/api/account/teams/%s/postmortem/%s/"
            % (str(self._team.unique_id), str(postmortem.unique_id)),
            request_payload=json.loads(postmortem.to_json()),
            success_code=200,
        )
        return self.get_postmortem_by_id(UUID(response["unique_id"]))

    def delete_postmortem(self, postmortem: Postmortem):
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint="/api/account/teams/%s/postmortem/%s/"
            % (str(self._team.unique_id), str(postmortem.unique_id)),
            success_code=204,
        )
