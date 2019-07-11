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

    def create_incident(self,body):
        #Used to create an incident for a particular service, identified by id
        #params dict body: contains necessary details for creating incident
        # Sample body:
        #           {"service":"c7fff4c5-2def-41e8-9120-c63f649a825c",
        #            "escalation_policy":"a70244c8-e343-4dd0-8d87-2f767115568a",
        #            "user":null,
        #            "title":"Name of trial",
        #            "summary":"summary of trial"}
        #  escalation_policy,service, title and summary are required fields.
        #  if escalation_policy is not set (set to None then), then assigned_to is required, as follows
        #           {"service":"b1559a26-c51f-45a1-886d-f6caeaf0fc7e",
        #            "escalation_policy":null,
        #            "assigned_to":"826032d6-7ccd-4d58-b114-f",
        #            "title":"Name of trial",
        #            "summary":"Summary of trial"}
        return self.api_client.call_api('POST','/api/incidents/',body=body)