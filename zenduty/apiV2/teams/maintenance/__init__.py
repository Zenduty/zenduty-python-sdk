import json
from typing import Optional
from uuid import UUID
from ...client import ZendutyClient, ZendutyClientRequestMethod
from .._models import Team
from .models import TeamMaintenance
from datetime import datetime


class TeamMaintenanceClient:
    def __init__(self, client: ZendutyClient, team: Team):
        self._client = client
        self._team = team

    def get_all_maintenance(self) -> list[TeamMaintenance]:
        """Get all the maintenance for the team

        Returns:
            list[TeamMaintenance]: List of all the maintenances
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/maintenance/" % str(self._team.unique_id),
            success_code=200,
        )
        return [TeamMaintenance(**r) for r in response]

    def get_maintenance_by_id(self, maintenance_id: UUID) -> TeamMaintenance:
        """Get a maintenance by ID

        Args:
            maintenance_id (UUID): ID for the maintenance to fetch

        Returns:
            TeamMaintenance: fetch a team maintenance object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/maintenance/%s/"
            % (str(self._team.unique_id), str(maintenance_id)),
            success_code=200,
        )
        return TeamMaintenance(**response)

    def create_team_maintenance(
        self,
        name: str,
        start_time: datetime,
        end_time: datetime,
        repeat_interval: int = 0,
        service_ids: list[UUID] = [],
        time_zone: str = "UTC",
        repeat_until: Optional[int] = None,
        **kwargs
    ) -> TeamMaintenance:
        """Create a new team maintenance object

        Args:
            name (str): A string that represents the Team Maintenance Mode object's name
            start_time (datetime): A formatted string that represents the Team Maintenance Mode object's start_time
            end_time (datetime): A formatted string that represents the Team Maintenance Mode object's end_time
            repeat_interval (int, optional): An integer that represents the Team Maintenance Mode object's repeat_interval. Defaults to 0.
            service_ids (list[UUID], optional): List of a system-generated string that represents the Service object's unique_id . Defaults to [].
            time_zone (str, optional): A formatted string that represents the Team Maintenance Mode object's time_zone. You can check out the time zone list here https://timezonedb.com/time-zones. Defaults to "UTC".
            repeat_until (Optional[int], optional): A formatted string that represents the Team Maintenance Mode object's repeat_until. Defaults to None.

        Returns:
            TeamMaintenance: Created TeamMaintenance object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/account/teams/%s/maintenance/" % str(self._team.unique_id),
            request_payload={
                "name": name,
                "start_time": start_time.isoformat(),
                "end_time": end_time.isoformat(),
                "repeat_interval": repeat_interval,
                "services": [{"service": svc_id} for svc_id in service_ids],
                "time_zone": time_zone,
                "repeat_until": repeat_until
                if repeat_until is None
                else repeat_until.isoformat(),
            },
            success_code=201,
        )
        return TeamMaintenance(**response)

    def update_maintenance(self, maintenance: TeamMaintenance) -> TeamMaintenance:
        """Update a team maintenance object

        Args:
            maintenance (TeamMaintenance): maintenance object to update

        Returns:
            TeamMaintenance: updated team maintenance object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint="/api/account/teams/%s/maintenance/%s/"
            % (str(self._team.unique_id), str(maintenance.unique_id)),
            request_payload=json.loads(maintenance.to_json()),
            success_code=200,
        )
        return TeamMaintenance(**response)

    def delete_maintenance(self, maintenance: TeamMaintenance) -> None:
        """Delete a maintenance object

        Args:
            maintenance (TeamMaintenance): Team maintenance object to delete
        """
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint="/api/account/teams/%s/maintenance/%s/"
            % (str(self._team.unique_id), str(maintenance.unique_id)),
            success_code=204,
        )
