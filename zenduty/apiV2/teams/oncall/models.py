import logging
from uuid import UUID
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
        **kwargs
    ) -> None:
        self.name = name
        self.summary = summary
        self.description = description
        self.unique_id = unique_id
        self.repeat_policy = repeat_policy
        self.move_to_next = move_to_next
        self.global_ep = global_ep
        if kwargs:
            logging.info(f"We have unexpected return values for {self.__class__.__name__}: {list(kwargs.keys())}")


class Team(JsonSerializable):
    unique_id: str
    name: str

    def __init__(self, unique_id: str, name: str, **kwargs) -> None:
        self.unique_id = unique_id
        self.name = name
        if kwargs:
            logging.info(f"We have unexpected return values for {self.__class__.__name__}: {list(kwargs.keys())}")


class User(JsonSerializable):
    username: str
    first_name: str
    email: str
    last_name: str

    def __init__(
        self, username: str, first_name: str, email: str, last_name: str, **kwargs
    ) -> None:
        self.username = username
        self.first_name = first_name
        self.email = email
        self.last_name = last_name
        if kwargs:
            logging.info(f"We have unexpected return values for {self.__class__.__name__}: {list(kwargs.keys())}")


class OnCall(JsonSerializable):
    escalation_policy: EscalationPolicy
    team: Team
    users: List[User]

    def __init__(
        self,
        escalation_policy: EscalationPolicy,
        team: Team,
        users: list[User],
        **kwargs
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
        if kwargs:
            logging.info(f"We have unexpected return values for {self.__class__.__name__}: {list(kwargs.keys())}")


class OnCallV2(JsonSerializable):
    class OnCallUsers(JsonSerializable):
        ep_rule: UUID
        position: int
        delay: int
        oncalls: List[User]

        def __init__(
            self,
            ep_rule: str,
            position: int,
            delay: int,
            oncalls: list,
            **kwargs
        ) -> None:
            self.ep_rule = (
                ep_rule
                if isinstance(ep_rule, UUID)
                else UUID(ep_rule)
            )
            self.position = position
            self.delay = delay
            self.users = (
                oncalls if type(oncalls) is list[User] else [User(**user) for user in oncalls]
            )
            if kwargs:
                logging.info(f"We have unexpected return values for {self.__class__.__name__}: {list(kwargs.keys())}")

    unique_id: UUID
    name: str
    oncalls: List[OnCallUsers]
    def __init__(
            self,
            unique_id: str,
            name: int,
            oncalls: list,
            **kwargs
        ) -> None:
        self.ep_unique_id = (
            unique_id
            if isinstance(unique_id, UUID)
            else UUID(unique_id)
        )
        self.ep_name = name
        self.oncalls = (
            oncalls if type(oncalls) is list[self.OnCallUsers] else [self.OnCallUsers(**user) for user in oncalls]
        )
        if kwargs:
            logging.info(f"We have unexpected return values for {self.__class__.__name__}: {list(kwargs.keys())}")