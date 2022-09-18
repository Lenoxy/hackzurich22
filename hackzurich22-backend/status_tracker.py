import in_memory_storage

import asyncio
import json
from pprint import pprint

import websockets

BASE_URL = "wss://hack.myport.guide"

KNOWN_LIFTS = set()
POSITION_TRACKER = dict()
DOOR_STATUS_TRACKER = dict()
MOVEMENT_TRACKER = dict()

async def handler():
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

            # Extract all relevant fields of interest from the received message.
            assert event['type'] == 'topic'
            data = event['data']

            # Interesting fields in the response:
            #   data['movingState']: enum[string] (one of: stand-still | starting | moving | landing)
            #   data['doorState']: enum[string] (one of: closing | closed | locking | locked | opening | opened)

            liftId = data['target']  # e.g. "1.1.2", uses hierarchical naming to reflect {building}.{group}.{car}
            floor = data['floor']
            doorState = data['doorState']
            movement = data['movingState']

            # Store everything we know about each lift keyed by its identifier.
            KNOWN_LIFTS.add(liftId)
            POSITION_TRACKER[liftId] = floor
            DOOR_STATUS_TRACKER[liftId] = doorState
            MOVEMENT_TRACKER[liftId] = movement

            # Pass along latest changes to downstream consumers. (NOTE: exact
            # formatting used by the frontend is as yet to be defined.)
            for lift_id in KNOWN_LIFTS:
                change_summary = {
                    "position": POSITION_TRACKER[lift_id],
                    "door": DOOR_STATUS_TRACKER[lift_id],
                    "movement": MOVEMENT_TRACKER[lift_id],
                }
                digest = json.dumps(change_summary)

                for elev in in_memory_storage.elevators:
                    # We aren't selective and just flood information about all lifts
                    # to every nkown smartphones and door signs, irrespective of
                    # whether this notification would be of interest.
                    #
                    # NOTE: if we'd prefer to be more smart, we could use our
                    # registration list to cross-check which information is relevant
                    # for which consumer and only send messages selectively.
                    elev.websocket.send(digest)
                    for ride in elev.rides:
                        ride.websocket.send(digest)
