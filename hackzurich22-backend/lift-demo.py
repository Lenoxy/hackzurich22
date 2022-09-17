#!/usr/bin/env python3

# Hacky test script to demonstrate how to call a lift and monitor its progress.
# See live demo: https://hack.myport.guide/ui/paas/demo/indoor-journey

BASE_URL = "https://hack.myport.guide"

JSON_DATA = b"""
{
    "asyncId": "1400781663740690789",
    "identity": {
        "type": "id",
        "textId": "1663369570907.0.0"
    },
    "target": "1.56.10.10",
    "options": {
        "destination": {
            "destinationFloor": 10,
            "destinationZone": "Penthouse"
        }
    }
}
"""

import json
import time
import urllib.parse
import urllib.request

# POST to start a lift movement
url = f'{BASE_URL}/publish/'
headers = { 'Content-Type': "application/json" }

req = urllib.request.Request(url, JSON_DATA, headers)
response = urllib.request.urlopen(req)
json_payload = response.read()
async_id = json.loads(json_payload)['asyncId']
print(async_id)
print('********')

# GET to monitor lift status
url = f'{BASE_URL}/async/{async_id}/'
print(url)
for i in range(10):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    print(response.read())
    time.sleep(1)
