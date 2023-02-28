import json
from uuid import UUID
import requests
from .authentication.zenduty_credential import ZendutyCredential
import regex
from ._logging import Logging
from typing import Optional, Union, Any
from enum import Enum
from json import JSONEncoder


def _remove_nulls(d):
    return {
        k: v
        for k, v in d.items()
        if v is not None or (isinstance(v, str) and len(v) > 0)
    }


class _ZendutyClientSerializer(JSONEncoder):
    def default(self, value: Any) -> str:
        """JSON serialization conversion function."""
        if isinstance(value, UUID):
            return str(value)
        return super(_ZendutyClientSerializer, self).default(value)


class ZendutyClientRequestMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


def clean_json_of_nulls(value: str) -> str:
    val = json.loads(value, object_hook=_remove_nulls)
    return json.dumps(val)


class APIException(Exception):
    def __init__(self, code: int, message: Optional[str] = None):
        self._code = code
        self._message = message

    def __str__(self):
        if self._message is None:
            return f"error: received code [%d]" % self._code
        else:
            return f"error: received code [%d] with message: %s" % (
                self._code,
                self._message,
            )


# def load_data(
#         method: ZendutyClientRequestMethod,
#         endpoint: str,
#         response_data: dict = {}):
#     p = None
#     with open("response.json", "r") as response:
#         payload = response.read()
#         p = json.loads(payload)
#         if p.get(str(method)) is None:
#             p[str(method)] = dict()
#         if p[str(method)].get(endpoint) is None:
#             p[str(method)][endpoint] = dict()
#         p[str(method)][endpoint] = response_data
#     with open("response.json", "w") as response:
#         response.write(json.dumps(p))


class ZendutyClient:
    """Zenduty client acts as a adapter for Zenduty APIs

    Raises:
        APIException: thrown when the api responds back with a non success code
    """

    _url: str

    def __init__(
        self,
        credential: ZendutyCredential,
        base_url: str = "www.zenduty.com",
        use_https: bool = True,
    ) -> None:
        """Constructor for zenduty client

        Args:
            credential (ZendutyCredential): credentials class that provies client support
            base_url (str, optional): Zenduty contact base url. Defaults to "www.zenduty.com".
            use_https (bool, optional): Enable or disable use_https for API requests. Defaults to True.

        Raises:
            ValueError: thrown when invalid credentials are supplied
            ValueError: thown when incorrect base url is supplied
        """
        if credential is None:
            raise ValueError("error: credential must not be None")
        elif not regex.match(
            "^([a-zA-Z0-9\-]+\.)*[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-]+$", base_url
        ):
            raise ValueError(
                f"error: {base_url} must be a base url. example: zenduty.com"
            )
        scheme = "https" if use_https else "http"
        self._url = scheme + "://" + base_url
        self._headers = {"Authorization": f"Token {credential.get_api_key()}"}
        self._logger = Logging()

    def execute(
        self,
        method: ZendutyClientRequestMethod,
        endpoint: str,
        request_payload: Optional[Union[dict, str]] = {},
        query_params: dict = {},
        success_code: int = 200,
    ) -> Union[list[dict], dict]:
        """Execute a Zenduty client request

        Args:
            method (ZendutyClientRequestMethod): HTTP method to use
            endpoint (str): API endpoint to contact
            request_payload (Optional[Union[dict, str]], optional): payload to send to host. Defaults to {}.
            query_params (dict, optional): query parameters . Defaults to {}.
            success_code (int, optional): Success code for the response from the endpoint. Defaults to 200.

        Raises:
            APIException: Throws exception when request is not successful

        Returns:
            Union[list[dict], dict]: resutls relavant parsed json payload
        """
        req = requests.PreparedRequest()
        req.prepare_url(f"{self._url}{endpoint}", query_params)
        self._logger.info(
            {
                "class": self.__class__.__name__,
                "method": method.value,
                "endpoint": req.url,
            }
        )
        response = requests.request(
            headers={
                **self._headers,
                "Content-Type": "application/json",
            },
            method=method.value,
            url=req.url,
            data=clean_json_of_nulls(
                json.dumps(
                    request_payload,
                    cls=_ZendutyClientSerializer,
                )
            )
            if isinstance(request_payload, dict)
            else request_payload,
        )
        try:
            data = response.json()

            # load_data(method, endpoint, data)
            if response.status_code == success_code:
                return data
            else:
                print(data)
                raise APIException(
                    response.status_code,
                    data.get("detail", None) if type(data) is dict else None,
                )
        except APIException as error:
            raise error
        except Exception as error:
            if response.status_code == success_code:
                # load_data(method, endpoint)
                return {}
            raise APIException(response.status_code, error.__cause__.__str__())
