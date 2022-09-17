import json

from flask import Flask
from flask_sock import Sock
from snowflake import SnowflakeGenerator

import in_memory_storage
from flask import request

from service import smartphone, elevator, lobby

app = Flask(__name__)
sock = Sock(app)

gen = SnowflakeGenerator(42)


@app.route("/new", methods=['POST'])
def new_session():
    ride = request.get_json()
    id = str(next(gen))

    # in_memory_storage.rides.append(
    #     in_memory_storage.Ride(
    #         id,
    #         ride['from_floor'],
    #         ride['to_floor'],
    #         ride['room'],
    #         ride['patient_name']
    #     )
    # )

    return id


@app.route("/")
def new_session2():
    return "<p>Hello, World!</p>"


@sock.route('/smartphone')
def smartphone_ws(ws):
    while True:
        smartphone.order(ws, json.loads(ws.receive()))


@sock.route('/lobby')
def lobby_ws(ws):
    while True:
        lobby.tbd()


@sock.route('/elevator')
def elevator_ws(ws):
    while True:
        elevator.tbd()
