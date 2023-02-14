import json
import logging


class Logging:
    def info(self, data: dict):
        msg = json.dumps(data)
        logging.info(msg)
