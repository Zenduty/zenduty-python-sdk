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

    def get_all_services(self) -> list[TeamMaintenance]:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/maintenance/" % str(self._team.unique_id),
            success_code=200,
        )
        return [TeamMaintenance(**r) for r in response]

    def get_maintenance_by_id(self, maintenance_id: UUID) -> TeamMaintenance:
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
        repeat_until: Optional[datetime] = None,
        **kwargs
    ) -> TeamMaintenance:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/account/teams/%s/maintenance/" % str(self._team.unique_id),
            request_payload={
                "name": name,
                "start_time": start_time.isoformat(),
                "end_time": end_time.isoformat(),
                "repeat_interval": repeat_interval,
                "service_ids": [{"service": str(svc_id)} for svc_id in service_ids],
                "time_zone": time_zone,
                "repeat_until": repeat_until
                if repeat_until is not None
                else repeat_until.isoformat(),
            },
            success_code=201,
        )
        return TeamMaintenance(**response)

    def update_service(self, maintenance: TeamMaintenance) -> TeamMaintenance:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint="/api/account/teams/%s/maintenance/%s/"
            % (str(self._team.unique_id), str(maintenance.unique_id)),
            request_payload=json.loads(maintenance.to_json()),
            success_code=200,
        )
        return TeamMaintenance(**response)

    def delete_service(self, maintenance: TeamMaintenance) -> None:
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint="/api/account/teams/%s/services/%s/"
            % (str(self._team.unique_id), str(service.unique_id)),
            success_code=204,
        )
