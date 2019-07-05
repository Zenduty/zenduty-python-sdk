from zenduty.api_client import ApiClient

class ServicesApi(object):
    def __init__(self,api_client=None):
        if api_client is None:
            api_client=ApiClient()
        self.api_client = api_client

    def get_service_for_team(self,team_id):
        #Returns all the services in a team
        #params str team_id: unnique id of team
        return self.api_client.call_api('GET','/api/account/teams/{}/services/'.format(team_id))

    def add_new_service_in_team(self,team_id,body):
        #Adds a new servie to a give team, identified by id
        #params str team_id: unique id of team
        #params dict body: contains the details of the new service to be added
        #Sample body
        #{"name":"Name of service",
        # "description":"Description of service",
        # "integrations":[{"application":"27c9800c-2856-490d-8119-790be1308dd4",
        #                 "name":"API",
        #                 "summary":"Edit summary for this integration"}],
        # "escalation_policy":"5c9b6288-c105-418d-970b-91a93d0e919a",
        # "acknowledgement_timeout":1,
        # "auto_resolve_timeout":1}
        return self.api_client.call_api('POST','/api/account/teams/{}/services/'.format(team_id),body=body)

    def get_services_by_id(self,team_id,service_id):
        #Returns a particular service from a  team, identified by id
        #params str team_id: unique id of team
        #params str service_id: unique id of service
        return self.api_client.call_api('GET','/api/account/teams/{}/services/{}/'.format(team_id,service_id))

    def update_service(self,team_id,service_id,body):
        #Updates the existing service in a team
        #params str team_id: unique id of team
        #params str service_id: unique id of service
        #params dict body: contains the updated details of services
        #Sample body:
        #{"unique_id":"bc808ce3-46c0-41d0-bf1f-f405fdd0c1c3",
        # "auto_resolve_timeout":0,
        # "acknowledgement_timeout":0,
        # "status":1,
        # "escalation_policy":"5c9b6288-c105-418d-970b-91a93d0e919a"}
        return self.api_client.call_api('PATCH','/api/account/teams/{}/services/{}/'.format(team_id,service_id),body=body)

    def delete_service_from_team(self,team_id,service_id):
        #Deletes a particular service from a team
        #params str team_id: unique id of team
        #params str service_id: unnique id of service
        return self.api_client.call_api('DELETE','/api/account/teams/{}/services/{}/'.format(team_id,service_id))
