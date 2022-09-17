#!/usr/bin/env python3

# Hacky test script to demonstrate how to call a lift and monitor its progress.
# See live demo: https://hack.myport.guide/ui/paas/demo/indoor-journey

import json
import time
import urllib.parse
import urllib.request

import httpx

BASE_URL = "https://hack.myport.guide"

def move_lift_from_to(pickupFloor, destinationFloor):
    # POST to start a lift movement
    JSON_DATA = {
        "asyncId": "mytoken",
        "target": {
            "floor": pickupFloor
        },
        "options": {
            "destination": {
                "destinationFloor": destinationFloor
            }
        }
    }

    resp = httpx.post(f'{BASE_URL}/publish/', json=JSON_DATA)
    return resp.json()['asyncId']

async_id = move_lift_from_to(8,3)
print(async_id)
print('********')

# GET to monitor lift status
url = f'{BASE_URL}/async/{async_id}/'
print(url)
while True:
    resp = httpx.get(url)
    j = resp.json()
    print(j)
    try:
        if j['state'] == 'succeeded':
            break
    except KeyError:
        pass  # final status messsage doesn't have nested structure `j['data']['state']`
    time.sleep(1)
