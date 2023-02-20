import json
from uuid import UUID
from ...client import ZendutyClient, ZendutyClientRequestMethod
from .._models import Team
from .models import Service
from datetime import datetime
from .integrations import IntegrationClient


class ServiceClient:
    def __init__(self, client: ZendutyClient, team: Team):
        self._client = client
        self._team = team

    def get_all_services(self) -> list[Service]:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/services/" % str(self._team.unique_id),
            success_code=200,
        )
        return [Service(**r) for r in response]

    def get_integration_client(self, svc: Service):
        return IntegrationClient(self._client, self._team, svc)

    def get_service_by_id(self, service_id: UUID) -> Service:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/services/%s/"
            % (str(self._team.unique_id), str(service_id)),
            success_code=200,
        )
        return Service(**response)

    def create_service(
        self,
        name: str,
        summary: str,
        description: str,
        escalation_policy: UUID,
        team: UUID,
        sla: UUID,
        team_priority: UUID,
        task_template: UUID,
        auto_resolve_timeout: int = 0,
        acknowledgement_timeout: int = 0,
        status: int = 1,
        under_maintenance: bool = False,
        collation: int = 0,
        collation_time: int = 0,
        **kwargs
    ) -> Service:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/account/teams/%s/services/" % str(self._team.unique_id),
            request_payload={
                "name": name,
                "summary": summary,
                "description": description,
                "auto_resolve_timeout": auto_resolve_timeout,
                "team_priority": team_priority,
                "task_template": task_template,
                "acknowledgement_timeout": acknowledgement_timeout,
                "status": status,
                "escalation_policy": escalation_policy,
                "team": team,
                "sla": sla,
                "under_maintenance": under_maintenance,
                "collation": collation,
                "collation_time": collation_time,
            },
            success_code=201,
        )
        return Service(**response)

    def update_service(self, service: Service) -> Service:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint="/api/account/teams/%s/services/%s/"
            % (str(self._team.unique_id), str(service.unique_id)),
            request_payload=json.loads(service.to_json()),
            success_code=200,
        )
        return Service(**response)

    def delete_service(self, service: Service):
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint="/api/account/teams/%s/services/%s/"
            % (str(self._team.unique_id), str(service.unique_id)),
            success_code=204,
        )
