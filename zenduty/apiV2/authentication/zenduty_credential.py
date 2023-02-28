import os


class ZendutyCredential:
    _api_key: str

    def __init__(self, api_key: str = os.environ.get("ZENDUTY_API_KEY")):
        if api_key == "":
            raise ValueError("error: api_key length must be greater than 0")
        else:
            self._api_key = api_key

    def get_api_key(self) -> str:
        return self._api_key
