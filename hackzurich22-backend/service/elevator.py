import json

from ..in_memory_storage import Elevator, Ride, elevators


def open_ws(ws, lift_name: str):
    # on
    elevator = Elevator(lift_name, "idle", [])
    elevators.append(elevator)
    ws.send(json.dumps(elevator))
