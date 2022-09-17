import json

from flask import Flask
from flask_sock import Sock
from snowflake import SnowflakeGenerator

import in_memory_storage
from flask import request

# Port 5000
app = Flask(__name__)
sock = Sock(app)

gen = SnowflakeGenerator(42)


@app.route("/new", methods=['POST'])
def new_session():
    ride = request.get_json()
    id = str(next(gen))

    in_memory_storage.rides.append(
        in_memory_storage.Ride(
            id,
            ride['from_floor'],
            ride['to_floor'],
            ride['room'],
            ride['patient_name']
        )
    )

    return id


@app.route("/")
def new_session2():
    return "<p>Hello, World!</p>"


@sock.route('/echo')
def echo(ws):
    while True:
        data = ws.receive()
        ws.send(data)
