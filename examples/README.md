## Example 1

### Code:

```python3
from datetime import timedelta
from zenduty.apiV2.teams import TeamsClient
from zenduty.apiV2.accounts.members import AccountMemberClient
from zenduty.apiV2.authentication.zenduty_credential import ZendutyCredential
from zenduty.apiV2.teams.escalation_policies.rules import RuleBuilder
from zenduty.apiV2.teams.escalation_policies.targets import TargetBuilder
from zenduty.apiV2.client import ZendutyClient

cred = ZendutyCredential("f3ab5c762c914dacca2c0c530b260fdf9fff0cc7")
client = ZendutyClient(credential=cred, use_https=True)
teams_client = TeamsClient(client=client)

team = teams_client.create_team(name="Test Team 3")
print("Created team...")
print(team)


member_client = AccountMemberClient(client=client)
member = member_client.invite(
    team_id=team.unique_id,
    email="john.doe.1@zenduty.com",
    first_name="John",
    last_name="doe",
    role=3
)
print("Created member...")
print(member)

esp_client_for_team = teams_client.get_escalation_policy_client(team)
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

sla_client_for_team = teams_client.get_sla_client(team)
sla = sla_client_for_team.create_sla(
    name="SLA-001",
    is_active=True,
    acknowledge_time=10,
    resolve_time=10
)
print("Created SLA...")
print(sla)


task_template_client_for_team = teams_client.get_task_template_client(team)
tt = task_template_client_for_team.create_task_template(
    name="Task-001",
    summary="Task template"
)
print("Created task template...")
print(tt)

priority_client_for_team = teams_client.get_priority_client(team)
priority = priority_client_for_team.create_priority(
    name="Priority-001",
    color="red",
    description="Description for priority-001"
)
print("Created team priority...")
print(priority)


svc_client_for_team = teams_client.get_service_client(team)
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
print(svc)

```

#### Output:

```bash
% python3 client.py
Created team...
{
    "account": "0a3d2b08-6fec-4264-84fd-60886c241e5c",
    "creation_date": "2023-02-27T00:00:00",
    "members": [
        {
            "joining_date": "2023-02-27T08:40:40.396295+00:00",
            "role": 1,
            "team": "49580d9f-9117-4c28-ae6c-cd893711302b",
            "unique_id": "e25cd474-6ce7-4ff3-87fb-fd04d08fafc0",
            "user": {
                "email": "kalariya3110@gmail.com",
                "first_name": "Shyam",
                "last_name": "Patel",
                "username": "35b1ff9f-99e5-4e1e-8d73-d"
            }
        }
    ],
    "name": "Test Team 3",
    "owner": "35b1ff9f-99e5-4e1e-8d73-d",
    "private": true,
    "roles": [],
    "unique_id": "49580d9f-9117-4c28-ae6c-cd893711302b"
}
Created member...
{
    "custom_role_id": null,
    "is_verified": false,
    "joining_date": "2023-02-27T08:40:43.667879Z",
    "role": 3,
    "team": null,
    "time_zone": "UTC",
    "unique_id": "b7f6a1ed-b786-4975-b22e-10913c7bd320",
    "user": {
        "email": "john.doe.1@zenduty.com",
        "first_name": "John",
        "last_name": "doe",
        "username": "0966ead6-39c7-4c6e-bba7-5"
    }
}
Created Escalation Policy...
{
    "description": "This is a test escalation policy",
    "global_ep": false,
    "move_to_next": true,
    "name": "ESP-001",
    "repeat_policy": 0,
    "rules": [
        {
            "delay": 0,
            "position": 1,
            "targets": [
                {
                    "target_id": "0966ead6-39c7-4c6e-bba7-5",
                    "target_type": 2
                }
            ],
            "unique_id": "de9fa876-2e42-4dfe-be53-af65933af778"
        }
    ],
    "summary": "Summary for ESP001",
    "team": "49580d9f-9117-4c28-ae6c-cd893711302b",
    "unique_id": "05cafff6-5183-471c-8870-335df3edc779"
}
Created SLA...
{
    "acknowledge_time": 10,
    "conditions": "{}",
    "creation_date": null,
    "description": "",
    "escalations": [],
    "is_active": true,
    "name": "SLA-001",
    "resolve_time": 10,
    "summary": "",
    "team": 5546,
    "unique_id": "c228c696-e675-407d-928e-287e9e1306e2"
}
Created task template...
{
    "creation_date": "2023-02-27T08:40:51.132641+00:00",
    "due_immediately": 0,
    "name": "Task-001",
    "summary": "Task template",
    "team": "49580d9f-9117-4c28-ae6c-cd893711302b",
    "unique_id": "2b0676a3-694c-4f6b-ace5-d188cb860f9a"
}
Created team priority...
{
    "color": "red",
    "creation_date": "2023-02-27T08:40:55.998958+00:00",
    "description": "Description for priority-001",
    "name": "Priority-001",
    "team": 5546,
    "unique_id": "deb7c33f-de64-43e6-b8d8-c4a610442624"
}
Created service...
{
    "acknowledgement_timeout": 0,
    "auto_resolve_timeout": 0,
    "collation": 0,
    "collation_time": 0,
    "created_by": "35b1ff9f-99e5-4e1e-8d73-d",
    "creation_date": "2023-02-27T08:40:57.136443+00:00",
    "description": "Description for SVC-001",
    "escalation_policy": "05cafff6-5183-471c-8870-335df3edc779",
    "name": "SVC-001",
    "sla": "c228c696-e675-407d-928e-287e9e1306e2",
    "status": 1,
    "summary": "Summary for SVC-001",
    "task_template": "2b0676a3-694c-4f6b-ace5-d188cb860f9a",
    "team": "49580d9f-9117-4c28-ae6c-cd893711302b",
    "team_name": "Test Team 3",
    "team_priority": "deb7c33f-de64-43e6-b8d8-c4a610442624",
    "under_maintenance": false,
    "unique_id": "6b393d6a-dc4d-4ba0-80ac-11c19ee76f9a"
}
% 
```