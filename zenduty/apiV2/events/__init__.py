from .router import RouterClient
from ..client import ZendutyClient, ZendutyClientRequestMethod
from .models import Event


class EventClient:
    def __init__(self, client: ZendutyClient):
        self._client = client

    def get_router_client(self) -> RouterClient:
        return RouterClient(self._client)

    def create_event(
        self,
        summary: str,
        message: str,
        alert_type: str,
        integration_key: str,
    ) -> Event:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/events/%s/" % integration_key,
            request_payload={
                "summary": summary,
                "message": message,
                "alert_type": alert_type,
            },
            success_code=201,
        )
        return Event(**response)
