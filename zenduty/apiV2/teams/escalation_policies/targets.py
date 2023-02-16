from datetime import datetime, timedelta
from uuid import UUID


class TargetBuilder:
    def __init__(self):
        self.targets = []

    def add_target(self, target_type: str, target_id: str):
        self.targets.append({"target_type": target_type, "target_id": target_id})
        return self

    def build(self) -> list[dict]:
        return self.targets
