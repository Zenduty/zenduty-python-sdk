from zenduty.api_client import ApiClient

class EventsApi(object):
    def __init__(self,api_client=None):
        if api_client is None:
            api_client=ApiClient()
        self.api_client = api_client

    def create_event(self,integration_key,body):
        #Creates an incident event on zenduty
        #params str integration_key: unique key provided for your integration
        #params dict body: contains the details of the event
        #   'message', 'summary' are required fields of the body
        #   'alert_type' is "info" by default
        #   'suppressed' is false by default
        #   if no entity_id is provided, Zenduty provides one automatically
        # Sample body:
        #          {'message':message,
        #         'summary':summary,
        #         'alert_type':alert_type,
        #         'supressed':supressed}
        return self.api_client.call_api('POST','/api/events/{}/'.format(integration_key),body=body)
