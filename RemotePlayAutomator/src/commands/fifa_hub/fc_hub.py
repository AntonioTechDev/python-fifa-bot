import asyncio

async def async_sleep(seconds):
    await asyncio.sleep(seconds)

async def go_to_squadBattle(device):
    device.controller.button("DOWN", "tap")
    await async_sleep(3)
    device.controller.button("CROSS", "tap")
    await async_sleep(35)
    device.controller.button("R1", "tap")
    await async_sleep(3)
    device.controller.button("R1", "tap")
    await async_sleep(3)
    device.controller.button("CROSS", "tap")
    await async_sleep(5)
    device.controller.button("R1", "tap")
    await async_sleep(3)
    device.controller.button("R1", "tap")
    await async_sleep(3)
    device.controller.button("CROSS", "tap")
    await async_sleep(5)

async def launch_squadBattle(device):

    device.controller.button("UP", "tap")
    await async_sleep(3)
    device.controller.button("CROSS", "tap")
    await async_sleep(3)
    device.controller.button("CROSS", "tap")
    
    await async_sleep(10)
    for i in range(18):  # Usa range(18) per ripetere il ciclo 18 volte
        device.controller.button("CROSS", "tap")
        print(f'click {i + 1}')
        await asyncio.sleep(3)  # Assicurati di usare asyncio.sleep invece di time.sleep

