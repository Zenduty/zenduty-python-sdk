import json
from uuid import UUID
from ...client import ZendutyClient, ZendutyClientRequestMethod
from .._models import Team
from .models import EscalationPolicy


class EscalationPolicyClient:
    def __init__(self, client: ZendutyClient, team: Team):
        self._client = client
        self._team = team

    def get_all_policies(self) -> list[EscalationPolicy]:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/escalation_policies/"
            % str(self._team.unique_id),
            success_code=200,
        )
        return [EscalationPolicy(**r) for r in response]

    def get_esp_by_id(self, esp_id: UUID):
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/escalation_policies/%s/"
            % (str(self._team.unique_id), str(esp_id)),
            success_code=200,
        )
        return EscalationPolicy(**response)

    def create_esp(
        self, name: str, description: str, summary: str, rules: list[dict]
    ) -> EscalationPolicy:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/account/teams/%s/escalation_policies/"
            % str(self._team.unique_id),
            request_payload={
                "name": name,
                "summary": summary,
                "description": description,
                "rules": rules,
            },
            success_code=201,
        )
        return EscalationPolicy(**response)

    def update_esp(self, esp: EscalationPolicy) -> EscalationPolicy:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint="/api/account/teams/%s/escalation_policies/%s/"
            % (str(self._team.unique_id), str(esp.unique_id)),
            request_payload=json.loads(esp.to_json()),
            success_code=200,
        )
        return EscalationPolicy(**response)

    def delete_esp(self, esp: EscalationPolicy):
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint="/api/account/teams/%s/escalation_policies/%s/"
            % (str(self._team.unique_id), str(esp.unique_id)),
            success_code=204,
        )
