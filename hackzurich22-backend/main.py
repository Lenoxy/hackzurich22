#!/usr/bin/env python

import asyncio
from websockets import serve


async def echo(websocket, path):
    async for message in websocket:
        if matches_path(path, "/journey"):
            await websocket.send(path + " " + message)
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
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever


asyncio.run(main())
