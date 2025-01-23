# What is Zenduty??

Zenduty is a cutting edge platform for incident management. With high level automation, Zenduty enables faster and better incident resolution keeping developers first.

# Zenduty Python SDK

Python SDK to communicate with zenduty endpoints

## Installing

Installation can be done through pip, as follows:

```sh
$ pip install zenduty-api
```

or you may grab the latest source code from GitHub:

```sh
$ git clone https://github.com/Zenduty/zenduty-python-sdk
```

## Contents

1. zenduty/apiV2 : Contains proper Clients to communicate and execute each function
2. zenduty/api : contains the functions to communicate with zenduty API endpoints
3. zenduty/ : contains the common required files
4. bin/ : contains sample script to run zenduty functions

## Getting started

Before you begin making use of the SDK, make sure you have your Zenduty Access Token.
You can then import the package into your python script.

First of all, start off by making a client which connects to Zenduty using API Token. And create a team, most of the operations we'd do start off by creating a team, and creating services. For now, we will start off with creating an instance of a team.

The Approach here is to make clients here, every module will get a new client to make things simpler and easier for us to understand.

You will also notice most of the create functions will be creating an object, this is because we will need to pass them to update, and delete functions later on. you are free to use the sdk as you like.

```python

from zenduty.apiV2.authentication.zenduty_credential import ZendutyCredential
from zenduty.apiV2.client import ZendutyClient

class SDKTestingClient:
    def __init__(self):
        self.cred = ZendutyCredential(<ZENDUTY API KEY>)
        self.client = ZendutyClient(
            credential=self.cred, use_https=True
        )  # defaults to default service endpoint zenduty.com
        self.datetime_timestamp = self.datetime_timestamp()

    @staticmethod
    def datetime_timestamp():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

It is important to note that each function returns a urllib3.response.HTTPResponse object.

## Teams

This object represents a team of the account. It lets you create different independent operational units in the account. You can check out the team docs here https://docs.zenduty.com/docs/teams.

A Team can have multiple Members, Services, Integrations, Schedules, Escalation Policies, Priorities, Maintenance, etc..

```python
class SDKTeamsClient(SDKTestingClient):
    def __init__(self):
        super().__init__()
        self.teams_client = TeamsClient(client=self.client)
        self.invite_url = "https://zenduty.com/api/invite/accept/"
        self.test_team_name = f"Team - {self.datetime_timestamp}"
```

#### POST - Create a new team

```python
def create_team(self):
    create_team = self.teams_client.create_team(self.test_team_name)
    self.team_obj = create_team # class object made to use later down the road
    return create_team
```

From here on, use this team object returned by create_team() to get the unique id of that team by calling it like this.

#### GET - List Teams

Will fetch all the teams present in that account

```python
def list_teams(self):
    list_teams = self.teams_client.list_teams()
    return list_teams
```

#### PATCH - Update teams

Update the team

```python
def update_team(self):
    update_team = self.teams_client.update_team(self.team_obj, name="Updated team name here")
    return update_team
```

#### DEL - Delete team

Delete the team

```python
def delete_team(self):
    return self.teams_client.delete_team(self.team_obj)
```

## Account Member

This object represents an account user. Each account member object has a role, which can be "owner," "admin," or "user." An account can have only one owner, but multiple admins and users.

Prerequisite: A team must be created, where the role of each member can be assigned. For our example, we are creating a new team using the create_team() method mentioned above.

```python

class SDKAccountMembersClient(SDKTeamsClient):
    def __init__(self):
        super().__init__()
        self.teams_client = TeamsClient(client=self.client)
        self.account_member_client = AccountMemberClient(client=self.client)
        self.team_obj = self.create_team() #Will be used for the purpose of inviting users to the team

```

#### GET - Invite a member to the team

#### Invite a member to the team.

```python
def test_invite(self):
    test_email = f"john.doe.{random.randint(2,10000000000000000000000)}@zenduty.com"
    self.team_invite_object = self.account_member_client.invite(
        team_id=self.team_obj.unique_id,
        email=test_email,
        first_name="Test",
        last_name="User",
        role=2,
    )

```

#### PATCH - Update Account Member

```python
def test_update_account_member(self):
    result = self.account_member_client.update_account_member(
        self.team_invite_object,
        "Updated",
        "Member Details",
        2,
    )
```

#### GET - Get Account member

#### Get details about a particular team member (NOTE: To get account member you have to pass its user id, not AccountMember Uniqueid)

```python
def test_get_account_member_by_id(self):
    result = self.account_member_client.get_account_member(self.team_invite_object.user.username)
```

#### GET - Get all the members of a team

#### Get details of all the members of the team.

```python
def test_get_all_members(self):
    result = self.account_member_client.get_all_members()
```

#### DEL - Delete an Account member

#### Delete a particular member of the team.

```python
def test_delete_account_member(self):
    self.account_member_client.delete_account_member(self.team_invite_object)
```

## Account Roles

There are a list of permissions you could give to a role. Please refer to these docs, https://apidocs.zenduty.com/#tag/Account-Custom-Role.

```python
class SDKAccountRolesClient(SDKTestingClient):
    def __init__(self):
        super().__init__()
        self.account_role_client = AccountRoleClient(client=self.client)
```

#### POST - Create Account Role

```python
def create_account_role(self):
    test_name = f"Account Role - {self.datetime_timestamp}"
    create_account_role = self.account_role_client.create_account_role(
        name=test_name,
        description="Account Role Description",
        permissions=["sla_read"],
    )
```

#### GET - Get an Account Role

```python
def test_get_account_role(self):
    get_account_role = self.account_role_client.get_account_role(self.role_obj.unique_id)
    return get_account_role
```

#### GET - Get a list of roles

```python
def test_list_account_roles(self):
    list_account_roles = self.account_role_client.list_account_roles()
    return list_account_roles
```

#### PATCH - Update an Account Role

```python

def test_update_account_role(self):
    update_account_role = self.account_role_client.update_account_role(account_role=self.role_obj, permissions=["sla_read"])
    return update_account_role

```

#### DEL - Delete an Account Role

```python
def test_delete_account_role(self):
    delete_account_role = self.account_role_client.delete_account_role(account_role=self.role_obj)
```

## Global Event Router

Global Event Router is a webhook, when sent requests to it, would navigate it to a particular integration, to a particular request, if matched with the alert rules defined, would raise an alert.

Refer to this, for more information, https://apidocs.zenduty.com/#tag/Global-Router.

```python
class SDKGERClients(SDKTestingClient):
    def __init__(self):
        super().__init__()
        self.router_client = RouterClient(client=self.client)
        self.router_name = f"Router - {self.datetime_timestamp}"
```

#### POST - Create Router

```python
def create_router(self):
    create_router = self.router_client.create_router(
        name=self.router_name,
        description="Router Description",
    )
```

#### GET - List Routers

```python
def get_all_routers(self):
    return self.router_client.get_all_routers()
```

#### GET - Get Router by ID

```python
def get_router_by_id(self):
    return self.router_client.get_router_by_id(self.router_obj.unique_id)
```

#### PATCH - Update a particular Router

```python
def update_router(self):
    self.router_client.update_router(
        router = self.router_obj,
        name = f"Router - {self.datetime_timestamp}",
        description = "New Router Description",
    )
```

#### DEL - Delete a particular Router

```python
def delete_router(self):
    return self.router_client.delete_router(self.router_obj)
```

## Events

This object represents the events of an integration.

```python
class SDKEventsClient(SDKTestingClient):
    def __init__(self):
        super().__init__()
        self.event_client = EventClient(client=self.client)
        self.event_name = f"Event - {self.datetime_timestamp}"
```

#### GET - Get Router Client

```python
def get_router_client(self):
    get_router = self.event_client.get_router_client()

```

#### POST - Create an Event

```python
def test_create_event(self):
    create_event = self.event_client.create_event(
        integration_key=<unique_id of an Integration>,
        alert_type="info",
        message="This is info alert",
        summary="This is the incident summary111",
        entity_id=123455,
        payload={
            "status": "ACME Payments are failing",
            "severity": "1",
            "project": "kubeprod",
        },
        urls=[
            {
                "link_url": "https://www.example.com/alerts/12345/",
                "link_text": "Alert URL",
            }
        ],
    )
```

## Escalation Policy

Escalation policies dictate how an incident created within a service escalates within your team.

```python

class SDKEscalationPolicyClient(SDKTeamsClient):
    # Inheriting a few methods from the Teams Object.
    def __init__(self):
        super().__init__()
        self.uuid = self.generate_uuid()
        self.teams_client = TeamsClient(client=self.client)
        self.account_member_client = AccountMemberClient(client=self.client)

        # Team object: Needed for escalation policy client
        self.team_obj = self.teams_client.create_team(name=f"ESP Team - {self.datetime_timestamp}")

        self.escalation_policy_client = self.teams_client.get_escalation_policy_client(
            self.team_obj
        )

        self.ep_name = f"EP - {self.datetime_timestamp}"

        # User required to add to escalation policy
        self.test_email = f"john.doe.{random.randint(2,10000000000000000000000)}@zenduty.com"
        self.team_member_obj = self.account_member_client.invite(
            team_id=self.team_obj.unique_id,
            email=self.test_email,
            first_name="Test",
            last_name="User",
            role=2,
        )

    def generate_uuid(self):
        return uuid4()
```

#### POST - Create an Escalation Policy

```python
def create_escalation_policy(self):
    self.rule_build = [
        {
            "delay": 0,
            "targets": [
                {"target_type": 2, "target_id": self.team_member_obj.user.username}
            ],
            "position": 1,
        }
    ]

    self.create_escalation_policy_obj = self.escalation_policy_client.create_esp(
        self.ep_name, rules=self.rule_build
    )

```

#### GET - Get Escalation Policies by ID

```python
def test_get_esp_by_id(self):
    self.escalation_policy_client.get_esp_by_id(
        esp_id=self.create_escalation_policy_obj.unique_id
    )
```

#### POST - Update Escalation Policy

```python
def test_update_esp(self):
    update_esp = self.escalation_policy_client.update_esp(
            esp=self.create_escalation_policy_obj,
            name="Test Updated",
            rules=self.rule_build,
        )
```

#### GET - Get all the escalation policies

```python
def test_get_all_policies(self):
    all_esp = self.escalation_policy_client.get_all_policies()
    return all_esp
```

#### DEL - Delete an Escalation Policy

```python
def test_delete_esp(self):
    delete_esp = self.escalation_policy_client.delete_esp(esp=self.create_escalation_policy_obj)

```

## Schedules

```python
class SDKSchedulesClient(SDKTeamsClient):
    def __init__(self):
        super().__init__()
        self.uuid = self.generate_uuid()
        self.teams_client = TeamsClient(client=self.client)
        self.account_member_client = AccountMemberClient(client=self.client)

        self.team_obj = self.teams_client.create_team(name=f"Schedule Team - {self.datetime_timestamp}")

        # adding test user to the team
        self.test_email = f"john.doe.{random.randint(2,10000000000000000000000)}@zenduty.com"
        self.team_member_obj = self.account_member_client.invite(
            team_id=self.team_obj.unique_id,
            email=self.test_email,
            first_name="Test",
            last_name="User",
            role=2,
        )

        self.schedules_client = self.teams_client.get_schedule_client(self.team_obj)
        self.schedules_name = f"Schedules - {self.datetime_timestamp}"
        self.layers = [
            {
                "name": "Layer 1",
                "is_active": True,
                "restriction_type": 0,
                "restrictions": [],
                "rotation_start_time": "2025-07-29T03:30:00.000Z",
                "rotation_end_time": None,
                "shift_length": 86400,
                "users": [
                    {
                        "user":self.team_member_obj.user.username,
                        "position": 1,
                    }
                ],
            }
        ]

    def generate_uuid(self):
        return uuid4()
```

#### POST - Create an Escalation Policy

```python
def create_schedule(self):
    create_schedule = self.schedules_client.create_schedule(
        name=self.schedules_name,
        timezone="Asia/Kolkata",
        layers=self.layers,
        overrides=self.overrides,
    )
```

#### GET - Get all Schedules

```python
def test_get_all_schedules(self):
    get_all_schedules = self.schedules_client.get_all_schedules()
```

#### GET - Get Schedules by ID

```python
def test_get_schedule_by_id(self):
    self.get_schedule_by_id = self.schedules_client.get_schedule_by_id(
            schedule_id=self.schedule_obj.unique_id
        )
    return self.get_schedule_by_id
```

#### POST - Update a Schedule

```python
def test_update_schedule(self):
    update_schedule = self.schedules_client.update_schedule(
            schedule=self.schedule_obj,
            name="Test Schedule Updated",
        )
```

#### DEL - Delete a Schedule

```python
def test_delete_schedules(self):
    delete_schedule = self.schedules_client.delete_schedule(
            schedule=self.schedule_obj
    )
```

## Maintenance

```python
class SDKMaintenanceClient(SDKTeamsClient):
    def __init__(self):
        super().__init__()
        self.uuid = self.generate_uuid()
        self.teams_client = TeamsClient(client=self.client)


        self.team_by_id = self.teams_client.find_team_by_id(
            team_id=self.team_ids[0].unique_id
        )
        self.maintenance_client = self.teams_client.get_maintenance_client(
            self.team_by_id
        )
        self.maintenance_name = f"Maintenance Mode - {self.datetime_timestamp}"

    def generate_uuid(self):
        return uuid4()
```

#### POST - Create a Maintenance

```python
def test_create_maintenance(self):
    self.maintenance_obj = self.maintenance_client.create_team_maintenance(
        name=self.maintenance_name,
        start_time="2026-07-08T18:06:00",
        end_time="2026-07-08T18:06:00",
        service_ids=[],
    )
```

#### GET - Get all Maintenances

```python
def test_get_maintenance_by_id(self):
    get_maintenance_by_id = self.maintenance_client.get_maintenance_by_id(
            maintenance_id=self.maintenance_obj.unique_id
        )
```

#### PATCH - Update a Maintenance

```python
def test_update_maintenance(self):
    update_maintenance = self.maintenance_client.update_maintenance(
        maintenance_id=self.maintenance_obj,
        name="Updated Maintenance Name",
        start_time="2026-07-08T18:06:00",
        end_time="2026-07-08T18:06:00",
        service_ids=[],
    )
```

#### DEL - Delete a Maintenance

```python
def test_delete_maintenance(self):
    delete_maintenance = self.maintenance_client.delete_maintenance(
        maintenance_id=self.maintenance_obj
    )
```

## Incidents

What is an Incident??

An incident on Zenduty is an event that is not part of usual operations, and that disrupts operational processes within a Service that is owned by a team. Incidents can be automatically created by an alert integration within the service or manually by a user.

An incident on Zenduty has three states:

Triggered: Triggered is the first state of the incident. Zenduty will continue escalating the alert, depending on the escalation policy, as long as the incident is in the Triggered state.
Acknowledged: When an incident is acknowledged by a user, Zenduty stops all further escalations.
Resolved: Marking an incident as resolved implies that the incident has been remediated. Incidents can be resolved automatically by the service integration that created it, or manually by a user.

```python
class SDKIncidentsClient(SDKTestingClient):
    def __init__(self):
        super().__init__()
        self.incident_client = IncidentClient(client=self.client)
        self.incident_name = f"Incident - {self.datetime_timestamp}"
        self.incident_notes = f"Incident Notes - {self.datetime_timestamp}"
        self.incident_tags = f"Incident Tags - {self.datetime_timestamp}"

        self.service_client = SDKServicesClient()


    def generate_uuid(self):
        return uuid4()
```

#### POST - Create an Incident

```python
def create_incident(self):
    create_incident = self.incident_client.create_incident(
        title=self.incident_name, service=<unique_id of a service>
    )
```

#### POST - Create an Incident Note

NOTE: Here we are creating a note client using incident object, meaning it is important to first execute create incident before running this function.

```python
def test_create_note(self):
    # to create a notes functions
    self.note_client = self.incident_client.get_note_client(
        incident=self.incident_obj
    )

    self.incident_note_obj = self.note_client.create_incident_note(
        note=self.incident_notes
    )
```

#### GET - Get all Incident Notes

```python
def test_get_all_incident_notes(self):
    get_all_incident_notes = self.note_client.get_all_incident_notes()
```

#### GET - Get Incident note by id

```python
def test_get_incident_by_note_id(self):
    get_incident_note_by_id = self.note_client.get_incident_note_by_id(
        incident_note_unique_id=self.incident_note_obj.unique_id
    )
```

#### PATCH - Update an Incident note

```python
def test_update_incident_note(self):
    update_incident_note = self.note_client.update_incident_note(
        incident_note=self.incident_note_obj,
        note="Updated Incident Note",
    )
```

#### DEL - Delete an Incident note

```python
def test_delete_incident_note(self):
    delete_incident_note = self.note_client.delete_incident_note(
        incident_note=self.incident_note_obj
    )
```

#### POST - Create an Incident Tag

NOTE: All the functions below require a tag client to be made, There we must run this function before executing any incident tags functions.

```python
def test_create_tag_client(self):
    self.tag_client = self.incident_client.get_tags_client(self.incident_obj)
```

#### GET - Get all Incident Tags

```python
def test_get_all_tags(self):
    get_all_tags = self.tag_client.get_all_tags()
    return get_all_tags
```

#### GET - Get all Incidents

```python
def test_get_all_incidents(self):
    get_all_incidents = self.incident_client.get_all_incidents(page=1)
    return get_all_incidents
```

#### GET - Get Alerts of Incidents

```python
def test_get_alert_on_incidents(self):
    get_alerts_by_incident = self.incident_client.get_alerts_for_incident(
        incident_number=self.incident_obj.incident_number
    )
```

#### PATCH - Update an Incident

```python
def test_update_incident(self):
    update_incident = self.incident_client.update_incident(
        incident_id=self.incident_obj.unique_id,
        title="Updated Incident Name",
        status=3,
        service="a91a3a00-8de9-472c-ad2e-61e7c89db062",
    )
```

## Postmortem

```python
class SDKPostMortemClient(SDKTeamsClient):
    def __init__(self):
        super().__init__()
        self.uuid = self.generate_uuid()
        self.teams_client = TeamsClient(client=self.client)
        self.team_obj = self.teams_client.create_team(name=f"Post Mortem Team - {self.datetime_timestamp}")


        self.incident_client = IncidentClient(client=self.client)
        self.incident_name = f"Incident - {self.datetime_timestamp}"

        self.postmortem_client = self.teams_client.get_postmortem_client(
            self.team_obj
        )

        self.postmortem_name = f"Postmortem - {self.datetime_timestamp}"

    def generate_uuid(self):
        return uuid4()
```

#### POST - Create a Postmortem

```python
def test_create_postmortem(self):
    # create new service
    self.service_client = SDKServicesClient()
    self.service_obj = self.service_client.test_create_service()

    # Create the Incident
    create_incident = self.incident_client.create_incident(
        title=self.incident_name, service=self.service_obj.unique_id
    )

    # Create the Postmortem
    self.postmortem_obj= self.postmortem_client.create_postmortem(
        author="43b2493a-58e9-4454-9fe5-4",
        incidents=[create_incident.unique_id],
        title="Test Postmortem",
    )
```

#### GET - Get postmortem by id

```python
def test_get_postmortem_by_id(self):
    self.postmortem_by_id = self.postmortem_client.get_postmortem_by_id(
        postmortem_id=self.postmortem_obj.unique_id
    )
```

#### PATCH - Update a postmortem

```python
def test_update_postmortem(self):
    update_postmortem = self.postmortem_client.update_postmortem(
        self.postmortem_obj,
        author="43b2493a-58e9-4454-9fe5-4",
        incidents=[],
        title="Test Postmortem Updated",
    )

```

#### DEL - Delete a postmortem

```python
def test_delete_postmortem(self):
    delete_postmortem = self.postmortem_client.delete_postmortem(
        self.postmortem_obj
    )
```

## Priorities

```python
class SDKPrioritiesClient(SDKTeamsClient):
    def __init__(self):
        super().__init__()
        self.uuid = self.generate_uuid()
        self.teams_client = TeamsClient(client=self.client)

        self.team_obj = self.teams_client.create_team(name=f"Post Mortem Team - {self.datetime_timestamp}")

        self.priority_client = self.teams_client.get_priority_client(self.team_obj)
        self.priority_name = f"Priority - {self.datetime_timestamp}"

    def generate_uuid(self):
        return uuid4()
```

#### POST - Create a priority

```python
def test_create_priority(self):
    self.priority_obj = self.priority_client.create_priority(
        name=self.priority_name,
        description="Priority Description",
        color="red",
    )
```

#### GET - Get all priorities

```python
def test_get_all_priorities(self):
    get_all_priorities = self.priority_client.get_all_priorities()
    return get_all_priorities
```

#### GET - Get priorities by ID

```python
def test_get_priority_by_id(self):
    self.priority_by_id = self.priority_client.get_priority_by_id(
        priority_id=self.priority_obj.unique_id
    )
```

#### PATCH - Update the priority

```python
def test_update_priority(self):
    update_priority = self.priority_client.update_priority(
        self.priority_obj,
        name="Test Priority Updated",
        description="Test Priority",
    )
```

#### DEL - Delete a priority

```python
def test_delete_priority(self):
    delete_priority = self.priority_client.delete_priority(self.priority_obj)
```

## Roles

```python
class SDKRolesClient(SDKTeamsClient):
    def __init__(self):
        super().__init__()
        self.uuid = self.generate_uuid()
        self.teams_client = TeamsClient(client=self.client)
        self.team_obj = self.teams_client.create_team(name=f"Roles Team - {self.datetime_timestamp}")

        self.role_client = self.teams_client.get_incident_role_client(self.team_obj)
        self.role_name = f"Role - {self.datetime_timestamp}"

    def generate_uuid(self):
        return uuid4()
```

#### POST - Create a Role

```python
def test_create_role(self):
    self.role_obj = self.role_client.create_incident_role(
        title="Test Role",
        description="Test Role",
        rank=2,
    )
```

#### GET - Get incident role by id

```python
def test_get_role_by_id(self):
    self.get_role_by_id = self.role_client.get_incident_role_by_id(
        role_id=self.role_obj.unique_id
    )
```

#### PATCH - Update an incident role

```python
def test_update_role(self):
    self.update_role = self.role_client.update_incident_role(
        role=self.role_obj,
        title="Test Role Updated",
    )
```

#### DEL - Delete an incident role

```python
def test_delete_role(self):
    self.delete_role = self.role_client.delete_incident_role(
        role=self.role_obj
    )
```

## Services

```python
class SDKServicesClient(SDKTeamsClient):
    def __init__(self):
        super().__init__()
        # Making the Teams Client
        self.teams_client = TeamsClient(client=self.client)
        self.team_obj = self.teams_client.create_team(name=f"Services Team - {self.datetime_timestamp}")


        # Making the Service Client
        self.service_client = self.teams_client.get_service_client(self.team_obj)

        self.escalation_policy_client = self.teams_client.get_escalation_policy_client(
            self.team_obj
        )
        self.priority_client = self.teams_client.get_priority_client(self.team_obj)
        self.sla_client = self.teams_client.get_sla_client(self.team_obj)

        # Making the names
        self.ep_name = f"EP - {self.datetime_timestamp}"
        self.priority_name = f"Priority - {self.datetime_timestamp}"
        self.sla_name = f"SLA - {self.datetime_timestamp}"
        self.service_name = f"Service - {self.datetime_timestamp}"


        self.account_member_client = AccountMemberClient(client=self.client)
        self.test_email = f"john.doe.{random.randint(2,10000000000000000000000)}@zenduty.com"
        self.team_member_obj = self.account_member_client.invite(
            team_id=self.team_obj.unique_id,
            email=self.test_email,
            first_name="Test",
            last_name="User",
            role=2,
        )
```

#### POST - Create a Service

```python
def test_create_service(self):
    # Create the escalation policy
    self.rule_build = [
        {
            "delay": 0,
            "targets": [
                {"target_type": 2, "target_id": self.team_member_obj.user.username}
            ],
            "position": 1,
        }
    ]
    create_escalation_policy = self.escalation_policy_client.create_esp(
        self.ep_name, rules=self.rule_build
    )


    # Create the Priority
    create_priority = self.priority_client.create_priority(
        name=self.priority_name,
        description="Priority Description",
        color="red",
    )



    # Create the SLA
    create_sla = self.sla_client.create_sla(name="Test SLA", escalations=[])

    # Finally create the service
    create_service = self.service_client.create_service(
        name=f"Test Service - {self.datetime_timestamp}",
        escalation_policy=create_escalation_policy.unique_id,
        team_priority=create_priority.unique_id,
        sla=create_sla.unique_id,
    )

    return create_service
```

## Integrations

#### POST - Create an integration

```python
integration_client = service_client.get_integration_client(svc=<unique_id of a service>)

create_integration = integration_client.create_intg( name="Test Integration", summary="Test Integration", application=<unique_id of an application>)

```

#### GET - Get all integrations

```python
all_integrations = integration_client.get_all_integrations()
```

#### GET - Get integration by id

```python
integration_by_id = integration_client.get_intg_by_id(intg=<unique_id of an integration>)
```

#### PATCH - Update an integration

```python
update_integration = integration_client.update_intg(intg=<unique_id of an integration>, name="Test Integration Updated", application=<unique_id of an application>)
```

#### DEL - Delete an integration

```python
delete_integration = integration_client.delete_intg(intg=<unique_id of an integration>)
```

## SLA

```python
class SDKSLAClient(SDKTeamsClient):
    def __init__(self):
        super().__init__()
        self.teams_client = TeamsClient(client=self.client)
        self.account_member_client = AccountMemberClient(client=self.client)
        self.team_obj = self.teams_client.create_team(name=f"Integration Team - {self.datetime_timestamp}")

        self.sla_client = self.teams_client.get_sla_client(self.team_obj)
```

#### POST - Create an SLA

```python
def test_create_sla(self):
    self.sla_obj = self.sla_client.create_sla(name="Test SLA", escalations=[])
```

#### GET - Get SLA by id

```python
def test_get_sla_by_id(self):
    sla_by_id = self.sla_client.get_sla_by_id(sla_id=self.sla_obj.unique_id)
```

#### PATCH - Update SLA

```python
def test_update_sla(self):
    update_sla = self.sla_client.update_sla(sla=self.sla_obj, name="Test SLA Updated", escalations=[])
```

#### DEL - Delete SLA

```python
def test_delete_sla(self):
    delete_sla = self.sla_client.delete_sla(sla=self.sla_obj)
```

## Tags

```python
class SDKTagClient(SDKTeamsClient):
    def __init__(self):
        super().__init__()
        self.teams_client = TeamsClient(client=self.client)
        self.account_member_client = AccountMemberClient(client=self.client)
        self.team_obj = self.teams_client.create_team(name=f"Integration Team - {self.datetime_timestamp}")

        self.tag_client = self.teams_client.get_tag_client(self.team_obj)
```

#### POST - Create a tag

```python
def test_create_tag(self):
    self.tag_obj = self.tag_client.create_tag(name=f"Tag name - {self.datetime_timestamp}", color="red")
```

#### GET - Get all tags

```python
def test_get_all_tags(self):
    get_all_tags = self.tag_client.get_all_tags()
```

#### GET - GET tag by id

```python
def test_get_tag_by_id(self):
    get_tag = self.tag_client.get_tag_by_id(tags_id = self.tag_obj.unique_id)
```

#### PATCH - Update tag by id

```python
def test_update_tag(self):
    update_tag = self.tag_client.update_tag(tag=self.tag_obj, name="updated name", color="green")
```

#### DEL - Delete tag

```python
def test_delete_tag(self):
    delete_tag = self.tag_client.delete_tag(tag=self.tag_obj)
```

## Task templates

```python
class SDKTemplateClient(SDKTeamsClient):
    def __init__(self):
        super().__init__()
        self.teams_client = TeamsClient(client=self.client)
        self.account_member_client = AccountMemberClient(client=self.client)
        self.team_obj = self.teams_client.create_team(name=f"Integration Team - {self.datetime_timestamp}")

        self.tag_client = self.teams_client.get_tag_client(self.team_obj)

        self.task_template_client = self.teams_client.get_task_template_client(self.team_obj)
```

#### POST - Create a task template

```python
def test_create_template(self):
    self.task_template_obj = self.task_template_client.create_task_template(
        name="Test Task Template", summary="Test Task Template"
        )
```

#### GET - Get all task templates

```python
def test_get_all_task_templates(self):
    get_all_task_templates = self.task_template_client.get_all_task_template()
```

#### GET - Get task templates by id

```python
def test_get_task_template_by_id(self):
    get_task_template_by_id =  self.task_template_client.get_task_template_by_id(
        task_template_id=self.task_template_obj.unique_id
    )
```

#### PATCH - Update the task template

```python
def test_update_task_template(self):
    update_task_template = self.task_template_client.update_task_template(
        task_template = self.task_template_obj, name="Test Task Template Updated"
    )
```

#### DEL - Delete the task template

```python
def test_delete_task_template(self):
    delete_task_template = self.task_template_client.delete_task_template(task_template = self.task_template_obj)
```

# Running tests

There is a sample skeleton code in tests/. Add your access token to it and modify the object and function name for testing purposes.

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
