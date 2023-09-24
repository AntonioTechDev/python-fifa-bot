import asyncio

async def async_sleep(seconds):
    await asyncio.sleep(seconds)

async def go_to_ps_home(device):
    device.controller.button("CIRCLE", "tap")
    await async_sleep(3)
    device.controller.button("CIRCLE", "tap")
    await async_sleep(3)
    device.controller.button("CIRCLE", "tap")
    await async_sleep(3)
    device.controller.button("L1", "tap")

async def launch_fifa_game(device):
    await async_sleep(5)
    print('lancio fifa')
    device.controller.button("RIGHT", "tap")
    await async_sleep(3)
    device.controller.button("RIGHT", "tap")
    await async_sleep(3)
    device.controller.button("CROSS", "tap")
    await async_sleep(60)


# def send_commands(device):
    
#     device.controller.button("UP", "tap")
#     time.sleep(3)
#     device.controller.button("CROSS", "tap")
#     time.sleep(3)
#     device.controller.button("UP", "tap")
#     time.sleep(3)
#     device.controller.button("UP", "tap")
#     time.sleep(10)
#     device.controller.button("CROSS", "tap")
#     time.sleep(3)
#     device.controller.button("CROSS", "tap")
#     time.sleep(3)
#     device.controller.button("CROSS", "tap")
#     time.sleep(3)
#     device.controller.button("CROSS", "tap")
#     time.sleep(3)
#     device.controller.button("CROSS", "tap")
#     time.sleep(3)
#     device.controller.button("CROSS", "tap")
#     time.sleep(3)
#     device.controller.button("CROSS", "tap")
#     time.sleep(3)
#     device.controller.button("CROSS", "tap")
