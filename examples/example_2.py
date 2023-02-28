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
    _note = note_client.create_incident_note(note=note)
    print("Note created...")
    print(_note)
