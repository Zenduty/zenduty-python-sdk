from zenduty.api_client import ApiClient

class IntegrationsApi(object):
    def __init__(self,api_client=None):
        if api_client is None:
            api_client=ApiClient()
        self.api_client = api_client

    def get_integrations_in_service(self,team_id,service_id):
        #Returns the integrations in a service
        #params str team_id: unique id of team
        #params str service_id: unique id of service
        return self.api_client.call_api('GET','/api/account/teams/{}/services/{}/integrations/'.format(team_id,service_id))

    def create_integration(self,team_id,service_id,body):
        #Creates a new integration for a given service in a team
        #params str team_id: unique id of team
        #params str service_id: unique id of service
        #params dict body: contains the details of the new integration
        # Sample body:
        #   {"name":"asdf",
        #   "summary":"asdf",
        #   "application":"27c9800c-2856-490d-8119-790be1308dd4"}
        return self.api_client.call_api('POST','/api/account/teams/{}/services/{}/integrations/'.format(team_id,service_id),body=body)

    def get_integrations_by_id(self,team_id,service_id,integration_id):
        #Returns an integration belonging to a service in a team, identified by id
        #params str team_id: unique id of team
        #params str service_id: unique id of service
        #params str integration_id: unique id of integration
        return self.api_client.call_api('GET','/api/account/teams/{}/services/{}/integrations/{}/'.format(team_id,service_id,integration_id))

    def get_alerts_in_integration(self,team_id,service_id,integration_id):
        #Retruns alerts in a particular integration
        #params str team_id: unique id of team
        #params str service_id: unique id of service
        #params str integration_id: unique id of integration
        return self.api_client.call_api('GET','/api/account/teams/{}/services/{}/integrations/{}/alerts/'.format(team_id,service_id,integration_id))
