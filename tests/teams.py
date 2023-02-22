import unittest
import inspect
from .utils import write_hacks


class TestTeams(unittest.TestCase):
    # def test_create_teams(self):
    #     from zenduty.apiV2.authentication.zenduty_credential import ZendutyCredential
    #     from zenduty.apiV2.client import ZendutyClient
    #     creds = ZendutyCredential("f3ab5c762c914dacca2c0c530b260fdf9fff0cc7") # ZendutyCredential also takes in the api key from env variable [ZENDUTY_API_KEY]
    #     client = ZendutyClient(credential=creds, use_https=True)
    #     from zenduty.apiV2.teams import TeamsClient
    #     from uuid import UUID
    #     team_client = TeamsClient(client)
    #     data = team_client.create_team(name="TEST001")
    #     write_hacks(inspect.stack()[0][3], data)

    # def test_list_teams(self):
    #     from zenduty.apiV2.authentication.zenduty_credential import ZendutyCredential
    #     from zenduty.apiV2.client import ZendutyClient
    #     creds = ZendutyCredential("f3ab5c762c914dacca2c0c530b260fdf9fff0cc7") # ZendutyCredential also takes in the api key from env variable [ZENDUTY_API_KEY]
    #     client = ZendutyClient(credential=creds, use_https=True)
    #     from zenduty.apiV2.teams import TeamsClient
    #     from uuid import UUID
    #     team_client = TeamsClient(client)
    #     data = team_client.list_teams()
    #     write_hacks(inspect.stack()[0][3], data)

    # def test_update_team(self):
    #     from zenduty.apiV2.authentication.zenduty_credential import ZendutyCredential
    #     from zenduty.apiV2.client import ZendutyClient
    #     creds = ZendutyCredential("f3ab5c762c914dacca2c0c530b260fdf9fff0cc7") # ZendutyCredential also takes in the api key from env variable [ZENDUTY_API_KEY]
    #     client = ZendutyClient(credential=creds, use_https=True)
    #     from zenduty.apiV2.teams import TeamsClient
    #     from uuid import UUID
    #     team_client = TeamsClient(client)
    #     data = team_client.find_team_by_id(UUID("2c0984d9-37f0-417d-a3d7-9de58eb480c0"))
    #     data = team_client.update_team(data)
    #     write_hacks(inspect.stack()[0][3], data)
    pass
