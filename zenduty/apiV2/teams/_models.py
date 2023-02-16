from uuid import UUID
from datetime import datetime
from typing import Union
import json
from ..serializer import serialize


class User(object):
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

    def toJSON(self):
        return json.dumps(self, default=serialize, sort_keys=True, indent=4)


class Member(object):
    unique_id: UUID
    team: UUID
    user: User
    joining_date: datetime
    role: int

    def __init__(
        self,
        unique_id: Union[UUID, str],
        team: Union[UUID, str],
        user: Union[User, dict],
        joining_date: Union[datetime, str],
        role: int,
    ) -> None:
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)
        self.team = team if type(team) is not str else UUID(team)
        self.user = user if type(user) is User else User(**user)
        self.joining_date = (
            joining_date
            if type(joining_date) is datetime
            else datetime.fromisoformat(joining_date.replace("Z", "+05:30"))
        )
        self.role = role


class Role(object):
    unique_id: UUID
    team: UUID
    title: str
    description: str
    creation_date: datetime
    rank: int

    def __init__(
        self,
        unique_id: Union[UUID, str],
        team: Union[UUID, str],
        title: str,
        description: str,
        creation_date: Union[datetime, str],
        rank: int,
    ) -> None:
        self.unique_id = unique_id if type(unique_id) is UUID else UUID(unique_id)
        self.team = team if type(team) is not str else UUID(team)
        self.title = title
        self.description = description
        self.creation_date = (
            creation_date
            if type(creation_date) is datetime
            else datetime.fromisoformat(creation_date.replace("Z", "+05:30"))
        )
        self.rank = rank


class Team(object):
    unique_id: UUID
    name: str
    account: UUID
    creation_date: datetime
    members: list[Member]
    owner: str
    roles: list[Role]
    private: bool

    def __init__(
        self,
        unique_id: Union[UUID, str],
        name: str,
        account: Union[UUID, str],
        creation_date: Union[datetime, str],
        members: Union[list[Member], list[dict]],
        owner: str,
        roles: Union[list[Role], list[dict]],
        private: bool,
        account_permissions: list[dict],
    ) -> None:
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)
        self.name = name
        self.account = account if type(account) is not str else UUID(account)
        self.creation_date = (
            creation_date
            if type(creation_date) is datetime
            else datetime.fromisoformat(creation_date.replace("Z", "+05:30"))
        )
        self.members = (
            members if type(members) is list[Member] else [Member(**m) for m in members]
        )
        self.owner = owner
        self.roles = roles if type(roles) is list[Role] else [Role(**r) for r in roles]
        self.private = private
