from datetime import datetime


class OverrideBuilder:
    def __init__(self):
        self.override = []

    def add_override(
        self, name: str, user: str, start_time: datetime, end_time: datetime
    ):
        """Add a new override to the OverrideBuilder

        Args:
            name (str): A string that represents the Schedule Overrides object's name
            user (str): A string that represents the User object's username
            start_time (datetime): A fromatted string that represents the Schedule Overrides object's start_time
            end_time (datetime): A fromatted string that represents the Schedule Overrides object's end_time
        """
        self.override.append(
            {
                "name": name,
                "user": user,
                "start_time": start_time.isoformat(),
                "end_time": end_time.isoformat(),
            }
        )
        return self

    def build(self) -> list[dict]:
        """Returns a list of created overrides.

        Returns:
            list[dict]: List of overrides.
        """
        return self.override
