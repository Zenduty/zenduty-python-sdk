from .models import Layer, User, Restriction
from datetime import datetime, timedelta

from ...serializer import JsonSerializable


class LayersBuilder(JsonSerializable):
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
        """add a layer to the layers

        Args:
            name (str): A string that represents the Schedule Layer object's name
            users (list[str]): List of system-generated strings that represents the User object's username
            restrictions (list[Restriction]): An array of Schedule Layer Restriction objects
            rotation_start_time (datetime): A formatted string that represents the Schedule Layer object's rotation_start_time
            rotation_end_time (datetime): A formatted string that represents the Schedule Layer object's rotation_end_time
            shift_length (timedelta): represents the Schedule Layer object's shift_length
            restriction_type (int): An integer that represents Schedule Layer object's restriction_type. 0 for no restriction, 1 for daily restrictions and 2 for weekly restrictions
            timezone (str): Timezone for the layer
        """
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
        """Returns a list of layers

        Returns:
            list[dict]: Created layers
        """
        return self.layers
