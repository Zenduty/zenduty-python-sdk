from datetime import datetime
from uuid import UUID


def serialize(o):
    if type(o) is datetime:
        return o.isoformat()
    elif type(o) is UUID:
        return str(o)
    else:
        return o.__dict__