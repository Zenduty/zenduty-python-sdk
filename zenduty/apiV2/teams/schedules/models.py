from datetime import datetime
from uuid import UUID
from typing import Union
import json
from ...serializer import serialize


class Restriction(object):
    duration: int
    start_day_of_week: int
    start_time_of_day: datetime
    unique_id: UUID

    def __init__(
        self,
        duration: int,
        start_day_of_week: int,
        start_time_of_day: str,
        unique_id: Union[UUID, str],
    ) -> None:
        self.duration = duration
        self.start_day_of_week = start_day_of_week
        self.start_time_of_day = start_time_of_day
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)

    def toJSON(self):
        return json.dumps(self, default=serialize, sort_keys=True, indent=4)


class User(object):
    user: str
    position: int
    unique_id: UUID

    def __init__(self, user: str, position: int, unique_id: Union[UUID, str]) -> None:
        self.user = user
        self.position = position
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)

    def toJSON(self):
        return json.dumps(self, default=serialize, sort_keys=True, indent=4)


class Layer(object):
    shift_length: int
    restrictions: list[Restriction]
    name: str
    users: list[User]
    rotation_start_time: datetime
    rotation_end_time: datetime
    unique_id: UUID
    last_edited: datetime
    restriction_type: int
    is_active: bool

    def __init__(
        self,
        shift_length: int,
        restrictions: Union[list[Restriction], list[dict]],
        name: str,
        users: Union[list[User], list[dict]],
        rotation_start_time: Union[str, datetime],
        rotation_end_time: Union[str, datetime],
        unique_id: Union[UUID, str],
        last_edited: Union[str, datetime, None],
        restriction_type: int,
        is_active: bool,
    ) -> None:
        self.shift_length = shift_length
        self.restrictions = (
            restrictions
            if type(restrictions) is list[dict]
            else [Restriction(**r) for r in restrictions]
        )
        self.name = name
        self.users = users if type(users) is list[dict] else [User(**r) for r in users]
        self.rotation_start_time = (
            rotation_start_time
            if type(rotation_start_time) is datetime
            else datetime.fromisoformat(rotation_start_time.replace("Z", "+05:30"))
        )
        self.rotation_end_time = (
            rotation_end_time
            if type(rotation_end_time) is datetime
            else datetime.fromisoformat(rotation_end_time.replace("Z", "+05:30"))
        )
        self.unique_id = unique_id
        self.last_edited = (
            last_edited
            if type(last_edited) is datetime or last_edited is None
            else datetime.fromisoformat(last_edited.replace("Z", "+05:30"))
        )
        self.restriction_type = restriction_type
        self.is_active = is_active

    def toJSON(self):
        return json.dumps(self, default=serialize, sort_keys=True, indent=4)


class Override(object):
    name: str
    user: str
    start_time: datetime
    end_time: datetime
    unique_id: UUID

    def __init__(
        self,
        name: str,
        user: str,
        start_time: Union[str, datetime],
        end_time: Union[str, datetime],
        unique_id: Union[UUID, str],
    ) -> None:
        self.name = name
        self.user = user
        self.start_time = (
            start_time
            if type(start_time) is datetime
            else datetime.fromisoformat(start_time.replace("Z", "+05:30"))
        )
        self.end_time = (
            end_time
            if type(end_time) is datetime
            else datetime.fromisoformat(end_time.replace("Z", "+05:30"))
        )
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)

    def toJSON(self):
        return json.dumps(self, default=serialize, sort_keys=True, indent=4)


class Schedule(object):
    name: str
    summary: str
    description: str
    time_zone: str
    team: UUID
    layers: list[Layer]
    overrides: list[Override]
    unique_id: UUID

    def __init__(
        self,
        name: str,
        summary: str,
        description: str,
        time_zone: str,
        team: Union[str, UUID],
        layers: Union[list[dict], list[Layer]],
        overrides: Union[list[Override], list[dict]],
        unique_id: Union[UUID, str],
    ) -> None:
        self.name = name
        self.summary = summary
        self.description = description
        self.time_zone = time_zone
        self.team = team if type(team) is UUID else UUID(team)
        self.layers = (
            layers if type(layers) is list[dict] else [Layer(**l) for l in layers]
        )
        self.overrides = (
            overrides
            if type(overrides) is list[dict]
            else [Override(**over) for over in overrides]
        )
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)

    def toJSON(self):
        return json.dumps(self, default=serialize, sort_keys=True, indent=4)
