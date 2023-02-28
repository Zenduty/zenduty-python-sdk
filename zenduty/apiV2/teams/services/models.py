from datetime import datetime
from uuid import UUID
import json
from ...serializer import serialize, JsonSerializable


class Service(JsonSerializable):
    name: str
    creation_date: datetime
    summary: str
    description: str
    unique_id: UUID
    auto_resolve_timeout: int
    created_by: str
    team_priority: UUID
    task_template: UUID
    acknowledgement_timeout: int
    status: int
    escalation_policy: UUID
    team: UUID
    sla: UUID
    under_maintenance: bool
    collation: int
    collation_time: int

    def __init__(
        self,
        name: str,
        creation_date: datetime,
        summary: str,
        description: str,
        unique_id: UUID,
        auto_resolve_timeout: int,
        created_by: str,
        team_priority: UUID,
        task_template: UUID,
        acknowledgement_timeout: int,
        status: int,
        escalation_policy: UUID,
        team: UUID,
        sla: UUID,
        under_maintenance: bool,
        collation: int,
        collation_time: int,
        **kwargs
    ) -> None:
        self.name = name
        self.creation_date = (
            creation_date
            if type(creation_date) is datetime
            else datetime.fromisoformat(creation_date.replace("Z", "+00:00"))
        )
        self.summary = summary
        self.description = description
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)
        self.auto_resolve_timeout = auto_resolve_timeout
        self.created_by = created_by
        self.team_priority = (
            team_priority if type(team_priority) is not str else UUID(team_priority)
        )
        self.task_template = (
            task_template if type(task_template) is not str else UUID(task_template)
        )
        self.acknowledgement_timeout = acknowledgement_timeout
        self.status = status
        self.escalation_policy = (
            escalation_policy
            if type(escalation_policy) is not str
            else UUID(escalation_policy)
        )
        self.team = team if type(team) is not str else UUID(team)
        self.sla = sla if type(sla) is not str else UUID(sla)
        self.under_maintenance = under_maintenance
        self.collation = collation
        self.collation_time = collation_time
        if kwargs.get("team_name", None) is not None:
            self.team_name = kwargs.get("team_name", None)

    def to_json(self):
        return json.dumps(self, default=serialize, sort_keys=True, indent=4)
