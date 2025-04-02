from zenduty import ZendutyClient

zenduty_client = ZendutyClient(
    api_key="f3ab5c762c914dacca2c0c530b260fdf9fff0cc7", use_https=True
) # Default credentials to ZENDUTY_API_KEY env variable if not provided. (use export ZENDUTY_API_KEY="<YOUR KEY>")


from zenduty import AccountMemberClient
members = AccountMemberClient(zenduty_client).get_all_members()
test_member = members[0]
from zenduty import AccountNotificationClient
member_contact_methods = AccountNotificationClient(zenduty_client,test_member).list_member_contact_methods()
member_notification_rules = AccountNotificationClient(zenduty_client, test_member).list_member_notification_rules()

from zenduty import AccountRoleClient
account_roles = AccountRoleClient(zenduty_client).list_account_roles()

from zenduty import EventClient

from zenduty import RouterClient
all_routers = RouterClient(zenduty_client).get_all_routers()

from zenduty import IncidentClient
all_incidents = IncidentClient(zenduty_client).get_all_incidents(status=3)

from zenduty import IncidentNoteClient
all_incident_notes = IncidentNoteClient(zenduty_client, all_incidents[0]).get_all_incident_notes()

from zenduty import IncidentTagClient
all_tags = IncidentTagClient(zenduty_client, all_incidents[0]).get_all_tags() 

from zenduty import TeamsClient
teams = TeamsClient(zenduty_client).list_teams()
team_members = TeamsClient(zenduty_client).list_team_members(teams[0])
team_permissions = TeamsClient(zenduty_client).fetch_team_permissions(teams[0])
oncall = TeamsClient(zenduty_client).get_all_oncall(teams[0])

from zenduty import EscalationPolicyClient
eps = EscalationPolicyClient(zenduty_client, teams[0]).get_all_policies()

from zenduty import TeamMaintenanceClient
team_maintenace = TeamMaintenanceClient(zenduty_client, teams[0]).get_all_maintenance()

from zenduty import OncallClient
oncall_v2 = OncallClient(zenduty_client, teams[0]).list_team_oncall_v2()
oncall = OncallClient(zenduty_client, teams[0]).get_all_oncall()

from zenduty import PostmortemClient
pm = PostmortemClient(zenduty_client, teams[0]).get_all_postmortem()

from zenduty import PriorityClient
p  = PriorityClient(zenduty_client, teams[0]).get_all_priorities()

from zenduty import IncidentRoleClient
ir  = IncidentRoleClient(zenduty_client, teams[0]).get_all_roles()

from zenduty import ScheduleClient
schedules = ScheduleClient(zenduty_client, teams[0]).get_all_schedules()

from zenduty import ServiceClient
sercives  = ServiceClient(zenduty_client, teams[0]).get_all_services()

from zenduty import IntegrationClient
intergrations = IntegrationClient(zenduty_client, teams[0], sercives[0]).get_all_integrations()

from zenduty import SLAClient
sla = SLAClient(zenduty_client, teams[0]).get_all_slas()