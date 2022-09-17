import json

from flask import Flask
from flask_cors import CORS
from flask_sock import Sock

import in_memory_storage
from flask import request

import smartphone, elevator
from elevator import  getAvailableElevator

app = Flask(__name__)
CORS(app)

sock = Sock(app)


@app.route("/ride/new", methods=['POST'])
def new_ride():
    ride = request.get_json()
    user_id = in_memory_storage.get_ride_id()
    elevator_to_use = getAvailableElevator()
    elevator_to_use.rides.append(
        in_memory_storage.Ride(
            user_id,
            ride['from_floor'],
            ride['to_floor']
        )
    )
    elevator_to_use.websocket.send(elevator_to_use.toJSON())
    return str(user_id)



@sock.route('/smartphone')
def smartphone_ws(ws):
    while True:
        smartphone.order(ws, json.loads(ws.receive()))


@sock.route('/elevator')
def elevator_ws(ws):
    while True:
        print('hello')
        elevator.open_ws(ws, ws.receive())
