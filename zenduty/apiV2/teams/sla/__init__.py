import json
from uuid import UUID
from ...client import ZendutyClient, ZendutyClientRequestMethod
from .._models import Team
from .models import SLA


class SLAClient:
    def __init__(self, client: ZendutyClient, team: Team):
        self._client = client
        self._team = team

    def get_all_slas(self) -> list[SLA]:
        """Get all SLAs

        Returns:
            list[SLA]: List of all SLAs
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/sla/" % str(self._team.unique_id),
            success_code=200,
        )
        return [SLA(**r) for r in response]

    def get_sla_by_id(self, sla_id: UUID) -> SLA:
        """Get a SLA by ID

        Args:
            sla_id (UUID): SLA ID for which to fetch the SLA

        Returns:
            SLA: SLA Object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/sla/%s/"
            % (str(self._team.unique_id), str(sla_id)),
            success_code=200,
        )
        return SLA(**response)

    def create_sla(
        self,
        name: str,
        is_active: bool,
        acknowledge_time: int,
        resolve_time: int,
        **kwargs
    ) -> SLA:
        """Create a new SLA object

        Args:
            name (str): An arbitary string that represents the SLA object's name
            is_active (bool): A boolean flag that represents whether the SLA object is active or not
            acknowledge_time (int): An integer that represents the SLA object's acknowledge_time
            resolve_time (int): An integer that represents the SLA object's resolve_time

        Returns:
            SLA: _description_
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/account/teams/%s/sla/" % str(self._team.unique_id),
            request_payload={
                "name": name,
                "is_active": is_active,
                "acknowledge_time": acknowledge_time,
                "resolve_time": resolve_time,
                "escalations": kwargs.get("escalations", []),
            },
            success_code=201,
        )
        return SLA(**response)

    def update_sla(self, sla: SLA) -> SLA:
        """Update a SLA object

        Args:
            sla (SLA): sla object to be updated

        Returns:
            SLA: updated SLA object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint="/api/account/teams/%s/sla/%s/"
            % (str(self._team.unique_id), str(sla.unique_id)),
            request_payload=json.loads(sla.to_json()),
            success_code=200,
        )
        return SLA(**response)

    def delete_sla(self, sla: SLA):
        """Delete a SLA object

        Args:
            sla (SLA): sla object to be deleted
        """
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint="/api/account/teams/%s/sla/%s/"
            % (str(self._team.unique_id), str(sla.unique_id)),
            success_code=204,
        )
