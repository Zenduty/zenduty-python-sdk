import json
from uuid import UUID
from ....client import ZendutyClient, ZendutyClientRequestMethod
from ..._models import Team
from ..models import Service
from .models import Integration, IntegrationAlert
from datetime import datetime


class __alertsItr__:
    def __init__(self, client: ZendutyClient, results: list, next: str, pos: int = 0):
        self._client = client
        self.results = results
        self.next = next
        self.pos = pos

    def __iter__(self):
        return self

    def __next__(self):
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
        return IntegrationAlert(**v)


class IntegrationClient:
    def __init__(self, client: ZendutyClient, team: Team, svc: Service):
        self._client = client
        self._team = team
        self._svc = svc

    def get_all_integrations(self) -> list[Integration]:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/services/%s/integrations/"
            % (str(self._team.unique_id), str(self._svc.unique_id)),
            success_code=200,
        )
        return [Integration(**r) for r in response]

    def get_intg_by_id(self, intg: UUID) -> Integration:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/services/%s/integrations/%s/"
            % (str(self._team.unique_id), str(self._svc.unique_id), str(intg)),
            success_code=200,
        )
        return Integration(**response)

    def get_intg_alerts_iter(self, intg: Integration) -> list[IntegrationAlert]:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/services/%s/integrations/%s/alerts"
            % (
                str(self._team.unique_id),
                str(self._svc.unique_id),
                str(intg.unique_id),
            ),
            success_code=200,
        )
        return __alertsItr__(self._client, response["results"], response["next"])

    def create_intg(
        self,
        name: str,
        summary: str,
        application: UUID,
        escalation_policy: UUID,
        default_urgency: int = 1,
        integration_type: int = 0,
        create_incidents_for: int = 1,
        is_enabled: bool = True,
        **kwargs
    ) -> Integration:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/account/teams/%s/services/%s/integrations/"
            % (str(self._team.unique_id), str(self._svc.unique_id)),
            request_payload={
                "name": name,
                "summary": summary,
                "escalation_policy": escalation_policy,
                "application": application,
                "default_urgency": default_urgency,
                "integration_type": integration_type,
                "create_incidents_for": create_incidents_for,
                "is_enabled": is_enabled,
                "team_priority": None,
                "sla": None,
            },
            success_code=201,
        )
        return self.get_intg_by_id(response["unique_id"])

    def update_intg(self, intg: Integration) -> Integration:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint="/api/account/teams/%s/services/%s/integrations/%s/"
            % (
                str(self._team.unique_id),
                str(self._svc.unique_id),
                str(intg.unique_id),
            ),
            request_payload=json.loads(intg.to_json()),
            success_code=200,
        )
        return Integration(**response)

    def delete_intg(self, intg: Integration):
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint="/api/account/teams/%s/services/%s/integrations/%s"
            % (
                str(self._team.unique_id),
                str(self._svc.unique_id),
                str(intg.unique_id),
            ),
            success_code=204,
        )
