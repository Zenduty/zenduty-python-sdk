from datetime import timedelta
from zenduty.apiV2.teams import TeamsClient
from zenduty.apiV2.accounts.members import AccountMemberClient
from zenduty.apiV2.authentication.zenduty_credential import ZendutyCredential
from zenduty.apiV2.teams.escalation_policies.rules import RuleBuilder
from zenduty.apiV2.teams.escalation_policies.targets import TargetBuilder
from zenduty.apiV2.client import ZendutyClient

cred = ZendutyCredential("f3ab5c762c914dacca2c0c530b260fdf9fff0cc7") # Default credentials to ZENDUTY_API_KEY env variable if not provided. (use export ZENDUTY_API_KEY="<YOUR KEY>")
client = ZendutyClient(credential=cred, use_https=True) # defaults to default service endpoint zenduty.com

# We pass a team client with default client.
teams_client = TeamsClient(client=client)

# We create a team
team = teams_client.create_team(name="Test Team 3")
print("Created team...")
# we print a pretty json for the team
print(team)


# We create a member client.
member_client = AccountMemberClient(client=client)

# we invite a member to the created team.
member = member_client.invite(
    team_id=team.unique_id,
    email="john.doe.1@zenduty.com",
    first_name="John",
    last_name="doe",
    role=3
)
print("Created member...")
print(member)

# we get the escalation policy client for the specific team.
esp_client_for_team = teams_client.get_escalation_policy_client(team)
# we create a escalation policy for the team
esp = esp_client_for_team.create_esp(
    name="ESP-001",
    summary="Summary for ESP001",
    description="This is a test escalation policy",
    rules=RuleBuilder()
        .add_rule(
            delay=timedelta(seconds=0), # If only one rule set it to 0 only.
            postition=0,
            targets=TargetBuilder()
                .add_target(target_type=2, target_id=member.user.username)
                .build()
        )
        .build(),
)
print("Created Escalation Policy...")
print(esp)


# we get the SLA client for the specific team.
sla_client_for_team = teams_client.get_sla_client(team)
# we create a SLA for the team
sla = sla_client_for_team.create_sla(
    name="SLA-001",
    is_active=True,
    acknowledge_time=10,
    resolve_time=10
)
print("Created SLA...")
print(sla)

# we get the Task Template client for the specific team.
task_template_client_for_team = teams_client.get_task_template_client(team)
# we create a Task Teamplate for the team
tt = task_template_client_for_team.create_task_template(
    name="Task-001",
    summary="Task template"
)
print("Created task template...")
print(tt)

# we get the priority client for the specific team.
priority_client_for_team = teams_client.get_priority_client(team)
# we create a Priority for the team
priority = priority_client_for_team.create_priority(
    name="Priority-001",
    color="red",
    description="Description for priority-001"
)
print("Created team priority...")
print(priority)

# we get the service client for the specific team.
svc_client_for_team = teams_client.get_service_client(team)
# we create a Service for the team
svc = svc_client_for_team.create_service(
    acknowledgement_timeout=0,
    name="SVC-001",
    summary="Summary for SVC-001",
    description="Description for SVC-001",
    escalation_policy=esp.unique_id,
    team=team.unique_id,
    sla=sla.unique_id,
    task_template=tt.unique_id,
    auto_resolve_timeout=0,
    team_priority=priority.unique_id,
    under_maintenance=False
    )

print("Created service...")
# we pretty print the service created
print(svc)
