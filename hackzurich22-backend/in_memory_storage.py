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


elevators: List[Elevator] = list()
