import json

from flask import Flask
from flask_cors import CORS
from flask_sock import Sock

import in_memory_storage
from flask import request

import smartphone, elevator, lobby

app = Flask(__name__)
CORS(app)

sock = Sock(app)


@app.route("/ride/new", methods=['POST'])
def new_session():
    ride = request.get_json()
    user_id = in_memory_storage.get_ride_id()
    in_memory_storage.elevators[0].rides.append(
        in_memory_storage.Ride(
            user_id,
            ride['from_floor'],
            ride['to_floor']
        )
    )

    return user_id



@sock.route('/smartphone')
def smartphone_ws(ws):
    while True:
        smartphone.order(ws, json.loads(ws.receive()))


@sock.route('/lobby')
def lobby_ws(ws):
    while True:
        lobby.open_ws(ws, ws.receive())


@sock.route('/elevator')
def elevator_ws(ws):
    while True:
        print('hello')
        elevator.open_ws(ws, ws.receive())
