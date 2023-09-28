import asyncio

async def cross(device):
    """Simulate a CROSS button tap."""
    device.controller.button("CROSS", "tap")
    await asyncio.sleep(4)

async def circle(device):
    """Simulate a CIRCLE button tap."""
    device.controller.button("CIRCLE", "tap")
    await asyncio.sleep(4)

async def square(device):
    """Simulate a SQUARE button tap."""
    device.controller.button("SQUARE", "tap")
    await asyncio.sleep(4)

async def triangle(device):
    """Simulate a TRIANGLE button tap."""
    device.controller.button("TRIANGLE", "tap")
    await asyncio.sleep(4)

async def share(device):
    """Simulate a SHARE button tap."""
    device.controller.button("SHARE", "tap")
    await asyncio.sleep(4)

async def ps(device):
    """Simulate a PS button tap."""
    device.controller.button("PS", "tap")
    await asyncio.sleep(4)

async def options(device):
    """Simulate an OPTIONS button tap."""
    device.controller.button("OPTIONS", "tap")
    await asyncio.sleep(4)

async def l3(device):
    """Simulate an L3 button tap."""
    device.controller.button("L3", "tap")
    await asyncio.sleep(4)

async def r3(device):
    """Simulate an R3 button tap."""
    device.controller.button("R3", "tap")
    await asyncio.sleep(4)

async def l1(device):
    """Simulate an L1 button tap."""
    device.controller.button("L1", "tap")
    await asyncio.sleep(4)

async def r1(device):
    """Simulate an R1 button tap."""
    device.controller.button("R1", "tap")
    await asyncio.sleep(4)

async def up(device):
    """Simulate an UP button tap."""
    device.controller.button("UP", "tap")
    await asyncio.sleep(4)

async def down(device):
    """Simulate a DOWN button tap."""
    device.controller.button("DOWN", "tap")
    await asyncio.sleep(4)

async def left(device):
    """Simulate a LEFT button tap."""
    device.controller.button("LEFT", "tap")
    await asyncio.sleep(4)

async def right(device):
    """Simulate a RIGHT button tap."""
    device.controller.button("RIGHT", "tap")
    await asyncio.sleep(4)

async def touchpad(device):
    """Simulate a TOUCHPAD button tap."""
    device.controller.button("TOUCHPAD", "tap")
    await asyncio.sleep(4)

# Functions for axis

async def analogico_left_x(device, point=(0.5, 0)):
    """Simulate an analogic movement on LEFT_X axis."""
    device.controller.stick("left", point=point)
    await asyncio.sleep(4)

async def analogico_left_y(device, point=(0, 0.5)):
    """Simulate an analogic movement on LEFT_Y axis."""
    device.controller.stick("left", point=point)
    await asyncio.sleep(4)

async def analogico_right_x(device, point=(0.5, 0)):
    """Simulate an analogic movement on RIGHT_X axis."""
    device.controller.stick("right", point=point)
    await asyncio.sleep(4)

async def analogico_right_y(device, point=(0, 0.5)):
    """Simulate an analogic movement on RIGHT_Y axis."""
    device.controller.stick("right", point=point)
    await asyncio.sleep(4)

async def analogico_l2(device, point=(0.5, 0)):
    """Simulate an analogic movement on L2 axis."""
    device.controller.stick("L2", point=point)  # Adjust if L2 isn't associated with left stick
    await asyncio.sleep(4)

async def analogico_r2(device, point=(0.5, 0)):
    """Simulate an analogic movement on R2 axis."""
    device.controller.stick("R2", point=point)  # Adjust if R2 isn't associated with right stick
    await asyncio.sleep(4)