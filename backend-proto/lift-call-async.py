#!/usr/bin/env python3

import asyncio
import json
import uuid
from pprint import pprint

import websockets

BASE_URL = "wss://hack.myport.guide"

async def lift_call_handler():
    async with websockets.connect(f'{BASE_URL}/') as websocket:
        # Stage 1: virtually press lift-request button
        inner_payload = {
            "asyncId": uuid.uuid4().hex,
            "target": { "floor": 10 }, # aka. `pickupFloor`
            "options": {
                "destination": { "destinationFloor": -1 }
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
            print(f'< {message}')
            print()

            event = json.loads(message)

            # Ignore response status
            try:
                if event['Reason-Phrase'] == 'Accepted':
                    continue
            except KeyError:
                pass

            assert event['type'] == 'inDoor'
            if 'data' in event: # and event['data']['state'] == 'waiting':
                alloc = event['data']['allocation']
                print(f'=> Allocated lift: {alloc["car"]["name"]}')
                break

loop = asyncio.get_event_loop()
result = loop.run_until_complete(lift_call_handler())
