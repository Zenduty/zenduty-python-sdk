import json
from uuid import UUID
from ...client import ZendutyClient, ZendutyClientRequestMethod
from .._models import Team
from .models import Service
from datetime import datetime
from .integrations import IntegrationClient


class ServiceClient:
    def __init__(self, client: ZendutyClient, team: Team):
        self._client = client
        self._team = team

    def get_all_services(self) -> list[Service]:
        """List of all services

        Returns:
            list[Service]: list of all services for the team
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/services/" % str(self._team.unique_id),
            success_code=200,
        )
        return [Service(**r) for r in response]

    def get_integration_client(self, svc: Service) -> IntegrationClient:
        """Get the integration client for a service

        Args:
            svc (Service): service to get the integration client for

        Returns:
            IntegrationClient: get the integration client
        """
        return IntegrationClient(self._client, self._team, svc)

    def get_service_by_id(self, service_id: UUID) -> Service:
        """Get service by ID

        Args:
            service_id (UUID): service id for which service has to be fetched

        Returns:
            Service: service object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/services/%s/"
            % (str(self._team.unique_id), str(service_id)),
            success_code=200,
        )
        return Service(**response)

    def create_service(
        self,
        name: str,
        summary: str,
        description: str,
        escalation_policy: UUID,
        team: UUID,
        sla: UUID,
        team_priority: UUID,
        task_template: UUID,
        auto_resolve_timeout: int = 0,
        acknowledgement_timeout: int = 0,
        status: int = 1,
        under_maintenance: bool = False,
        collation: int = 0,
        collation_time: int = 0,
        **kwargs
    ) -> Service:
        """Create a new service

        Args:
            name (str): A string that represents the Service object's name
            summary (str): A string that represents the Service object's summary
            description (str): A string that represents the Service object's description
            escalation_policy (UUID): A system-generated string that represents the Escalation Policy object's unique_id
            team (UUID): Team uuid for the team to link
            sla (UUID): A system-generated string that represents the SLA object's unique_id
            team_priority (UUID): A system-generated string that represents the Priority object's unique_id
            task_template (UUID): A system-generated string that represents the Task Template object's unique_id
            auto_resolve_timeout (int, optional): An integer that represents the timeout for automatically resolving an Incident. Defaults to 0.
            acknowledgement_timeout (int, optional): An integer that represents the timeout for acknowledging an Incident. Defaults to 0.
            status (int, optional): An integer that represents the Service object's status 0 is disabled, 1 is active, 2 is a warning, 3 is critical, and 4 is under maintenance. Defaults to 1.
            under_maintenance (bool, optional): A boolean flag that represents whether the service object is under maintenance or not. Defaults to False.
            collation (int, optional): An integer that represents the Service object's collation type. 0 is off, 1 is time-based, and 2 is intelligence. Defaults to 0.
            collation_time (int, optional): An integer that represents the Service object's collation_time. Defaults to 0.

        Returns:
            Service: Created service object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/account/teams/%s/services/" % str(self._team.unique_id),
            request_payload={
                "name": name,
                "summary": summary,
                "description": description,
                "auto_resolve_timeout": auto_resolve_timeout,
                "team_priority": team_priority,
                "task_template": task_template,
                "acknowledgement_timeout": acknowledgement_timeout,
                "status": status,
                "escalation_policy": escalation_policy,
                "team": team,
                "sla": sla,
                "under_maintenance": under_maintenance,
                "collation": collation,
                "collation_time": collation_time,
            },
            success_code=201,
        )
        return Service(**response)

    def update_service(self, service: Service) -> Service:
        """Update a service

        Args:
            service (Service): service to update

        Returns:
            Service: updated service object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint="/api/account/teams/%s/services/%s/"
            % (str(self._team.unique_id), str(service.unique_id)),
            request_payload=json.loads(service.to_json()),
            success_code=200,
        )
        return Service(**response)

    def delete_service(self, service: Service):
        """Delete a service

        Args:
            service (Service): service object to delete
        """
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint="/api/account/teams/%s/services/%s/"
            % (str(self._team.unique_id), str(service.unique_id)),
            success_code=204,
        )
