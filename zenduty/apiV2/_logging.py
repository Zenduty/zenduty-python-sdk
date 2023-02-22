import json
import logging


class Logging:
    """logging for internals"""

    def info(self, data: dict):
        msg = json.dumps(data)
        logging.info(msg)
