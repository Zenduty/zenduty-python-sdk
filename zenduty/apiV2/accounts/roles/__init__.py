from .models import AccountRole
from zenduty.apiV2.client import ZendutyClient, ZendutyClientRequestMethod


class AccountRoleClient:
    def __init__(self, client: ZendutyClient):
        self._client = client

    def create_account_role(
        self,
        name: str,
        description: str,
        permissions: list[str],
    ) -> AccountRole:
        """Create a new account role

        Args:
            name (str): name of the role to create
            description (str): description of the role
            permissions (list[str]): permissions for the role

        Returns:
            AccountRole: account role object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/account/customroles/",
            request_payload={
                "name": name,
                "description": description,
                "permissions": permissions,
            },
            success_code=201,
        )
        return self.get_account_role(response["unique_id"])

    def get_account_role(self, account_role_id: str) -> AccountRole:
        """Get account role object by account_role_id

        Args:
            account_role_id (str): the unique id of account

        Returns:
            AccountRole: account role object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint=f"/api/account/customroles/{account_role_id}/",
            success_code=200,
        )
        return AccountRole(**response)

    def list_account_roles(self) -> list[AccountRole]:
        """get list of account roles

        Returns:
            list[AccountRole]: List of account roles
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/customroles/",
            success_code=200,
        )
        return [AccountRole(**r) for r in response]

    def update_account_role(
        self,
        account_role: AccountRole,
        permissions: list[str],
        name: str = None,
        description: str = None,
    ) -> AccountRole:
        """Update account role object with optional fields

        Args:
            account_role_id (str): The ID of the account role to update
            name (str, optional): New name for the account role. Defaults to None.
            description (str, optional): New description for the account role. Defaults to None.
            permissions (list[str], optional): New permissions for the account role. Defaults to None.

        Returns:
            AccountRole: Updated information about the account role
        """
        # Fetch current account role details

        # Prepare the request payload with either new values or existing ones
        request_payload = {
            "name": name if name is not None else account_role.name,
            "description": description if description is not None else account_role.description,
            "permissions": permissions if permissions is not None else account_role.permissions,
        }

        # Execute the update request
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint=f"/api/account/customroles/{account_role.unique_id}/",
            request_payload=request_payload,
            success_code=200,
        )

        # Return the updated account role
        return self.get_account_role(response["unique_id"])

    def delete_account_role(
        self,
        account_role: AccountRole,
    ) -> None:
        """Delete account role

        Args:
            account_role (AccountRole): account role to be deleted
        """
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint=f"/api/account/customroles/{account_role.unique_id}/",
            success_code=204,
        )
