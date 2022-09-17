#!/usr/bin/env python

import asyncio
import json

from flask import Flask
from websockets import serve

import smartphone


async def router(websocket, path):
    async for message in websocket:
        if matches_path(path, "/smartphone"):
            # {id: string, from_floor: number, to_floor: number}
            await smartphone.order(websocket, json.loads(message))
        elif matches_path(path, "/lobby"):
            # I assume we get the lift number from the message
            return
        elif matches_path(path, "/elevator"):
            # I assume we get the lift number from the message
            return
        else:
            print("unknown WS path:" + path)


def matches_path(path, str):
    if path == str:
        return True
    elif path + "/" == str:
        return True
    elif path == str + "/":
        return True
    else:
        return False


async def main():
    async with serve(router, "localhost", 8765):
        await asyncio.Future()  # run forever


asyncio.run(main())

# app = Flask(__name__)
#
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
