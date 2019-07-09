import zenduty
from zenduty.exceptions import ApiException

api_instance = zenduty.TeamsApi(zenduty.ApiClient('ENTER-YOUR-ACCESS-TOKEN-HERE'))

try:
    # Get Incidents
    api_response = api_instance.get_teams()
    print(api_response.data)
except ApiException as e:
    print("Exception when calling TeamsApi->api_account_teams_get: %s\n" % e)
