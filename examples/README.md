## Example 1

The following example shows how to:
- Create a team
- Invite a user to the team
- Create a escalation policy
- Create a SLA
- Create a Task Teamplate
- Create a Team Priority
- Create a Service

### Code:

```python
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


## Example 2

In a continuation of the above example.

The following example shows how to:
- Create an Incident
- Create notes for the incident.

### Code:
```python


from uuid import UUID
from zenduty.apiV2.authentication.zenduty_credential import ZendutyCredential
from zenduty.apiV2.client import ZendutyClient
from zenduty.apiV2.incidents import IncidentClient


cred = ZendutyCredential("f3ab5c762c914dacca2c0c530b260fdf9fff0cc7")
client = ZendutyClient(credential=cred, use_https=True)

# we create a incident client
incident_client = IncidentClient(client)
# we create a a incident for the team and other specifics from example 1.
incident = incident_client.create_incident(
    title="Incident-0001",
    summary="New summary",
    assigned_to="0966ead6-39c7-4c6e-bba7-5",
    escalation_policy=UUID("05cafff6-5183-471c-8870-335df3edc779"),
    service=UUID("6b393d6a-dc4d-4ba0-80ac-11c19ee76f9a"),
    sla=UUID("c228c696-e675-407d-928e-287e9e1306e2"),
    status=1,
    team_priority=UUID("deb7c33f-de64-43e6-b8d8-c4a610442624"),
)
print("Created incident...")
print(incident)

# we get the incident note client for the incident
note_client = incident_client.get_note_client(incident)
# we create a array of incident notes to create
notes = [
    "Incident Note - 001",
    "Incident Note - 002",
    "Incident Note - 003",
    "Incident Note - 004",
    "Incident Note - 005",
]

for note in notes:
    # we create a incident note for all the notes to create
    _note = note_client.create_incident_note(
        note=note
    )
    print("Note created...")
    print(_note)


```
### Output:

```bash
mayank@ATSs-MacBook-Pro zenduty-python-sdk % python3 client.py 
Created incident...
{
    "acknowledged_date": null,
    "assigned_to": "0966ead6-39c7-4c6e-bba7-5",
    "assigned_to_name": "John doe",
    "context_window_end": null,
    "context_window_start": null,
    "creation_date": "2023-02-27T09:03:53.760264+00:00",
    "escalation_policy": "05cafff6-5183-471c-8870-335df3edc779",
    "escalation_policy_object": {
        "name": "ESP-001",
        "unique_id": "05cafff6-5183-471c-8870-335df3edc779"
    },
    "incident_key": "chvXpTzNdotyMNfyGXoBeK",
    "incident_number": 5803,
    "merged_with": null,
    "resolved_date": null,
    "service": "6b393d6a-dc4d-4ba0-80ac-11c19ee76f9a",
    "service_object": {
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
    },
    "sla": "c228c696-e675-407d-928e-287e9e1306e2",
    "sla_object": {
        "acknowledge_time": 10,
        "creation_date": "2023-02-27T08:40:50.051330+00:00",
        "is_active": true,
        "name": "SLA-001",
        "resolve_time": 10,
        "unique_id": "c228c696-e675-407d-928e-287e9e1306e2"
    },
    "status": 1,
    "summary": "New summary",
    "tags": [],
    "team_priority": "deb7c33f-de64-43e6-b8d8-c4a610442624",
    "team_priority_object": {
        "color": "red",
        "description": "Description for priority-001",
        "name": "Priority-001",
        "unique_id": "deb7c33f-de64-43e6-b8d8-c4a610442624"
    },
    "title": "Incident-0001",
    "unique_id": "nW4FvNgtooBszwSTSjaX2A",
    "urgency": 1
}
Note created...
{
    "creation_date": "2023-02-27T09:03:55.103231+00:00",
    "incident": 5803,
    "note": "Incident Note - 001",
    "unique_id": "kjtupist6nspAYkugWQt8c",
    "user": "35b1ff9f-99e5-4e1e-8d73-d",
    "user_name": "Shyam Patel"
}
Note created...
{
    "creation_date": "2023-02-27T09:03:59.497570+00:00",
    "incident": 5803,
    "note": "Incident Note - 002",
    "unique_id": "Q43fQ7UQQgVysPjVqkSG2N",
    "user": "35b1ff9f-99e5-4e1e-8d73-d",
    "user_name": "Shyam Patel"
}
Note created...
{
    "creation_date": "2023-02-27T09:04:00.918126+00:00",
    "incident": 5803,
    "note": "Incident Note - 003",
    "unique_id": "djrzYC87TTsimHcuNibrzB",
    "user": "35b1ff9f-99e5-4e1e-8d73-d",
    "user_name": "Shyam Patel"
}
Note created...
{
    "creation_date": "2023-02-27T09:04:01.914746+00:00",
    "incident": 5803,
    "note": "Incident Note - 004",
    "unique_id": "x6z7kqgd3zbGgVtjdp8Uc8",
    "user": "35b1ff9f-99e5-4e1e-8d73-d",
    "user_name": "Shyam Patel"
}
Note created...
{
    "creation_date": "2023-02-27T09:04:02.927280+00:00",
    "incident": 5803,
    "note": "Incident Note - 005",
    "unique_id": "8o9pCn85zyGqG533e9esgm",
    "user": "35b1ff9f-99e5-4e1e-8d73-d",
    "user_name": "Shyam Patel"
}
```