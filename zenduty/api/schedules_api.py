from zenduty.api_client import ApiClient

class SchedulesApi(object):
    def __init__(self,api_client=None):
        if api_client is None:
            api_client=ApiClient()
        self.api_client = api_client

    def get_schedules(self,team_id):
        #Returns the schedules in a particular team, identified by id
        #params str team_id: unique id of a team
        return self.api_client.call_api('GET','/api/account/teams/{}/schedules/'.format(team_id))

    def create_schedule(self, team_id,body):
        #Creates a schedule for a team
        #params str team_id: unique id of team
        #params dict body: contains the details of the schedule to be created
        #Sample body:
        #{"name":"Name of schedule",
        # "summary":"summar of schedule",
        # "time_zone":"Asia/Kolkata",
        # "team":"d4a777db-5bce-419c-a725-420ebb505c54",
        # "layers":[]}
        return self.api_client.call_api('POST','/api/account/teams/{}/schedules/'.format(team_id),body=body)

    def get_schedule_by_id(self,team_id,schedule_id):
        #Returns a particular schedule from a team, identifed by id
        #params str team_id: unique id of a team
        #params schedule_id: unique id of schedule
        return self.api_client.call_api('GET','/api/account/teams/{}/schedules/{}/'.format(team_id,schedule_id))

    def update_schedule(self,team_id,schedule_id,body):
        #Updates the schedule details for a given team, identified by id
        #params str team_id: unique id of a team
        #params str schedul_id: unique id of schedule
        #params dict body: contains the updated values of  schedule
        #   'unique_id' and 'team' are required. Other fields are just those which have been changed
        #Sample body:
        #{"name":"Name of schedule",
        # "summary":"summar of schedule",
        # "time_zone":"Asia/Kamchatka",
        # "team":"d4a777db-5bce-419c-a725-420ebb505c54",
        # "unique_id":"f9b34bd3-818a-4b98-9d8a-04d8bd501cd0",
        # "layers":[]}
        return self.api_client.call_api('PATCH','/api/account/teams/{}/schedules/{}/'.format(team_id,schedule_id),body=body)

    def delete_schedule(self,team_id,schedule_id):
        #Deletes a schedule from a team
        #params str team_id:unique id of team
        #params str schedule_id: unique id of schedule
        return self.api_client.call_api('DELETE','/api/account/teams/{}/schedules/{}/'.format(team_id,schedule_id))
