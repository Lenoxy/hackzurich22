import json
from in_memory_storage import Elevator, Ride, elevators
from datetime import datetime
from elevator import getAvailableElevator


class OrderElevator:
    customer_id: int
    from_floor: int
    to_floor: int


def order(ws, order: OrderElevator):
    print("not implemented")
    elevator: Elevator = getAvailableElevator()
    elevator.rides.append(Ride(order.customer_id, order.from_floor, order.to_floor))
    ws.send(json.dumps(type('obj', (object,),
                            {'name': elevator.name, 'arrival_timestamp': datetime.now()}
                            )))
