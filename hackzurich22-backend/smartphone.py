class OrderElevator:
    id: str
    from_floor: int
    to_floor: int


async def order(ws, order: OrderElevator):
    print("not implemented")
    await ws.send("order elevator, not implemented")

