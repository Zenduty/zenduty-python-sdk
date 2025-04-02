from typing import Optional
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
            )