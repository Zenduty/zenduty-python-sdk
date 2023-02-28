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
        """get postmortem client for a team

        Args:
            team (Team): team for which postmortem client is required

        Returns:
            PostmortemClient: postmortem client
        """
        return PostmortemClient(self._client, team)

    def get_priority_client(self, team: Team) -> PriorityClient:
        """get priority client for a team

        Args:
            team (Team): team for which priority client is required.

        Returns:
            PriorityClient: priority client
        """
        return PriorityClient(self._client, team)

    def get_incident_role_client(self, team: Team) -> IncidentRoleClient:
        """get incident role client

        Args:
            team (Team): team for which incident role client is required

        Returns:
            IncidentRoleClient: incident role client object for the team.
        """
        return IncidentRoleClient(self._client, team)

    def get_sla_client(self, team: Team) -> SLAClient:
        """get SLA client for a team

        Args:
            team (Team): team for which SLA client is required.

        Returns:
            SLAClient: The sla client object
        """
        return SLAClient(self._client, team)

    def get_tag_client(self, team: Team) -> TagClient:
        """get tag client for a team

        Args:
            team (Team): team for which tag client is required

        Returns:
            TagClient: the tag client object
        """
        return TagClient(self._client, team)

    def get_task_template_client(self, team: Team) -> TaskTemplateClient:
        """get task template client for a team

        Args:
            team (Team): team for which task template client is required

        Returns:
            TaskTemplateClient: the task template client object
        """
        return TaskTemplateClient(self._client, team)

    def get_escalation_policy_client(self, team: Team) -> EscalationPolicyClient:
        """get escalation policy client for a team

        Args:
            team (Team): team for which escalation policy client is required

        Returns:
            EscalationPolicyClient: the escalation policy client
        """
        return EscalationPolicyClient(self._client, team)

    def get_service_client(self, team: Team) -> ServiceClient:
        """get service client for a team

        Args:
            team (Team): team for which services client is required

        Returns:
            ServiceClient: the service client
        """
        return ServiceClient(self._client, team)

    def create_team(self, name: str) -> Team:
        """create a team

        Args:
            name (str): name of the team

        Returns:
            Team: The created team object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/account/teams/",
            request_payload={"name": name},
            success_code=201,
        )
        return Team(**response)

    def list_teams(self) -> list[Team]:
        """Lists all the teams in the account

        Returns:
            list[Team]: List of all the teams
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/",
            success_code=200,
        )
        return [Team(**team) for team in response]

    def find_team_by_id(self, team_id: UUID) -> Team:
        """Find a team by the unique id of team

        Args:
            team_id (UUID): team id for which Team object has to be returned

        Returns:
            Team: The team object required.
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint=f"/api/account/teams/{str(team_id)}/",
            success_code=200,
        )
        return Team(**response)

    def update_team(self, team: Team) -> Team:
        """The team that has to be updated

        Args:
            team (Team): team to be updated with the pass fields

        Returns:
            Team: The updated teams object
        """
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
        """Delete a team object

        Args:
            team (Team): The team object that has to be deleted.
        """
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint=f"/api/account/teams/{str(team.unique_id)}/",
            success_code=204,
        )

    def find_team_member(self, team: Team, member_unique_id: str) -> Member:
        """Find a team member

        Args:
            team (Team): team object that has to be searched against.
            member_unique_id (str): unique id of the member.

        Returns:
            Member: Member object.
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/members/%s/"
            % (str(team.unique_id), member_unique_id),
            success_code=200,
        )
        return Member(**response)

    def update_team_member_role(self, team: Team, member_id: UUID, role: int) -> Member:
        """Makes updates to the member object's roles.

        Args:
            team (Team): _description_
            member_id (UUID): _description_
            role (int): An integer that represents the Team Member object's role. 1 is manager and 2 is user

        Returns:
            Member: The member object.
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PATCH,
            endpoint=f"/api/account/teams/{str(team.unique_id)}/members/{str(member_id)}/",
            request_payload={
                "role": role,
            },
            success_code=200,
        )
        return self.find_team_member(team, response["unique_id"])

    def add_team_member(self, team: Team, username: str) -> Member:
        """Add a memeber to a team by username of the user.

        Args:
            team (Team): The team object to which the memeber has to be added.
            username (str): Username of the memeber.

        Returns:
            Member: The created memeber.
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint=f"/api/account/teams/%s/members/" % str(team.unique_id),
            request_payload={"user": username},
            success_code=201,
        )
        return self.find_team_member(team, response["unique_id"])

    def delete_team_member(self, team: Team, member_id: UUID):
        """Delete a team membet

        Args:
            team (Team): Team to which a team member has to be removed from
            member_id (UUID): member id for the team member who has to be removed
        """
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint="/api/account/teams/%s/members/%s/"
            % (str(team.unique_id), str(member_id)),
            success_code=204,
        )

    def list_team_members(self, team: Team) -> list[Member]:
        """List members of a team

        Args:
            team (Team): team for which team members has to be listed.

        Returns:
            list[Member]: List of members
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint=f"/api/account/teams/{str(team.unique_id)}/members/",
            success_code=200,
        )
        return [Member(**member) for member in response]

    def fetch_team_permissions(self, team: Team) -> list[str]:
        """Fetch the permissions of a team

        Args:
            team (Team): The team object for which fetch the permissions

        Returns:
            list[str]: List of permissions
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint=f"/api/account/teams/{str(team.unique_id)}/permissions/",
            success_code=200,
        )
        return response.get("account_permissions", [])

    def get_all_oncall(self, team: Team) -> list[OnCall]:
        """Get all members on call for a team

        Args:
            team (Team): Team for which to list the team members

        Returns:
            list[OnCall]: List of OnCall objects.
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint=f"/api/account/teams/{str(team.unique_id)}/oncall/",
            success_code=200,
        )
        return [OnCall(**oncall) for oncall in response]

    def update_team_permissions(self, team: Team, permissions: list[str]) -> list[str]:
        """Update the team permissions for a team object

        Args:
            team (Team): The team object to update
            permissions (list[str]): list of permissions to be attatched to a team.

        Returns:
            list[str]: List of permissions
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint=f"/api/account/teams/{str(team.unique_id)}/permissions/",
            request_payload={
                "account_permissions": permissions,
            },
            success_code=200,
        )
        return response.get("account_permissions", [])
