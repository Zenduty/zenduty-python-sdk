from .maintenance import TeamMaintenanceClient
from .oncall.models import OnCall
from .postmortem import PostmortemClient
from .priorities import PriorityClient
from .roles import IncidentRole, IncidentRoleClient
from .sla import SLAClient
from .tags import TagClient
from .task_templates import TaskTemplateClient
from ..client import ZendutyClient, ZendutyClientRequestMethod
from ._models import Team, Member
from uuid import UUID
from .schedules import ScheduleClient
from .escalation_policies import EscalationPolicyClient
from .services import ServiceClient


class TeamsClient:
    def __init__(self, client: ZendutyClient):
        self._client = client

    def get_schedule_client(self, team: Team) -> ScheduleClient:
        """get schedule client for a team

        Args:
            team (Team): team for which schedule client is available

        Returns:
            ScheduleClient: client to interact with schedule objects
        """
        return ScheduleClient(self._client, team)

    def get_maintenance_client(self, team: Team) -> TeamMaintenanceClient:
        """get maintenanace client for a team

        Args:
            team (Team): team for which maintenance client is required.

        Returns:
            TeamMaintenanceClient: team maintenance client which is required.
        """
        return TeamMaintenanceClient(self._client, team)

    def get_postmortem_client(self, team: Team) -> PostmortemClient:
        return PostmortemClient(self._client, team)

    def get_priority_client(self, team: Team) -> PriorityClient:
        return PriorityClient(self._client, team)

    def get_incident_role_client(self, team: Team) -> IncidentRoleClient:
        return IncidentRoleClient(self._client, team)

    def get_sla_client(self, team: Team) -> SLAClient:
        return SLAClient(self._client, team)

    def get_tag_client(self, team: Team) -> TagClient:
        return TagClient(self._client, team)

    def get_task_template_client(self, team: Team) -> TaskTemplateClient:
        return TaskTemplateClient(self._client, team)

    def get_escalation_policy_client(self, team: Team) -> EscalationPolicyClient:
        return EscalationPolicyClient(self._client, team)

    def get_service_client(self, team: Team) -> ServiceClient:
        return ServiceClient(self._client, team)

    def create_team(self, name: str) -> Team:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/account/teams/",
            request_payload={"name": name},
            success_code=201,
        )
        return Team(**response)

    def list_teams(self) -> list[Team]:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/",
            success_code=200,
        )
        return [Team(**team) for team in response]

    def find_team_by_id(self, team_id: UUID) -> Team:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint=f"/api/account/teams/{str(team_id)}/",
            success_code=200,
        )
        return Team(**response)

    def update_team(self, team: Team) -> Team:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint=f"/api/account/teams/{str(team.unique_id)}/",
            request_payload={
                "name": team.name,
            },
            success_code=200,
        )
        return Team(**response)

    def delete_team(self, team: Team):
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint=f"/api/account/teams/{str(team.unique_id)}/",
            success_code=204,
        )

    def find_team_member(self, team: Team, member_unique_id: str) -> Member:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/members/%s/"
            % (str(team.unique_id), member_unique_id),
            success_code=200,
        )
        return Member(**response)

    def update_team_member_role(self, team: Team, member: Member, role: int) -> Member:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PATCH,
            endpoint=f"/api/account/teams/{str(team.unique_id)}/members/{str(member.unique_id)}/",
            request_payload={
                "role": role,
            },
            success_code=200,
        )
        return self.find_team_member(team, response["unique_id"])

    def add_team_member(self, team: Team, username: str) -> Member:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint=f"/api/account/teams/%s/members/" % str(team.unique_id),
            request_payload={"user": username},
            success_code=201,
        )
        return self.find_team_member(team, response["unique_id"])

    def delete_team_member(self, team: Team, member: Member):
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint="/api/account/teams/%s/members/%s/"
            % (str(team.unique_id), str(member.unique_id)),
            success_code=204,
        )

    def list_team_members(self, team: Team) -> list[Member]:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint=f"/api/account/teams/{str(team.unique_id)}/members/",
            success_code=200,
        )
        return [Member(**member) for member in response]

    def fetch_team_permissions(self, team: Team) -> list[str]:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint=f"/api/account/teams/{str(team.unique_id)}/permissions/",
            success_code=200,
        )
        return response.get("account_permissions", [])

    def get_all_oncall(self, team: Team) -> list[OnCall]:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint=f"/api/account/teams/{str(team.unique_id)}/oncall/",
            success_code=200,
        )
        return [OnCall(**oncall) for oncall in response]

    def update_team_permissions(self, team: Team, permissions: list[str]) -> list[str]:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint=f"/api/account/teams/{str(team.unique_id)}/permissions/",
            request_payload={
                "account_permissions": permissions,
            },
            success_code=200,
        )
        return response.get("account_permissions", [])
