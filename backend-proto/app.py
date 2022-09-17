#!/usr/bin/env python3

# Source: https://flask.palletsprojects.com/en/2.2.x/quickstart/
# Run with `flask run`

import atexit
import threading
import time
from datetime import datetime

from flask import Flask

app = Flask(__name__)

VISIT_COUNTER = 0
VISIT_COUNT_LOCK = threading.Lock()

def background_task():
    while True:
        with VISIT_COUNT_LOCK:
            print(f'{datetime.now()}: visit_count = {VISIT_COUNTER}')
        time.sleep(10)

def shutdown_hook():
    # Only available with multiprocessing but then we lose data sharing.
    #BG_WORKER.terminate()
    pass

@app.route("/")
def hello_world():
    global VISIT_COUNTER
    with VISIT_COUNT_LOCK:
        VISIT_COUNTER += 1
    return f'You are visitor number {VISIT_COUNTER}'

with app.app_context():
    atexit.register(shutdown_hook)
    global BG_WORKER
    BG_WORKER = threading.Thread(target=background_task)
    BG_WORKER.start()
