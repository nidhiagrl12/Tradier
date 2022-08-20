import requests
import json
import asyncio
import websockets

token = '<<MY TOKEN >> '

response = requests.post('https://api.tradier.com/v1/markets/events/session',
    data={},
    headers={'Authorization': f"Bearer {token}", 'Accept': 'application/json'}
)

resp = response.json()
session = resp['stream']['sessionid']

async def ws_connect():
    uri = "wss://ws.tradier.com/v1/markets/events"
    async with websockets.connect(uri, ssl=True, compression=None) as websocket:
        payload = '{"symbols": ["SPY"], "sessionid": "' + session + '", "linebreak": true}'
        await websocket.send(payload)

        # print(f">>> {payload}")

        async for message in websocket:
            print(f"<<< {message}")

asyncio.run(ws_connect())

