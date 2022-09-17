#!/usr/bin/env python3

# Hacky test script to demonstrate how to call a lift and monitor its progress.
# See live demo: https://hack.myport.guide/ui/paas/demo/indoor-journey

import json
import time
import urllib.parse
import urllib.request

import httpx

BASE_URL = "https://hack.myport.guide"

# POST to start a lift movement
JSON_DATA = {
    "asyncId": "1400781663740690789",
    "identity": {
        "type": "id",
        "textId": "1663369570907.0.0"
    },
    "target": "1.56.10.10",
    "options": {
        "destination": {
            "destinationFloor": 10,
            "destinationZone": "Penthouse",
        }
    }
}

resp = httpx.post(f'{BASE_URL}/publish/', json=JSON_DATA)
async_id = resp.json()['asyncId']

print(async_id)
print('********')

# GET to monitor lift status
url = f'{BASE_URL}/async/{async_id}/'
print(url)
for i in range(10):
    resp = httpx.get(url)
    print(resp.json())
    time.sleep(1)
