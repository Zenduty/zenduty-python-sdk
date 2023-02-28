from datetime import datetime, timedelta
from uuid import UUID


class RuleBuilder:
    def __init__(self):
        self.rules = []

    def add_rule(self, delay: timedelta, postition: int, targets: list[dict]):
        """Add a rule to the rules list

        Args:
            delay (timedelta): delay to add
            postition (int): postition of the rule
            targets (list[dict]): Targets to add to the rule
        """
        self.rules.append(
            {
                "delay": delay.total_seconds(),
                "targets": targets,
                "postition": postition,
            }
        )
        return self

    def build(self) -> list[dict]:
        """Return a list of created rules

        Returns:
            list[dict]: List of created rules
        """
        return self.rules
