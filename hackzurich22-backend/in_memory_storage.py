import json
from typing import List

from websockets.legacy.server import WebSocketServerProtocol


class Ride:
    def __init__(self, ws: WebSocketServerProtocol, customer_id: int, from_floor: int, to_floor: int):
        self.websocket = ws
        self.customer_id = customer_id
        self.from_floor = from_floor
        self.to_floor = to_floor

    websocket: WebSocketServerProtocol
    customer_id: int
    from_floor: int
    to_floor: int

    def toJSON(self):
        return json.dumps({"customer_id": self.customer_id, "from_floor": self.from_floor, "to_floor": self.to_floor})


class Elevator:
    def __init__(self, ws: WebSocketServerProtocol, name: str, state: str, floor: int, rides: List[Ride]):
        self.websocket = ws
        self.name = name
        self.state = state
        self.floor = floor
        self.rides = rides

    websocket: WebSocketServerProtocol
    name: str
    state: str
    floor: int
    rides: List[Ride] = list()

    def toJSON(self):
        string_rides = []
        for ride in self.rides:
            string_rides.append(ride.toJSON())
        return json.dumps({"name": self.name, "state": self.state, "floor": self.floor, "rides": string_rides})



elevators: List[Elevator] = list()


def get_ride_id():
    x = 1
    for elevator in elevators:
        x += len(elevator.rides)
    return x
