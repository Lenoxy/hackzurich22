from ..in_memory_storage import Elevator, Ride


def open_ws(ws, lift_name: str):
    # on
    ws.send(Elevator(lift_name, "idle", []))
