import unittest
import inspect
from .utils import write_hacks


class TestAccount(unittest.TestCase):
    pass
    # def test_invite(self):
    #     from zenduty.apiV2.authentication.zenduty_credential import ZendutyCredential
    #     from zenduty.apiV2.client import ZendutyClient

    #     creds = ZendutyCredential("f3ab5c762c914dacca2c0c530b260fdf9fff0cc7") # ZendutyCredential also takes in the api key from env variable [ZENDUTY_API_KEY]
    #     client = ZendutyClient(credential=creds, use_https=True)
    #     from zenduty.apiV2.accounts.members import AccountMemberClient
    #     from uuid import UUID
    #     member_client = AccountMemberClient(client)
    #     data = member_client.invite(
    #         team_id=UUID("2c0984d9-37f0-417d-a3d7-9de58eb480c0"),
    #         email="ds31@gmail.com",
    #         first_name="snxs",
    #         last_name="aaa",
    #         role=3
    #     )
    #     write_hacks(inspect.stack()[0][3], data)
    # def test_get_all_member(self):
    #     from zenduty.apiV2.authentication.zenduty_credential import ZendutyCredential
    #     from zenduty.apiV2.client import ZendutyClient
    #     creds = ZendutyCredential("f3ab5c762c914dacca2c0c530b260fdf9fff0cc7") # ZendutyCredential also takes in the api key from env variable [ZENDUTY_API_KEY]
    #     client = ZendutyClient(credential=creds, use_https=True)
    #     from zenduty.apiV2.accounts.members import AccountMemberClient
    #     member_client = AccountMemberClient(client)
    #     data = member_client.get_all_members()
    #     print(data)
    #     write_hacks(inspect.stack()[0][3], data)

    # def test_get_account_member(self):
    #     from zenduty.apiV2.authentication.zenduty_credential import ZendutyCredential
    #     from zenduty.apiV2.client import ZendutyClient
    #     creds = ZendutyCredential("f3ab5c762c914dacca2c0c530b260fdf9fff0cc7") # ZendutyCredential also takes in the api key from env variable [ZENDUTY_API_KEY]
    #     client = ZendutyClient(credential=creds, use_https=True)
    #     from zenduty.apiV2.accounts.members import AccountMemberClient
    #     member_client = AccountMemberClient(client)
    #     data = member_client.get_account_member("cba9894b-181e-4a51-99f5-e")
    #     write_hacks(inspect.stack()[0][3], data)

    #   def test_update_account_member(self):
    #     from zenduty.apiV2.authentication.zenduty_credential import ZendutyCredential
    #     from zenduty.apiV2.client import ZendutyClient
    #     creds = ZendutyCredential("f3ab5c762c914dacca2c0c530b260fdf9fff0cc7") # ZendutyCredential also takes in the api key from env variable [ZENDUTY_API_KEY]
    #     client = ZendutyClient(credential=creds, use_https=True)
    #     from zenduty.apiV2.accounts.members import AccountMemberClient
    #     member_client = AccountMemberClient(client)
    #     member = member_client.get_account_member("cba9894b-181e-4a51-99f5-e")
    #     data = member_client.update_account_member(member)
    #     write_hacks(inspect.stack()[0][3], data)

    #   def test_create_account_role(self):
    #     from zenduty.apiV2.authentication.zenduty_credential import ZendutyCredential
    #     from zenduty.apiV2.client import ZendutyClient
    #     creds = ZendutyCredential("f3ab5c762c914dacca2c0c530b260fdf9fff0cc7") # ZendutyCredential also takes in the api key from env variable [ZENDUTY_API_KEY]
    #     client = ZendutyClient(credential=creds, use_https=True)
    #     from zenduty.apiV2.accounts.members import AccountMemberClient
    #     from zenduty.apiV2.accounts.roles import AccountRoleClient
    #     client = AccountRoleClient(client)
    #     data = client.create_account_role(
    #         description="account_role",
    #         name="new_account_role_2",
    #         permissions=[
    #             "sla_read"
    #         ],
    #     )
    #     write_hacks(inspect.stack()[0][3], data)


#    def test_list_account_roles(self):
#         from zenduty.apiV2.authentication.zenduty_credential import ZendutyCredential
#         from zenduty.apiV2.client import ZendutyClient
#         creds = ZendutyCredential("f3ab5c762c914dacca2c0c530b260fdf9fff0cc7") # ZendutyCredential also takes in the api key from env variable [ZENDUTY_API_KEY]
#         client = ZendutyClient(credential=creds, use_https=True)
#         from zenduty.apiV2.accounts.members import AccountMemberClient
#         from zenduty.apiV2.accounts.roles import AccountRoleClient
#         client = AccountRoleClient(client)
#         data = client.list_account_roles()
#         write_hacks(inspect.stack()[0][3], data)

#    def test_get_account_role_by_id(self):
#         from zenduty.apiV2.authentication.zenduty_credential import ZendutyCredential
#         from zenduty.apiV2.client import ZendutyClient
#         creds = ZendutyCredential("f3ab5c762c914dacca2c0c530b260fdf9fff0cc7") # ZendutyCredential also takes in the api key from env variable [ZENDUTY_API_KEY]
#         client = ZendutyClient(credential=creds, use_https=True)
#         from zenduty.apiV2.accounts.members import AccountMemberClient
#         from zenduty.apiV2.accounts.roles import AccountRoleClient
#         client = AccountRoleClient(client)
#         data = client.get_account_role("7f9251c6-4436-4006-9717-0dcb35413a9b")
#         write_hacks(inspect.stack()[0][3], data)


#    def test_update_account_role_by_id(self):
#         from zenduty.apiV2.authentication.zenduty_credential import ZendutyCredential
#         from zenduty.apiV2.client import ZendutyClient
#         creds = ZendutyCredential("f3ab5c762c914dacca2c0c530b260fdf9fff0cc7") # ZendutyCredential also takes in the api key from env variable [ZENDUTY_API_KEY]
#         client = ZendutyClient(credential=creds, use_https=True)
#         from zenduty.apiV2.accounts.members import AccountMemberClient
#         from zenduty.apiV2.accounts.roles import AccountRoleClient
#         client = AccountRoleClient(client)
#         data = client.get_account_role("7f9251c6-4436-4006-9717-0dcb35413a9b")
#         data = client.update_account_role(data)
#         write_hacks(inspect.stack()[0][3], data)
