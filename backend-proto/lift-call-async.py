#!/usr/bin/env python3

import asyncio
import json
from pprint import pprint

import websockets

BASE_URL = "wss://hack.myport.guide"

async def lift_call_handler():
    async with websockets.connect(f'{BASE_URL}/') as websocket:
        inner_payload = {
            "asyncId": "mytoken",
            "target": { "floor": 10 }, # aka. `pickupFloor`
            "options": {
                "destination": { "destinationFloor": -1 }
            }
        }
        outer_payload = {
            "asyncId": 1,
            "Request-URI": "/publish/",
            "Method": "POST",
            "body-json": inner_payload,
        }
        await websocket.send(json.dumps(outer_payload))

        async for message in websocket:
            print(f'< {message}')
            print()

loop = asyncio.get_event_loop()
result = loop.run_until_complete(lift_call_handler())
