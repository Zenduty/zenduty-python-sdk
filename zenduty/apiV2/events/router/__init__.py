import json
from uuid import UUID
from ...client import ZendutyClient, ZendutyClientRequestMethod
from .models import Router


class RouterClient:
    def __init__(self, client: ZendutyClient):
        self._client = client

    def get_all_routers(self) -> list[Router]:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/v2/account/events/router/",
            success_code=200,
        )
        return [Router(**r) for r in response]

    def get_router_by_id(self, router_id: UUID) -> Router:
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
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/v2/account/events/router/",
            request_payload={"name": name, "description": description},
            success_code=201,
        )
        return Router(**response)

    def update_router(self, router: Router) -> Router:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint=f"/api/v2/account/events/router/{str(router.unique_id)}/",
            request_payload=json.loads(router.to_json()),
            success_code=200,
        )
        return Router(**response)

    def delete_router(self, router: Router) -> Router:
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint=f"/api/v2/account/events/router/{str(router.unique_id)}/",
            success_code=204,
        )
