import asyncio
import json
import uuid
from datetime import datetime

import websockets

from elevator import create_or_return_existing
from in_memory_storage import Elevator, Ride

BASE_URL = "wss://hack.myport.guide"


async def lift_call_handler(from_floor, to_floor):
    async with websockets.connect(f'{BASE_URL}/') as websocket:
        # Stage 1: virtually press lift-request button
        inner_payload = {
            "asyncId": uuid.uuid4().hex,
            "target": {"floor": from_floor},  # aka. `pickupFloor`
            "options": {
                "destination": {"destinationFloor": to_floor}
            }
        }
        outer_payload = {
            "asyncId": uuid.uuid4().hex,
            "Request-URI": "/publish/",
            "Method": "POST",
            "body-json": inner_payload,
        }
        await websocket.send(json.dumps(outer_payload))

        # Stage 2: monitor to see wihch lift was effectively selected
        async for message in websocket:
            event = json.loads(message)

            # Ignore response status
            try:
                if event['Reason-Phrase'] == 'Accepted':
                    continue
            except KeyError:
                pass

            assert event['type'] == 'inDoor'
            if 'data' in event:  # and event['data']['state'] == 'waiting':
                alloc = event['data']['allocation']
                return alloc["car"]["name"]


class OrderElevator:
    def __init__(self, customer_id: int, from_floor: int, to_floor: int):
        self.customer_id = customer_id
        self.from_floor = from_floor
        self.to_floor = to_floor

    customer_id: int
    from_floor: int
    to_floor: int


def order(ws, order: OrderElevator):
    print(order.customer_id + order.from_floor)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    assigned_lift = loop.run_until_complete(lift_call_handler(order.from_floor, order.to_floor))

    elevator: Elevator = create_or_return_existing(ws, assigned_lift)
    elevator.rides.append(Ride(ws, order.customer_id, order.from_floor, order.to_floor))
    ws.send(json.dumps({'name': elevator.name, 'arrival_timestamp': str(datetime.now())}))
    # caution: we reworked the code to include the elevator logic from main.py
    # but we also deleted the second (seemingly unused elevator ride). Undo if needed.
    if elevator.websocket is not None:
        elevator.websocket.send(elevator.toJSON())
