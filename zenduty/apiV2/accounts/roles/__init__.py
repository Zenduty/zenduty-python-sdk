import json
from ...client import ZendutyClient, ZendutyClientRequestMethod
from .models import AccountRole


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

    def update_account_role(self, account_role: AccountRole) -> AccountRole:
        """Update account role object

        Args:
            account_role (AccountRole): updated information about a account role

        Returns:
            AccountRole: updated information about a account role
        """        
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint="/api/account/customroles/%s/" % str(account_role.unique_id),
            request_payload=json.loads(account_role.to_json()),
            success_code=200,
        )
        return self.get_account_role(response["unique_id"])

    def delete_account_role(self, account_role: AccountRole) -> None:
        """Delete account role

        Args:
            account_role (AccountRole): account role to be deleted
        """        
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint=f"/api/account/customroles/{str(account_role.unique_id)}/",
            success_code=204,
        )
