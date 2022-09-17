#!/usr/bin/env python3

import asyncio
import json

import websockets

BASE_URL = "wss://hack.myport.guide"

async def handler():
    async with websockets.connect(f'{BASE_URL}/') as websocket:
        payload = json.dumps({
            "Method": "SUBSCRIBE",
            "asyncid": 1,
            "Request-URI": "/topic/liftState/",
        })
        await websocket.send(payload)

        async for message in websocket:
            print(message)

            event = json.loads(message)
            assert event['type'] == 'topic'
            data = event['data']

            # Interesting fields in the response:
            #   data['floor']: int
            #   data['movingState']: enum[string] (one of: stand-still | starting | moving | landing)
            #   data['doorState']: enum[string] (one of: closing | closed | locking | locked | opening | opened)
            #   data['target']: string (e.g. "1.1.2")

asyncio.run(handler())
