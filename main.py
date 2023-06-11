###############################################################################
###               Stock Repo
###
### Facilitates Stock Repo program
###
### @file   main.py
### @author Justin Loi
###############################################################################

#pip install websocket-client

import config

import websocket
import json
import threading
import time

def send_json_request(ws, request):
    ws.send(json.dumps(request))

def receive_json_response(ws):
    response = ws.recv()
    if response:
        return json.loads(response)

def heartbeat(interval, ws):
    print('heartbeat begins')
    while True:
        time.sleep(interval)
        heartbeatJSON = {
            "op": 1,
            "d": "null"
        }
        send_json_request(ws, heartbeatJSON)
        print("heartbeat sent")

ws = websocket.WebSocket()
ws.connect('wss://gateway.discord.gg/?v=10&encoding=json')
event = receive_json_response(ws)

heartbeat_interval = event['d']['heartbeat_interval'] / 1000
threading._start_new_thread(heartbeat, (heartbeat_interval, ws))


token = config.test_server
payload = {
    'op': 2,
    "d": {
        "token": token,
        "properties": {
            "$os": "windows",
            "$browser": "chrome",
            "$device": "pc"
        }
    }
}

send_json_request(ws, payload)

while True:
    event = receive_json_response(ws)

    try:
        print(f"{event['d']['author']['username']}: {event['d']['content']}")
        op_code = event('op')
        if op_code == 11:
            print('heartbeat received')
    except:
        pass







