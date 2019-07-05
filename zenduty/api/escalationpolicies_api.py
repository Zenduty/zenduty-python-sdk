from zenduty.api_client import ApiClient

class EscalationPoliciesApi(object):
    def __init__(self,api_client=None):
        if api_client is None:
            api_client=ApiClient()
        self.api_client = api_client

    def get_escalation_policies(self,team_id):
        #Returns the escalation policies belonging to one team
        #params str team_id: unique id of team
        return self.api_client.call_api('GET','/api/account/teams/{}/escalation_policies/'.format(team_id))

    def create_escalation_policy(self,team_id,body):
        #Creates an escalation policy for one team
        #params str team_id: unique id of team
        #params dict body: contains the required details for creating escalation policy
        #Sample body:
        #   {'name':name,
        #     'summary':summary,
        #     'description':description,
        #     'rules':rules,
        #     'unique_id':unique_id,
        #     'team':team_id}
        return self.api_client.call_api('POST','/api/account/teams/{}/escalation_policies/'.format(team_id),body=body)

    def get_escalation_policy_by_id(self,team_id,ep_id):
        #Returns escalation_policy identified by id
        #params str team_id: unique id of team
        #params str ep_id: unique id of escalation policy
        return self.api_client.call_api('GET','/api/account/teams/{}/escalation_policies/{}/'.format(team_id,ep_id))

    def update_escalation_policy(self,team_id,ep_id,body):
        #Updates escalation policy, identified by id
        #params str team_id: unique id of team
        #params str ep_id: unqiue id of escalation policy
        #params dict body: contains all the updated values
        #       'rules' is a required part of the body
        #Sample body:
        # body={'summary':'changes description',
        #       'rules':[{"delay":1,
        #                 "targets":[{"target_type":2,
        #                             "target_id":"826032d6-7ccd-4d58-b114-f"}],
        #                 "position":1,
        #                 "unique_id":"c0dad09b-321b-491e-9c23-f816c7bd0339"}]}
        return self.api_client.call_api('PATCH','/api/account/teams/{}/escalation_policies/{}/'.format(team_id,ep_id),body=body)

    def delete_escalation_policy(self,team_id,ep_id):
        #Deletes escalation policy, identified by id
        #params str team_id: unique id of team
        #params str ep_id: unique id of escalation policy
        return self.api_client.call_api('DELETE','/api/account/teams/{}/escalation_policies/{}/'.format(team_id,ep_id))
