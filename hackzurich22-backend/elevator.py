import json
from in_memory_storage import Elevator, Ride, elevators


def open_ws(ws, lift_name: str):
    # on
    elevator = create_or_return_existing(lift_name)
    print(elevator)
    ws.send(elevator.toJSON())


def create_or_return_existing(name: str):
    for elevator in elevators:
        if elevator.name == name:
            return elevator

    elevator = Elevator(name, "idle", 0, [])
    elevators.append(elevator)
    return elevator
