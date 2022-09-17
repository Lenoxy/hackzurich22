#!/usr/bin/env python3

import asyncio
import json
from pprint import pprint

import websockets

BASE_URL = "wss://hack.myport.guide"

POSITION_TRACKER = dict()
DOOR_STATUS_TRACKER = dict()
MOVEMENT_TRACKER = dict()

async def lift_status_handler():
    async with websockets.connect(f'{BASE_URL}/') as websocket:
        payload = json.dumps({
            "Method": "SUBSCRIBE",
            "asyncid": 1,
            "Request-URI": "/topic/liftState/",
        })
        await websocket.send(payload)

        async for message in websocket:
            #print(message)
            event = json.loads(message)

            # Ignore initial SUB confirmation
            try:
                if event['Reason-Phrase'] == 'Created':
                    continue
            except KeyError:
                pass

            assert event['type'] == 'topic'
            data = event['data']

            # Interesting fields in the response:
            #   data['movingState']: enum[string] (one of: stand-still | starting | moving | landing)
            #   data['doorState']: enum[string] (one of: closing | closed | locking | locked | opening | opened)

            liftId = data['target']  # e.g. "1.1.2", uses hierarchical naming to reflect {building}.{group}.{car}
            floor = data['floor']
            doorState = data['doorState']
            movement = data['movingState']

            POSITION_TRACKER[liftId] = floor
            DOOR_STATUS_TRACKER[liftId] = doorState
            MOVEMENT_TRACKER[liftId] = movement

async def periodic_log():
    while True:
        await asyncio.sleep(5)
        pprint(POSITION_TRACKER)
        pprint(DOOR_STATUS_TRACKER)
        pprint(MOVEMENT_TRACKER)
        print()

async def handler():
    await asyncio.gather(
        lift_status_handler(),
        periodic_log(),
    )

loop = asyncio.get_event_loop()
result = loop.run_until_complete(handler())
