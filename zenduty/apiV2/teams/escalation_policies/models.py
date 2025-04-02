import json
import logging
from uuid import UUID
from typing import Union

from zenduty.apiV2.serializer import serialize, JsonSerializable



class Target(JsonSerializable):
    target_type: int
    target_id: str

    def __init__(self, target_type: int, target_id: str, **kwargs) -> None:
        self.target_type = target_type
        self.target_id = target_id
        if kwargs:
            logging.info(f'Received unexpected return values for {self.__class__.__name__}: {list(kwargs.keys())}')

    def to_json(self):
        return json.dumps(self, default=serialize, sort_keys=True, indent=4)


class AssignmentSettings(JsonSerializable):
    unique_id: UUID
    assignee_strategy: int
    assignment_index: int

    def __init__(self, unique_id: Union[UUID, str], assignee_strategy: int, assignment_index: int, **kwargs) -> None:
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)
        self.assignee_strategy = assignee_strategy
        self.assignment_index = assignment_index
        if kwargs:
            logging.info(f'Received unexpected return values for {self.__class__.__name__}: {list(kwargs.keys())}')

    def to_json(self):
        return json.dumps(self, default=serialize, sort_keys=True, indent=4)


class Rule(JsonSerializable):
    delay: int
    targets: list[Target]
    position: int
    unique_id: UUID

    def __init__(
        self,
        delay: int,
        targets: Union[list[Target], list[dict]],
        position: int,
        unique_id: Union[UUID, str],
        **kwargs
    ) -> None:
        self.delay = delay
        self.targets = targets if type(targets) is not list[dict] else [Target(**l) for l in targets]
        self.position = position
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)
        if kwargs:
            logging.info(f'Received unexpected return values for {self.__class__.__name__}: {list(kwargs.keys())}')

    def to_json(self):
        return json.dumps(self, default=serialize, sort_keys=True, indent=4)


class EscalationPolicy(JsonSerializable):
    name: str
    summary: str
    description: str
    rules: list[Rule]
    unique_id: UUID
    team: UUID
    repeat_policy: int
    move_to_next: bool
    global_ep: bool
    connections: int
    assignment_settings: AssignmentSettings

    def __init__(
        self,
        name: str,
        summary: str,
        description: str,
        rules: Union[list[Rule], list[dict]],
        unique_id: Union[UUID, str],
        team: Union[UUID, str],
        repeat_policy: int,
        move_to_next: bool,
        global_ep: bool,
        connections: int,
        assignment_settings: AssignmentSettings,
        **kwargs
    ) -> None:
        self.name = name
        self.summary = summary
        self.description = description
        self.rules = rules if type(rules) is not list[dict] else [Rule(**l) for l in rules]
        self.unique_id = unique_id if type(unique_id) is not str else UUID(unique_id)
        self.team = team if type(team) is not str else UUID(team)
        self.repeat_policy = repeat_policy
        self.move_to_next = move_to_next
        self.global_ep = global_ep
        self.connections = connections
        self.assignment_settings = assignment_settings
        if kwargs:
            logging.info(f'Received unexpected return values for {self.__class__.__name__}: {list(kwargs.keys())}')

    def to_json(self):
        return json.dumps(self, default=serialize, sort_keys=True, indent=4)
