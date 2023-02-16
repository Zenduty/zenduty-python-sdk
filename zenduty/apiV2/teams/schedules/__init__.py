import json
from uuid import UUID
from ...client import ZendutyClient, ZendutyClientRequestMethod
from .._models import Team
from .models import Schedule


class ScheduleClient:
    def __init__(self, client: ZendutyClient, team: Team):
        self._client = client
        self._team = team

    def get_all_schedules(self):
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/schedules/" % str(self._team.unique_id),
            success_code=200,
        )
        return [Schedule(**r) for r in response]

    def get_schedule_by_id(self, schedule_id: UUID):
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/schedules/%s/"
            % (str(self._team.unique_id), str(schedule_id)),
            success_code=200,
        )
        return Schedule(**response)

    def create_schedule(
        self,
        name: str,
        description: str,
        summary: str,
        timezone: str,
        layers: list[dict],
        overrides: list[dict],
    ) -> Schedule:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/account/teams/%s/schedules/" % str(self._team.unique_id),
            request_payload={
                "name": name,
                "summary": summary,
                "description": description,
                "time_zone": timezone,
                "layers": layers,
                "overrides": overrides,
            },
            success_code=201,
        )
        return Schedule(**response)

    def update_schedule(self, schedule: Schedule) -> Schedule:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint="/api/account/teams/%s/schedules/%s/"
            % (str(self._team.unique_id), str(schedule.unique_id)),
            request_payload=json.loads(schedule.toJSON()),
            success_code=200,
        )
        return Schedule(**response)

    def delete_schedule(self, schedule: Schedule):
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint="/api/account/teams/%s/schedules/%s/"
            % (str(self._team.unique_id), str(schedule.unique_id)),
            success_code=204,
        )
