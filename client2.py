import pprint
from zenduty.apiV2.authentication.zenduty_credential import ZendutyCredential
from zenduty.apiV2.client import ZendutyClient

creds = ZendutyCredential(
    "f3ab5c762c914dacca2c0c530b260fdf9fff0cc7"
)  # ZendutyCredential also takes in the api key from env variable [ZENDUTY_API_KEY]
client = ZendutyClient(credential=creds, use_https=True)

from zenduty.apiV2.teams import TeamsClient
from uuid import UUID

client = TeamsClient(client)
teams = client.list_teams()

print(teams)
