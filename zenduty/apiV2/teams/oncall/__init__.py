
from ..models import Team
from .models import OnCallV2, OnCall
from ..escalation_policies.models import EscalationPolicy
from zenduty.apiV2.client import ZendutyClient, ZendutyClientRequestMethod
class OncallClient:
    def __init__(self, client: ZendutyClient, team: Team):
        self._client = client
        self._team = team

    
    def get_all_oncall(self) -> list[OnCall]:
        """Get all members on call for a team
        
        Returns:
            list[OnCall]: List of OnCall objects.
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint=f"/api/account/teams/{str(self._team.unique_id)}/oncall/",
            success_code=200,
        )
        return [OnCall(**oncall) for oncall in response]

    def get_team_oncall_v2(self, escalation_policy: EscalationPolicy) -> OnCallV2:
        """Get all members on call for a team

        Returns:
            list[OnCall]: List of OnCall objects.
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint=f"/api/v2/account/teams/{str(self._team.unique_id)}/escalation_policies/{str(escalation_policy.unique_id)}/oncall/",
        )
        return OnCallV2(**response[0])
    
    def list_team_oncall_v2(self)-> list[OnCallV2]:
        """Get all members on call for a team

        Returns:
            list[OnCall]: List of OnCall objects.
        """
         
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint=f"/api/v2/account/teams/{str(self._team.unique_id)}/oncall/",
        )
        return[ OnCallV2(**oncall) for oncall in response]
