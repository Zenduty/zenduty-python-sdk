from datetime import datetime, timedelta
from uuid import UUID


class RuleBuilder:
    def __init__(self):
        self.rules = []

    def add_rule(self, delay: timedelta, postition: int, targets: list[dict]):
        self.rules.append(
            {
                "delay": delay.total_seconds(),
                "targets": targets,
                "postition": postition,
            }
        )
        return self

    def build(self) -> list[dict]:
        return self.rules
