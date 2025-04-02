from uuid import UUID

from .models import AccountMember, User
from zenduty.apiV2.client import ZendutyClient, ZendutyClientRequestMethod

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
            success_code=201,
        )
        return self.get_account_member(response["user"]["username"])

    def update_account_member(
        self,
        account_member: AccountMember,
        first_name: str = None,
        last_name: str = None,
        role: int = None,
        email: str = None,
    ) -> AccountMember:
        """Update account member information with optional fields

        Args:
            account_member_id (str): The ID of the account member to update
            first_name (str, optional): New first name for the account member. Defaults to None.
            last_name (str, optional): New last name for the account member. Defaults to None.
            role (int, optional): New role for the account member. Defaults to None.

        Returns:
            AccountMember: Updated account member information from the server
        """
        # Fetch current account member details

        # Prepare the user part of the request payload
        user_payload = {
            "username": account_member.user.username,
            "first_name": first_name if first_name is not None else account_member.user.first_name,
            "last_name": last_name if last_name is not None else account_member.user.last_name,
        }

        # Initialize the request payload with the user information
        request_payload = {"user": user_payload}

        # Add role to the payload if provided
        if role is not None:
            request_payload["role"] = role
        else:
            request_payload["role"] = account_member.role
        # Execute the update request
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint=f"/api/account/members/{account_member.user.username}/",
            request_payload=request_payload,
            success_code=200,
        )

        # Return the updated account member
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
