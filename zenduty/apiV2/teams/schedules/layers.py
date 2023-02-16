from .models import Layer, User, Restriction
from datetime import datetime, timedelta


class LayersBuilder(object):
    def __init__(self):
        self.layers = []

    def add_layer(
        self,
        name: str,
        users: list[str],
        restrictions: list[Restriction],
        rotation_start_time: datetime,
        rotation_end_time: datetime,
        shift_length: timedelta,
        restriction_type: int,
        timezone: str,
    ) -> object:
        self.layers.append(
            {
                "name": name,
                "users": [{"user": user} for user in users],
                "restrictions": [r.__dict__ for r in restrictions],
                "rotation_start_time": rotation_start_time.isoformat(),
                "rotation_end_time": rotation_end_time.isoformat(),
                "shift_length": int(shift_length.total_seconds()),
                "restriction_type": restriction_type,
                "time_zone": timezone,
            }
        )
        return self

    def build(self) -> list[dict]:
        return self.layers
