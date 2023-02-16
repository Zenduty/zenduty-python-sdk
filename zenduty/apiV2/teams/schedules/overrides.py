from .models import Layer, User, Restriction
from datetime import datetime
class OverrideBuilder:
    def __init__(self):
        self.override = []

    def add_override(self, name: str, user: str,start_time: datetime, end_time:datetime ):
        self.override.append({
            "name": name,
            "user": user,
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat(),
        })
        return self
    
    def build(self) -> list[dict]:
        return self.override
