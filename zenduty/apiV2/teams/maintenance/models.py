from uuid import UUID
from datetime import datetime
from typing import List, Optional


class Service:
    unique_id: UUID
    service: UUID

    def __init__(self, unique_id: Optional[UUID], service: UUID) -> None:
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)
        self.service = service if type(service) is not str else UUID(service)


class TeamMaintenance:
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
        repeat_until: Optional[datetime],
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
        self.services = services
        self.creation_date = (
            creation_date
            if type(creation_date) is datetime
            else datetime.fromisoformat(creation_date.replace("Z", "+00:00"))
        )
        self.name = name
        self.time_zone = time_zone
        self.repeat_until = (
            repeat_interval
            if type(repeat_interval) is datetime and repeat_until is not None
            else datetime.fromisoformat(repeat_interval.replace("Z", "+00:00"))
        )
