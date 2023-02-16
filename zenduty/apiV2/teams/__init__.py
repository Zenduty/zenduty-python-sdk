from ..client import ZendutyClient, ZendutyClientRequestMethod
from ._models import Team, Member
from uuid import UUID
from .schedules import ScheduleClient

class ZendutyTeamsClient:
    def __init__(self, client: ZendutyClient):
        self._client = client

    def get_schedule_client(self, team: Team) -> ScheduleClient:
        return ScheduleClient(self._client, team)

    def create_team(self, name: str) -> Team:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/account/teams/",
            request_payload={"name": name},
            success_code=201,
        )
        return Team(**response)

    def list_teams(self) -> list[Team]:
        # https://www.zenduty.com/api/account/teams/
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
        print(response)
        return response.get("account_permissions", [])

    def update_team_permissions(self, team: Team, permissions: list[str]) -> list[str]:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint=f"/api/account/teams/{str(team.unique_id)}/permissions/",
            request_payload={
                "account_permissions": permissions,
            },
            success_code=200,
        )
        print(response)
        return response.get("account_permissions", [])
