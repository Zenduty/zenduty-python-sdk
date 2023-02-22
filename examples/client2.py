from zenduty.apiV2.authentication.zenduty_credential import ZendutyCredential
from zenduty.apiV2.client import ZendutyClient

creds = ZendutyCredential(
    "f3ab5c762c914dacca2c0c530b260fdf9fff0cc7"
)  # ZendutyCredential also takes in the api key from env variable [ZENDUTY_API_KEY]
client = ZendutyClient(credential=creds, use_https=True)

from zenduty.apiV2.accounts.members import AccountMemberClient
from uuid import UUID

member_client = AccountMemberClient(client)
account = member_client.invite(
    team_id=UUID("2c0984d9-37f0-417d-a3d7-9de58eb480c0"),
    email="mayank22oct2@gmail.com",
    first_name="snxs",
    last_name="aaa",
    role=3,
)
print(account.to_json())
