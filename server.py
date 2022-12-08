# server

import asyncio
import websockets
import json


connected_clients = {

}

async def recv_handler(websocket):
    # connection_id = 0
    # # print("connected", websocket)

    print(websocket.remote_address)
    # websocket_connection_id = str(websocket.remote_address[1])
    # connected_clients[websocket_connection_id] = websocket
    
    async for data in websocket:
        try: 
            json_packet: dict = json.loads(data)

            user_id = json_packet["type"]
            message = json_packet["message"]

            # save client on open connection
            if (message == "first connection"):
                # if user_id not in connected_clients:
                print(user_id, "has connected")
                connected_clients[user_id] = websocket

            # if disconnect, remove from list
            if (message == "disconnect"):
                connected_clients[user_id].pop(user_id)

            # check if id exists
            if user_id in connected_clients:
                if (user_id == "hardware"):
                    print(f"From Hardware: {data}")
                    try:
                        await connected_clients["client"].send(data)
                    except:
                        print("client has not yet connected")
                else:
                    print(f"From Client: {data}")
            else:
                print("users not all connected")

        except websockets.exception.ConnectionClosedOK: 
            print("error")
            return

    
async def start_server():
    async with websockets.serve(recv_handler, "", 3001,):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(start_server())