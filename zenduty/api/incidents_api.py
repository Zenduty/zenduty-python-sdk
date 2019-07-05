from zenduty.api_client import ApiClient

class IncidentsApi(object):
    def __init__(self,api_client=None):
        if api_client is None:
            api_client=ApiClient()
        self.api_client = api_client

    def get_incidents(self,body):
        #Returns the incidents from your zenduty account
        #params dict body: contains all the required details of your account
        # Sample body:
        #           {'page':1,
        #         'status':5,
        #         'team_id':['a2c6322b-4c1b-4884-8f7a-a7f270de98cb'],
        #         'service_ids':[],
        #         'user_ids':[]}
        return self.api_client.call_api('GET','/api/incidents/',body=body)

    def get_incidents_by_number(self,incident_number):
        #Returns the incidents belonging to a given incident number
        #params int incident_number: incident number of event
        return self.api_client.call_api('GET','/api/incidents/{}/'.format(incident_number))

    def get_incident_alerts(self,incident_number):
        #Returns all alerts of a particular incident
        #params int incident_number: incident number of event
        return self.api_client.call_api('GET','/api/incidents/{}/alerts/'.format(incident_number))

    def get_incident_notes(self,incident_number):
        #Gets the notes regarding an incident, identified by incident number
        #params int incident_number: incident number of event
        return self.api_client.call_api('GET','/api/incidents/{}/note/'.format(incident_number))

    def acknowledge_or_resolve_incidents(self,incident_number,body):
        #Used to acknowledge or resolve incident, identified by incident number
        #params str incident_number: incident number of event
        #params dict body: contains the changed values of incident
        # Sample body:
        #          {'status':3,
        #         'incident_number':12}
        return self.api_client.call_api('PATCH','/api/incidents/{}/'.format(incident_number),body=body)
