from typing import List

from zenduty.apiV2.serializer import JsonSerializable


class EscalationPolicy(JsonSerializable):
    name: str
    summary: str
    description: str
    unique_id: str
    repeat_policy: int
    move_to_next: bool
    global_ep: bool

    def __init__(
        self,
        name: str,
        summary: str,
        description: str,
        unique_id: str,
        repeat_policy: int,
        move_to_next: bool,
        global_ep: bool,
    ) -> None:
        self.name = name
        self.summary = summary
        self.description = description
        self.unique_id = unique_id
        self.repeat_policy = repeat_policy
        self.move_to_next = move_to_next
        self.global_ep = global_ep


class Team(JsonSerializable):
    unique_id: str
    name: str

    def __init__(self, unique_id: str, name: str) -> None:
        self.unique_id = unique_id
        self.name = name


class User(JsonSerializable):
    username: str
    first_name: str
    email: str
    last_name: str

    def __init__(
        self, username: str, first_name: str, email: str, last_name: str
    ) -> None:
        self.username = username
        self.first_name = first_name
        self.email = email
        self.last_name = last_name


class OnCall(JsonSerializable):
    escalation_policy: EscalationPolicy
    team: Team
    users: List[User]

    def __init__(
        self, escalation_policy: EscalationPolicy, team: Team, users: list[User]
    ) -> None:
        self.escalation_policy = (
            escalation_policy
            if isinstance(escalation_policy, EscalationPolicy)
            else EscalationPolicy(**escalation_policy)
        )
        self.team = team if isinstance(team, Team) else Team(**team)
        self.users = (
            users if type(users) is list[User] else [User(**user) for user in users]
        )
