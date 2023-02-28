import json
from uuid import UUID

from zenduty.apiV2.client import ZendutyClient, ZendutyClientRequestMethod
from .models import AccountMember


class AccountMemberClient:
    def __init__(self, client: ZendutyClient):
        self._client = client

    def invite(
        self,
        team_id: UUID,
        email: str,
        first_name: str,
        last_name: str,
        role: int,
    ) -> AccountMember:
        """Invite users to the specified team

        Args:
            team_id (UUID): A system-generated string that represents the Team object's unique_id
            email (str): A string that represents the User object's email
            first_name (str): A string that represents the User object's first_name
            last_name (str): A string that represents the User object's last_name
            role (int): An integer that represents the Account Member object's role
        Returns:
            AccountMember: Returns an Account Member object.
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/account/api_invite/",
            request_payload={
                "team": str(team_id),
                "user_detail": {
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "role": role,
                },
            },
            success_code=200,
        )
        return self.get_account_member(response["user"]["username"])

    def update_account_member(self, account_member: AccountMember) -> AccountMember:
        """update account member information

        Args:
            account_member (AccountMember): updated account member information

        Returns:
            AccountMember: return the updated account memmber information from server
        """
        payload = json.loads(account_member.to_json())
        payload["user"].pop("email")
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint="/api/account/members/%s/" % account_member.user.username,
            request_payload=payload,
            success_code=200,
        )
        return AccountMember(**response)

    def get_account_member(self, account_member_id: str) -> AccountMember:
        """Get account member details by account member id

        Args:
            account_member_id (str): username of the acccount member

        Returns:
            AccountMember: account member information object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/members/%s/" % account_member_id,
            success_code=200,
        )
        return AccountMember(**response)

    def get_all_members(self) -> list[AccountMember]:
        """Gets all members in the account

        Returns:
            list[AccountMember]: List of account members
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/members/",
            success_code=200,
        )
        return [AccountMember(**member) for member in response]

    def delete_account_member(self, account_member: AccountMember) -> None:
        """delete a account member

        Args:
            account_member (AccountMember): account member object to delete
        """
        self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/account/deleteuser/",
            request_payload={
                "username": account_member.user.username,
            },
            success_code=204,
        )
