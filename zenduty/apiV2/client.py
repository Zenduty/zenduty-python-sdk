import json, re, urllib3
from uuid import UUID
from typing import Optional, Union, Any
from enum import Enum
from json import JSONEncoder
from .exceptions import APIException

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

class ZendutyClient:
    """Zenduty client acts as an adapter for Zenduty APIs

    Raises:
        APIException: thrown when the api responds back with a non success code
    """

    def __init__(
        self, 
        api_key: str, 
        use_https: bool = True,
        base_url: str = "www.zenduty.com",
        cert_verify: bool = True
    ) -> None:
        if cert_verify:
            self.pool_manager = urllib3.PoolManager()
        
        else:
            self.pool_manager = urllib3.PoolManager(cert_reqs='CERT_NONE', assert_hostname=False)
        
        if api_key is None:
            raise ValueError("error: api_key must not be None")
        
        self.bearer_token = api_key
        self.headers = {
            'Authorization': f'Token {self.bearer_token}',
            'Content-Type': 'application/json'
        }

        if not re.match('^([a-zA-Z0-9\-]+\.)*[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-]+$', base_url):
            raise ValueError(f"error: {base_url} must be a base url. example: zenduty.com")
        
        self.base_url = f'https://{base_url}' if use_https else f'http://{base_url}'

    def execute(
        self,
        method: ZendutyClientRequestMethod,
        endpoint: str,
        request_payload: Optional[Union[dict, str]] = None,
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
            Union[list[dict], dict]: results relevant parsed json payload
        """
        url = self.base_url + endpoint
        if method.value == "GET":
            response = self.pool_manager.request(method=method.value, url=url, headers=self.headers)
        
        else:
            request_payload = json.dumps(request_payload) if request_payload is not None else None
            response = self.pool_manager.request(method=method.value, url=url, body=request_payload, headers=self.headers)
        
        try:
            response_data = json.loads(response.data.decode('utf-8'))
        
        except:
            response_data = {}
        
        if response.status == success_code:
            return response_data
        raise APIException(
            response.status,
            response_data.get("detail", None) if isinstance(response_data, dict) else None
        )