import asyncio
import atexit
import threading
import json

from flask import Flask
from flask import request
from flask_cors import CORS
from flask_sock import Sock

import elevator
import in_memory_storage
import smartphone
import status_tracker

app = Flask(__name__)
CORS(app)

sock = Sock(app)


@app.route("/ride/new", methods=['POST'])
def new_ride():
    ride = request.get_json()
    user_id = in_memory_storage.get_ride_id()
    return str(user_id)


@sock.route('/smartphone')
def smartphone_ws(ws):
    while True:
        x = json.loads(ws.receive())
        smartphone.order(ws, smartphone.OrderElevator(x['customer_id'], x['from_floor'], x['to_floor']))


@sock.route('/elevator')
def elevator_ws(ws):
    while True:
        elevator.open_ws(ws, ws.receive())

## Logic related to bookkeeping of which elevators are where, whether their
## doors are open, etc. Makes use of the publish-subscribe API provided by Schindler

def background_task():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(status_tracker.handler())

def shutdown_hook():
    # This method is only available with multiprocessing, however, we cannot
    # run across different processes because data sharing is no longer possible.
    # For now, let's just leave aside clean termination...
    #BG_WORKER.terminate()
    pass

with app.app_context():
    atexit.register(shutdown_hook)
    global BG_WORKER
    BG_WORKER = threading.Thread(target=background_task)
    BG_WORKER.start()
