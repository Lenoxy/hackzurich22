import array
from typing import List


class Ride:
    def __init__(self, id: str, from_floor: int, to_floor: int, room: int, patient_name: str):
        self.id = id
        self.from_floor = from_floor
        self.to_floor = to_floor
        self.room = room
        self.patient_name = patient_name

    id: str
    from_floor: int
    to_floor: int
    room: int
    patient_name: str


class Elevator:
    name: str
    rides: List[Ride] = list()


elevators: List[Elevator] = list()
