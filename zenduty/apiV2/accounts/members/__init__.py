import json
from uuid import UUID

from zenduty.apiV2.client import ZendutyClient, ZendutyClientRequestMethod
from .models import AccountMember


class AccountMemberClient:
    def __init__(self, client: ZendutyClient):
        self._client = client

    def invite(
        self, team_id: UUID, email: str, first_name: str, last_name: str, role: int
    ) -> AccountMember:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/account/api_invite/",
            request_payload={
                "team_id": str(team_id),
                "user_detail": {
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "role": role,
                },
            },
            success_code=200,
        )
        return AccountMember(**response)

    def update_account_member(self, account_member: AccountMember) -> AccountMember:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint="/api/account/members/%s/" % account_member.unique_id,
            request_payload=json.loads(account_member.to_json()),
            success_code=200,
        )
        return AccountMember(**response)

    def get_account_member(self, account_member_id: str) -> AccountMember:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/members/%s/" % account_member_id,
            success_code=200,
        )
        return AccountMember(**response)

    def get_all_members(self) -> list[AccountMember]:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/members/",
            success_code=200,
        )
        return [AccountMember(**member) for member in response]

    def delete_account_member(self, account_member: AccountMember) -> None:
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint="/api/account/members/%s/" % str(account_member.unique_id),
            success_code=204,
        )
