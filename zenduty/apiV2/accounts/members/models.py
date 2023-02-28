from typing import Optional
from uuid import UUID
from datetime import datetime

from zenduty.apiV2.serializer import JsonSerializable


class User(JsonSerializable):
    username: str
    first_name: str
    last_name: str
    email: str

    def __init__(
        self, username: str, first_name: str, last_name: str, email: str
    ) -> None:
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


class AccountMember(JsonSerializable):
    unique_id: UUID
    time_zone: str
    user: User
    joining_date: datetime
    role: int
    is_verified: bool
    team: UUID

    def __init__(
        self,
        unique_id: UUID,
        time_zone: str,
        user: User,
        joining_date: datetime,
        role: int,
        is_verified: bool,
        team: Optional[UUID] = None,
        custom_role_id: Optional[str] = None,
    ) -> None:
        self.unique_id = unique_id if isinstance(unique_id, UUID) else unique_id
        self.time_zone = time_zone
        self.user = User(**user)
        self.joining_date = (
            joining_date if isinstance(joining_date, datetime) else joining_date
        )
        self.role = role
        self.is_verified = is_verified
        self.team = team if isinstance(team, UUID) or team is None else UUID(team)
        self.custom_role_id = custom_role_id
