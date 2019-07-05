from zenduty.api_client import ApiClient

class MembersApi(object):
    def __init__(self,api_client=None):
        if api_client is None:
            api_client=ApiClient()
        self.api_client = api_client

    def add_members_to_team(self,team_id,body):
        #Adds a member to a given team, identified by id
        #params str team_id: unique id of team
        #params dict body: contains the details of the user being added and the team to add to
        #Sample body:
        # {"team":"d4a777db-5bce-419c-a725-420ebb505c54","user":"af9eeb60-5acb-406c-971e-3"}
        return self.api_client.call_api('POST','/api/account/teams/{}/members/'.format(team_id),body=body)

    def delete_members_from_team(self,team_id,member_id):
        #Removes a member from a particular team
        #params str team_id: unique id of a team
        #params str member_id: unique id of member to be deleted
        return self.api_client.call_api('DELETE','/api/account/teams/{}/members/{}/'.format(team_id,member_id))
