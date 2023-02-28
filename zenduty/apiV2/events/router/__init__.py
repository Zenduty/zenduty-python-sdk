import json
from uuid import UUID
from ...client import ZendutyClient, ZendutyClientRequestMethod
from .models import Router


class RouterClient:
    def __init__(self, client: ZendutyClient):
        self._client = client

    def get_all_routers(self) -> list[Router]:
        """Returns a list of all the registered routers

        Returns:
            list[Router]: List of all the registered routers
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/v2/account/events/router/",
            success_code=200,
        )
        return [Router(**r) for r in response]

    def get_router_by_id(self, router_id: UUID) -> Router:
        """Get a router by a given id

        Args:
            router_id (UUID): ID of the router

        Returns:
            Router: Router object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint=f"/api/v2/account/events/router/{str(router_id)}/",
            success_code=200,
        )
        return Router(**response)

    def create_router(
        self,
        name: str,
        description: str,
    ) -> Router:
        """Create a new router with the given name and description

        Args:
            name (str): name of the router
            description (str): description of the router

        Returns:
            Router: Created Router object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/v2/account/events/router/",
            request_payload={"name": name, "description": description},
            success_code=201,
        )
        return Router(**response)

    def update_router(self, router: Router) -> Router:
        """Update a router

        Args:
            router (Router): router to update with new information

        Returns:
            Router: Updated router object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint=f"/api/v2/account/events/router/{str(router.unique_id)}/",
            request_payload=json.loads(router.to_json()),
            success_code=200,
        )
        return Router(**response)

    def delete_router(self, router: Router):
        """Delete a router

        Args:
            router (Router): router to delete
        """
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint=f"/api/v2/account/events/router/{str(router.unique_id)}/",
            success_code=204,
        )
