import json

from flask import Flask
from flask import request
from flask_cors import CORS
from flask_sock import Sock

import elevator
import in_memory_storage
import smartphone
from elevator import getAvailableElevator

app = Flask(__name__)
CORS(app)

sock = Sock(app)


@app.route("/ride/new", methods=['POST'])
def new_ride():
    ride = request.get_json()
    user_id = in_memory_storage.get_ride_id()
    elevator_to_use = getAvailbleElevator()
    elevator_to_use.rides.append(
        in_memory_storage.Ride(
            # Websocket not open yet, only on order
            None,
            user_id,
            ride['from_floor'],
            ride['to_floor']
        )
    )
    if elevator_to_use.websocket is not None:
        if elevator_to_use.websocket.open:
            elevator_to_use.websocket.send(elevator_to_use.toJSON())
    return str(user_id)


@sock.route('/smartphone')
def smartphone_ws(ws):
    while True:
        smartphone.order(ws, json.loads(ws.receive()))


@sock.route('/elevator')
def elevator_ws(ws):
    while True:
        elevator.open_ws(ws, ws.receive())
