from uuid import UUID
from datetime import datetime
from typing import List, Optional
from ...serializer import JsonSerializable


class Service(JsonSerializable):
    unique_id: UUID
    service: UUID

    def __init__(self, unique_id: Optional[UUID], service: UUID) -> None:
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)
        self.service = service if type(service) is not str else UUID(service)


class TeamMaintenance(JsonSerializable):
    unique_id: UUID
    start_time: datetime
    end_time: datetime
    repeat_interval: int
    services: List[Service]
    creation_date: datetime
    name: str
    time_zone: str
    repeat_until: Optional[datetime]

    def __init__(
        self,
        unique_id: UUID,
        start_time: datetime,
        end_time: datetime,
        repeat_interval: int,
        services: List[Service],
        creation_date: datetime,
        name: str,
        time_zone: str,
        repeat_until: Optional[int],
    ) -> None:
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)
        self.start_time = (
            start_time
            if type(start_time) is datetime
            else datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        )
        self.end_time = (
            end_time
            if type(end_time) is datetime
            else datetime.fromisoformat(end_time.replace("Z", "+00:00"))
        )
        self.repeat_interval = repeat_interval
        self.services = (
            services
            if type(services) is list[Service]
            else [Service(**svc) for svc in services]
        )
        self.creation_date = (
            creation_date
            if type(creation_date) is datetime
            else datetime.fromisoformat(creation_date.replace("Z", "+00:00"))
        )
        self.name = name
        self.time_zone = time_zone
        if repeat_until is not None:
            self.repeat_until = (
                repeat_until
                if type(repeat_until) is datetime or repeat_until is None
                else datetime.fromisoformat(repeat_until.replace("Z", "+00:00"))
            )
