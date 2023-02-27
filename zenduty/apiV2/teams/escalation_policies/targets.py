from datetime import datetime, timedelta
from uuid import UUID


class TargetBuilder:
    def __init__(self):
        self.targets = []

    def add_target(self, target_type: str, target_id: str):
        """Add a target to the targets

        Args:
            target_type (str): target An integer that represents the Escalation Policy Rule Target object's target_type. 1 for Schedule and 2 for User
            target_id (str): A system-generated string that represents Escalation Policy Rule Target object's target_id. If target_type is 1 then target_id is Schedule object's unique_id and if target_type is 2 then target_id is User object's username
        """
        self.targets.append({"target_type": target_type, "target_id": target_id})
        return self

    def build(self) -> list[dict]:
        """Builds a list of targets

        Returns:
            list[dict]: list of targets
        """
        return self.targets
