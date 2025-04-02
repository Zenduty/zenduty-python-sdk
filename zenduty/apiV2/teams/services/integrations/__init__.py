from uuid import UUID
from ...models import Team
from ..models import Service
from .models import Integration
from zenduty.apiV2.client import ZendutyClient, ZendutyClientRequestMethod


class IntegrationClient:
    def __init__(self, client: ZendutyClient, team: Team, svc: Service):
        self._client = client
        self._team = team
        self._svc = svc

    def get_all_integrations(self) -> list[Integration]:
        """Get all the integration

        Returns:
            list[Integration]: List of integrations
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/services/%s/integrations/"
            % (str(self._team.unique_id), str(self._svc.unique_id)),
            success_code=200,
        )
        return [Integration(**r) for r in response]

    def get_intg_by_id(self, intg: UUID) -> Integration:
        """Get a integration by ID.

        Args:
            intg (UUID): Integration ID.

        Returns:
            Integration: Integration Object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/services/%s/integrations/%s/"
            % (str(self._team.unique_id), str(self._svc.unique_id), str(intg)),
            success_code=200,
        )
        return Integration(**response)

    def get_intg_alerts_iter(self, intg: Integration, page=1) -> list:
        """Get a integration alerts iterator.


        Args:
            intg (Integration): Integration for which to retrieve alerts.

        Returns:
            __alertsItr__: alerts iterator
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/services/%s/integrations/%s/alerts/?page=%s"
            % (
                str(self._team.unique_id),
                str(self._svc.unique_id),
                str(intg.unique_id),
                int(page),
            ),
            success_code=200,
        )
        return response["results"]

    def create_intg(
        self,
        name: str,
        summary: str,
        application: UUID,
        default_urgency: int = 1,
        integration_type: int = 0,
        create_incidents_for: int = 1,
        is_enabled: bool = True,
        **kwargs
    ) -> Integration:
        """Create a new integration

        Args:
            name (str): A string that represents the Integration object's name
            summary (str): A string that represents the Integration object's summary
            application (UUID): A system-generated string that represents the Application object's unique_id
            escalation_policy (UUID):  A system-generated string that represents the Escalation Policy object's unique_id
            default_urgency (int, optional): An integer that represents the Integration object's default_urgency. 0 is low and 1 is high.. Defaults to 1.
            integration_type (int, optional): An integer that represents the Integration object's integration_type. 0 is alert and 1 is outbound.. Defaults to 0.
            create_incidents_for (int, optional): An integer that represents the type of the Incidents this Integration object will create. 0 is do not create incidents. 1 is critical, 2 is critical and errors, and 3 is critical, errors and warnings.. Defaults to 1.
            is_enabled (bool, optional): A boolean flag that represents whether an Integration is enabled or not. Defaults to True.

        Returns:
            Integration: Created Integration object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/account/teams/%s/services/%s/integrations/"
            % (str(self._team.unique_id), str(self._svc.unique_id)),
            request_payload={
                "name": name,
                "summary": summary,
                "application": application,
                "default_urgency": default_urgency,
                "integration_type": integration_type,
                "create_incidents_for": create_incidents_for,
                "is_enabled": is_enabled,
                "team_priority": None,
                "sla": None,
            },
            success_code=201,
        )
        return self.get_intg_by_id(response["unique_id"])

    def update_intg(
        self,
        intg: Integration,
        name: str,
        application: UUID,
        summary: str = None,
        default_urgency: int = 1,
        integration_type: int = 0,
        create_incidents_for: int = 1,
        is_enabled: bool = True,
        **kwargs
    ) -> Integration:
        """Update the integration provided

        Args:
            intg (Integration): Integration to update

        Returns:
            Integration: Updated integration object
        """
        request_payload = {
            "name": name,
            "summary": summary,
            "application": application,
            "default_urgency": default_urgency,
            "integration_type": integration_type,
            "create_incidents_for": create_incidents_for,
            "is_enabled": is_enabled,
            "team_priority": None,
            "sla": None,
        }

        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint="/api/account/teams/%s/services/%s/integrations/%s/"
            % (
                str(self._team.unique_id),
                str(self._svc.unique_id),
                str(intg.unique_id),
            ),
            request_payload=request_payload,
            success_code=200,
        )
        return Integration(**response)

    def delete_intg(self, intg: Integration):
        """Delete a integration

        Args:
            intg (Integration): Integration object to delete
        """
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint="/api/account/teams/%s/services/%s/integrations/%s"
            % (
                str(self._team.unique_id),
                str(self._svc.unique_id),
                str(intg.unique_id),
            ),
            success_code=204,
        )
