import random
import asyncio
import random
import traceback

last_function = None
SIX_MINUTES = 360
FIVE_SECONDS = 5

async def continuous_press_x_for_40_seconds(device):
    end_time = asyncio.get_event_loop().time() + 40
    while asyncio.get_event_loop().time() < end_time:
        device.controller.button("CROSS", "tap")
        await asyncio.sleep(0.5)

async def play_loop(device):
    try:
        await execute_random_function(device)
    except Exception as e:
        traceback.print_exc()

async def play_for_5_minutes(device):
    current_time = asyncio.get_event_loop().time()
    end_time = current_time + SIX_MINUTES
    
    while current_time < end_time:
        await play_loop(device)
        await asyncio.sleep(FIVE_SECONDS)
        current_time = asyncio.get_event_loop().time()

async def random_play(device):
    for _ in range(2):
        await play_for_5_minutes(device)
        await continuous_press_x_for_40_seconds(device)

# ------------------------------------------------

async def execute_random_function(device):
    global last_function
    functions = [
        run_forward, run_backward, run_diagonal_right_up, run_diagonal_left_up,
        run_diagonal_right_down, run_diagonal_left_down, short_pass, long_pass,
        through_ball, shoot, cross, dribble, defend, slide_tackle, change_player,
        sprint
    ]
    
    # Se l'ultima funzione è stata eseguita, la rimuoviamo dalla lista delle funzioni selezionabili
    if last_function:
        functions.remove(last_function)
    
    selected_function = random.choice(functions)
    print(f"Esecuzione della funzione: {selected_function.__name__}")
    await selected_function(device)
    
    # Memorizza la funzione selezionata come l'ultima funzione eseguita
    last_function = selected_function

# comandi gioco
async def run_forward(device):
    device.controller.stick("left", axis="y", value=1.0)
    await asyncio.sleep(3)
    device.controller.button("R2", "tap")

async def run_backward(device):
    device.controller.stick("left", axis="y", value=-1.0)
    await asyncio.sleep(3)
    device.controller.button("R2", "tap")

async def run_diagonal_right_up(device):
    device.controller.stick("left", point=(0.5, 1.0))
    await asyncio.sleep(3)
    device.controller.button("R2", "tap")

async def run_diagonal_left_up(device):
    device.controller.stick("left", point=(-0.5, 1.0))
    await asyncio.sleep(3)
    device.controller.button("R2", "tap")

async def run_diagonal_right_down(device):
    device.controller.stick("left", point=(0.5, -1.0))
    await asyncio.sleep(3)    
    device.controller.button("R2", "tap")

async def run_diagonal_left_down(device):
    device.controller.stick("left", point=(-0.5, -1.0))
    await asyncio.sleep(3)
    device.controller.button("R2", "tap")

async def short_pass(device):
    device.controller.button("CROSS", "tap")
    await asyncio.sleep(3)

async def long_pass(device):
    device.controller.button("SQUARE", "tap")
    await asyncio.sleep(3)

async def through_ball(device):
    device.controller.button("TRIANGLE", "tap")
    await asyncio.sleep(3)

async def shoot(device):
    device.controller.button("CIRCLE", "tap")
    await asyncio.sleep(3)

async def cross(device):
    device.controller.button("SQUARE", "tap")
    await asyncio.sleep(3)

async def dribble(device):
    device.controller.stick("right", axis="x", value=0.5)
    await asyncio.sleep(3)
    device.controller.stick("right", axis="x", value=0)

async def defend(device):
    device.controller.button("L1", "tap")
    await asyncio.sleep(3)

async def slide_tackle(device):
    device.controller.button("SQUARE", "tap")
    await asyncio.sleep(3)

async def change_player(device):
    device.controller.button("L1", "tap")
    await asyncio.sleep(3)

async def sprint(device):
    device.controller.button("R2", "tap")
    await asyncio.sleep(3)

