from zenduty.api_client import ApiClient

class TeamsApi(object):
    def __init__(self,api_client):
        if api_client is None:
            api_client=ApiClient()
        self.api_client = api_client

    def get_teams(self):
        #Returns all the teams and their details from your Zenduty account
        return self.api_client.call_api('GET','/api/account/teams/')

    def create_team(self,body):
        #Creates a new team for your zenduty account
        #params dict body: contains the details for your new team
        #Sample body:
        #   'name' is a required field
        #   {'name':name}
        return self.api_client.call_api('POST','/api/account/teams/',body)

    def get_team_details(self,team_id):
        #Returns a team form your zenduty acocunt, identified by id
        # params str team_id: unique id of team
        return self.api_client.call_api('GET','/api/account/teams/{}/'.format(team_id))

    def delete_team(self,team_id):
        #Deletes a team form your zenduty account
        #params str team_id: unique id of team
        return self.api_client.call_api('DELETE','/api/account/teams/{}/'.format(team_id))
