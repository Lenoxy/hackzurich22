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

        while True:
            try:
                message = await websocket.recv()
            except websockets.ConnectionClosedOK:
                break
            print(message)

asyncio.run(handler())
