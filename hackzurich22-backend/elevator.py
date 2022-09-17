import json
from in_memory_storage import Elevator, Ride, elevators


def open_ws(ws, lift_name: str):
    # on
    elevator = Elevator(lift_name, "idle", 0, [])
    elevators.append(elevator)
    x = elevator.toJSON()
    print(x)
    ws.send(x)
