import json


def write_hacks(name, payload):
    if isinstance(payload, list):
        z = [p.to_json() for p in payload]
        payload = json.dumps(z)
    else:
        payload = payload.to_json()
    p = None
    with open("addr.json", "r") as response:
        pay = response.read()
        p = json.loads(pay)
        if p.get(name) is not None:
            return

        p[name] = payload
    with open("addr.json", "w") as response:
        response.write(json.dumps(p))
