from zenduty.apiV2.events.router import RouterClient
from .models import Event
from zenduty.apiV2.client import ZendutyClient, ZendutyClientRequestMethod


class EventClient:
    def __init__(self, client: ZendutyClient):
        """The constructor of a EventClient

        Args:
            client (ZendutyClient): The ZendutyClient to connect to the APIs
        """
        self._client = client

    def get_router_client(self) -> RouterClient:
        """Returns a event router client

        Returns:
            RouterClient: The event router client
        """
        return RouterClient(self._client)

    def create_event(
        self,
        summary: str,
        message: str,
        alert_type: str,
        integration_key: str,
        entity_id: int = None,
        payload: dict = None,
        urls: list = None,
    ) -> Event:
        """Create the Event object by setting the values of all the required parameters passed, including optional ones.
        Args:
            summary (str): A string that represents the Event object's summary.
            message (str): A string that represents the Event object's message.
            alert_type (str): A pre-defined string that represents the Event object's alert_type. Choices - critical, acknowledged, resolved, error, warning, info.
            integration_key (str): Integration_key of the Integration object.
            entity_id (int, optional): The entity ID associated with the event.
            payload (dict, optional): Additional payload information for the event.
            urls (list, optional): List of URLs associated with the event.

        Returns:
            Event: The created event object.
        """
        request_payload = {
            "summary": summary,
            "message": message,
            "alert_type": alert_type,
        }

        if entity_id is not None:
            request_payload["entity_id"] = entity_id
        if payload is not None:
            request_payload["payload"] = payload
        if urls is not None:
            request_payload["urls"] = urls

        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint=f"/api/events/{integration_key}/",
            request_payload=request_payload,
            success_code=201,
        )
        return Event(**response)
