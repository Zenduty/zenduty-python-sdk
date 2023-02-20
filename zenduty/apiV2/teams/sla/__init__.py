import json
from uuid import UUID
from ...client import ZendutyClient, ZendutyClientRequestMethod
from .._models import Team
from .models import SLA


class SLAClient:
    def __init__(self, client: ZendutyClient, team: Team):
        self._client = client
        self._team = team

    def get_all_slas(self) -> list[SLA]:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/sla/" % str(self._team.unique_id),
            success_code=200,
        )
        return [SLA(**r) for r in response]

    def get_sla_by_id(self, sla_id: UUID) -> SLA:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/sla/%s/"
            % (str(self._team.unique_id), str(sla_id)),
            success_code=200,
        )
        return SLA(**response)

    def create_sla(
        self,
        name: str,
        is_active: bool,
        acknowledge_time: int,
        resolve_time: int,
        **kwargs
    ) -> SLA:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/account/teams/%s/schedules/" % str(self._team.unique_id),
            request_payload={
                "name": name,
                "is_active": is_active,
                "acknowledge_time": acknowledge_time,
                "resolve_time": resolve_time,
                "escalations": kwargs.get("escalations", []),
            },
            success_code=201,
        )
        return SLA(**response)

    def update_schedule(self, sla: SLA) -> SLA:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint="/api/account/teams/%s/sla/%s/"
            % (str(self._team.unique_id), str(sla.unique_id)),
            request_payload=json.loads(sla.to_json()),
            success_code=200,
        )
        return SLA(**response)

    def delete_schedule(self, sla: SLA):
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint="/api/account/teams/%s/sla/%s/"
            % (str(self._team.unique_id), str(sla.unique_id)),
            success_code=204,
        )
