from pynput.mouse import Listener
import json
import rel
import websocket


def on_move(x, y):
    """ track mouse movement """
    # print('Pointer moved to {0}'.format((x, y)))

def on_click(x, y, button, pressed):
    """ track mouse click """
    keyData = '{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y))
    data = {
        "type" : "hardware",
        "message" : keyData
    }
    if (pressed == True):
        ws.send(json.dumps(data))
    print(keyData)
def on_scroll(x, y, dx, dy):
    """ track mouse scroll """
    keyData = 'Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y))
    data = {
        "type" : "hardware",
        "message" : keyData
    }
    # print(keyData)
    # ws.send(json.dumps(data))
    # print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))


def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")
    ws.send(json.dumps({"type" : "hardware", "message" : "first connection"}))
    # with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    #             listener.join()
    listener = Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
    listener.start()


if __name__ == "__main__":
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:3001",
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.run_forever(dispatcher=rel, reconnect=5)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()