import json
from typing import List


class Ride:
    def __init__(self, customer_id: int, from_floor: int, to_floor: int):
        self.customer_id = customer_id
        self.from_floor = from_floor
        self.to_floor = to_floor

    customer_id: int
    from_floor: int
    to_floor: int


class Elevator:
    def __init__(self, name: str, state: str, floor: int, rides: List[Ride]):
        self.name = name
        self.state = state
        self.floor = floor
        self.rides = rides

    name: str
    state: str
    floor: int
    rides: List[Ride] = list()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


elevators: List[Elevator] = list()


def get_ride_id():
    x = 1
    for elevator in elevators:
        x += len(elevator.rides)
    return x
