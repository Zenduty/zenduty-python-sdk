from .router import RouterClient
from ..client import ZendutyClient, ZendutyClientRequestMethod
from .models import Event


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
    ) -> Event:
        """Create the Event object by setting the values of all the required parameters passed.



        Args:
            summary (str): A string that represents the Event object's summary
            message (str): A string that represents the Event object's message
            alert_type (str): A pre-defined string that represents the Event object's alert_type. Choices - critical, acknowledged, resolved, error, warning, info.
            integration_key (str): integration_key of the Integration object

        Returns:
            Event: The created event object
        """    
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
