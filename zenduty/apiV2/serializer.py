import json
from datetime import datetime
from uuid import UUID


class JsonSerializable:
    def to_json(self):
        return json.loads(self, default=serialize, sort_keys=True, indent=4)

    def __repr__(self):
        return json.dumps(self, default=serialize, sort_keys=True, indent=4)

    def __str__(self):
        return json.dumps(self, default=serialize, sort_keys=True, indent=4)


def serialize(o):
    if isinstance(o, datetime):
        return o.isoformat()
    elif isinstance(o, UUID):
        return str(o)
    else:
        return o.__dict__
