from typing import List, Any
from uuid import UUID

from zenduty.apiV2.serializer import JsonSerializable


class SLA(JsonSerializable):
    escalations: List[Any]
    unique_id: UUID
    name: str
    description: str
    is_active: bool
    conditions: str
    acknowledge_time: int
    resolve_time: int
    team: int

    def __init__(
        self,
        escalations: List[Any],
        unique_id: UUID,
        name: str,
        description: str,
        is_active: bool,
        conditions: str,
        acknowledge_time: int,
        resolve_time: int,
        team: int,
    ) -> None:
        self.escalations = escalations
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)
        self.name = name
        self.description = description
        self.is_active = is_active
        self.conditions = conditions
        self.acknowledge_time = acknowledge_time
        self.resolve_time = resolve_time
        self.team = team
