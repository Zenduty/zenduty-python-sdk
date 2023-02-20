from datetime import datetime
from typing import List, Any, Optional
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
    creation_date: datetime

    def __init__(
        self,
        unique_id: UUID,
        name: str,
        is_active: bool,
        acknowledge_time: int,
        resolve_time: int,
        creation_date: Optional[datetime] = None,
        escalations: Optional[List[Any]] = [],
        description: Optional[str] = None,
        conditions: Optional[str] = None,
        team: Optional[int] = None,
        summary: Optional[str] = "",
        time_zone: Optional[str] = None,
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
        self.creation_date = creation_date if isinstance(creation_date, datetime) or creation_date is None else datetime.fromisoformat(creation_date.replace("Z", "+00:00"))
        self.summary = summary