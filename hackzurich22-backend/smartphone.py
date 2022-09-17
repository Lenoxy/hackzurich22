import json
from in_memory_storage import Elevator, Ride, elevators
from datetime import datetime


class OrderElevator:
    customer_id: int
    from_floor: int
    to_floor: int


def getAvailableElevator():
    # todo implement
    # for elevator in elevators:
    #     if elevator.state == "waiting"
    return elevators.__getitem__(0)


def order(ws, order: OrderElevator):
    print("not implemented")
    elevator: Elevator = getAvailableElevator()
    elevator.rides.append(Ride(order.customer_id, order.from_floor, order.to_floor))
    ws.send(json.dumps(type('obj', (object,),
                            {'name': elevator.name, 'arrival_timestamp': datetime.now()}
                            )))
