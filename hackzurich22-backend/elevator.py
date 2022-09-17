import json
from in_memory_storage import Elevator, Ride, elevators


def open_ws(ws, lift_name: str):
    elevator = create_or_return_existing(ws, lift_name)
    print(elevator)
    ws.send(elevator.toJSON())


def create_or_return_existing(ws, name: str):
    for elevator in elevators:
        if elevator.name == name:
            return elevator

    elevator = Elevator(ws, name, "idle", 0, [])
    elevators.append(elevator)
    return elevator


def getAvailableElevator():
    # todo implement
    # for elevator in elevators:
    #     if elevator.state == "waiting"
    return elevators[0]
