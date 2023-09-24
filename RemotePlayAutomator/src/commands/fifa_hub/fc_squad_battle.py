import random
import asyncio
import random
import traceback

async def continuous_press_x_for_40_seconds(device):
    end_time = asyncio.get_event_loop().time() + 40  # 40 secondi
    while asyncio.get_event_loop().time() < end_time:
        device.controller.button("CROSS", "tap")
        await asyncio.sleep(0.5)  # Premi il tasto ogni mezzo secondo

async def play_loop(device):
    for _ in range(6):
        try:
            await play_loop_1(device)
            await asyncio.sleep(3)  # Pausa di 1 secondo tra le iterazioni
        except Exception as e:
            traceback.print_exc()  # Stampa la traccia dell'errore

async def play_for_5_minutes(device):
    end_time = asyncio.get_event_loop().time() + 300  # 360 secondi = 6 minuti
    
    while asyncio.get_event_loop().time() < end_time:
        await play_loop(device)  # Esegui la funzione play_loop
        await asyncio.sleep(3)

async def random_play(device):
    for _ in range(2):  # Esegui il ciclo 2 volte
        await play_for_5_minutes(device)
        await continuous_press_x_for_40_seconds(device)


# ------------------------------------------------
# comandi gioco
async def run_forward(device):
    device.controller.stick("left", axis="y", value=1.0)
    await asyncio.sleep(3)
    device.controller.button("R2", "tap")
    await asyncio.sleep(3)
    device.controller.stick("left", axis="y", value=0)

async def run_backward(device):
    device.controller.stick("left", axis="y", value=-1.0)
    await asyncio.sleep(3)
    device.controller.button("R2", "tap")
    await asyncio.sleep(3)
    device.controller.stick("left", axis="y", value=0)

async def run_diagonal_right_up(device):
    device.controller.stick("left", point=(0.5, 1.0))
    await asyncio.sleep(3)
    device.controller.button("R2", "tap")
    await asyncio.sleep(3)
    device.controller.stick("left", point=(0, 0))

async def run_diagonal_left_up(device):
    device.controller.stick("left", point=(-0.5, 1.0))
    await asyncio.sleep(3)
    device.controller.button("R2", "tap")
    await asyncio.sleep(3)
    device.controller.stick("left", point=(0, 0))

async def run_diagonal_right_down(device):
    device.controller.stick("left", point=(0.5, -1.0))
    await asyncio.sleep(3)    
    device.controller.button("R2", "tap")
    await asyncio.sleep(3)
    device.controller.stick("left", point=(0, 0))

async def run_diagonal_left_down(device):
    device.controller.stick("left", point=(-0.5, -1.0))
    await asyncio.sleep(3)
    device.controller.button("R2", "tap")
    await asyncio.sleep(3)
    device.controller.stick("left", point=(0, 0))

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
    await asyncio.sleep(2)
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

async def continuous_press_x(device):
    end_time = asyncio.get_event_loop().time() + 30  # 30 secondi
    while asyncio.get_event_loop().time() < end_time:
        device.controller.button("CROSS", "tap")
        await asyncio.sleep(0.5)  # Premi il tasto ogni mezzo secondo

async def start_game(device):
    device.controller.button("CROSS", "tap")
    await asyncio.sleep(3)

async def pause_game(device):
    device.controller.button("OPTIONS", "tap")
    await asyncio.sleep(3)

# serie di comandi 
async def play_loop_1(device):
    for _ in range(6):
        await run_forward(device)
        print('corri');
        await asyncio.sleep(2)
        await dribble(device)
        print('dribbling');
        await asyncio.sleep(2)
        await run_diagonal_left_up(device)
        print('diagonale');
        await asyncio.sleep(2)
        await long_pass(device)
        print('longPass');
        await asyncio.sleep(2)
        await run_backward(device)
        print('backword');
        await asyncio.sleep(2)
        await shoot(device)
        print('SHOOT');

async def play_loop_2(device):
    for _ in range(6):
        await run_diagonal_right_down(device)
        await short_pass(device)
        await run_forward(device)
        await through_ball(device)
        await run_diagonal_left_down(device)
        await cross(device)

async def play_loop_3(device):
    for _ in range(6):
        await run_backward(device)
        await dribble(device)
        await run_diagonal_right_up(device)
        await slide_tackle(device)
        await run_forward(device)
        await shoot(device)

async def play_loop_4(device):
    for _ in range(6):
        await run_diagonal_left_down(device)
        await long_pass(device)
        await run_diagonal_right_up(device)
        await defend(device)
        await run_backward(device)
        await cross(device)

async def play_loop_5(device):
    for _ in range(6):
        await run_forward(device)
        await change_player(device)
        await run_diagonal_left_up(device)
        await short_pass(device)
        await run_diagonal_right_down(device)
        await shoot(device)

async def play_loop_6(device):
    for _ in range(6):
        await run_backward(device)
        await dribble(device)
        await run_diagonal_right_down(device)
        await through_ball(device)
        await run_forward(device)
        await slide_tackle(device)

async def play_loop_7(device):
    for _ in range(6):
        await run_diagonal_left_up(device)
        await short_pass(device)
        await run_forward(device)
        await defend(device)
        await run_diagonal_right_up(device)
        await cross(device)

async def play_loop_8(device):
    for _ in range(6):
        await run_diagonal_right_down(device)
        await long_pass(device)
        await run_backward(device)
        await dribble(device)
        await run_forward(device)
        await shoot(device)

async def play_loop_9(device):
    for _ in range(6):
        await run_forward(device)
        await change_player(device)
        await run_diagonal_left_down(device)
        await slide_tackle(device)
        await run_diagonal_right_up(device)
        await cross(device)

async def play_loop_10(device):
    for _ in range(6):
        await run_backward(device)
        await short_pass(device)
        await run_diagonal_right_down(device)
        await through_ball(device)
        await run_forward(device)
        await shoot(device)

async def play_loop_11(device):
    for _ in range(6):
        await run_forward(device)
        await run_diagonal_left_up(device)
        await dribble(device)
        await short_pass(device)
        await run_diagonal_right_down(device)
        await long_pass(device)

async def play_loop_12(device):
    for _ in range(6):
        await run_backward(device)
        await change_player(device)
        await run_diagonal_right_up(device)
        await through_ball(device)
        await run_forward(device)
        await slide_tackle(device)

async def play_loop_13(device):
    for _ in range(6):
        await run_diagonal_left_down(device)
        await dribble(device)
        await run_forward(device)
        await defend(device)
        await run_diagonal_right_up(device)
        await shoot(device)

async def play_loop_14(device):
    for _ in range(6):
        await run_diagonal_right_down(device)
        await short_pass(device)
        await run_backward(device)
        await dribble(device)
        await run_forward(device)
        await cross(device)

async def play_loop_15(device):
    for _ in range(6):
        await run_forward(device)
        await change_player(device)
        await run_diagonal_left_up(device)
        await long_pass(device)
        await run_diagonal_right_down(device)
        await slide_tackle(device)

async def play_loop_16(device):
    for _ in range(6):
        await run_backward(device)
        await dribble(device)
        await run_diagonal_right_up(device)
        await through_ball(device)
        await run_forward(device)
        await defend(device)

async def play_loop_17(device):
    for _ in range(6):
        await run_diagonal_left_down(device)
        await short_pass(device)
        await run_forward(device)
        await dribble(device)
        await run_diagonal_right_up(device)
        await shoot(device)

async def play_loop_18(device):
    for _ in range(6):
        await run_diagonal_right_down(device)
        await long_pass(device)
        await run_backward(device)
        await change_player(device)
        await run_forward(device)
        await cross(device)

async def play_loop_19(device):
    for _ in range(6):
        await run_forward(device)
        await change_player(device)
        await run_diagonal_left_down(device)
        await defend(device)
        await run_diagonal_right_up(device)
        await slide_tackle(device)

async def play_loop_20(device):
    for _ in range(6):
        await run_backward(device)
        await short_pass(device)
        await run_diagonal_right_down(device)
        await dribble(device)
        await run_forward(device)
        await shoot(device)

async def play_loop_21(device):
    for _ in range(6):
        await run_diagonal_left_up(device)
        await dribble(device)
        await run_forward(device)
        await through_ball(device)
        await run_diagonal_right_down(device)
        await defend(device)

async def play_loop_22(device):
    for _ in range(6):
        await run_diagonal_right_up(device)
        await short_pass(device)
        await run_backward(device)
        await change_player(device)
        await run_forward(device)
        await cross(device)

async def play_loop_23(device):
    for _ in range(6):
        await run_forward(device)
        await change_player(device)
        await run_diagonal_left_down(device)
        await long_pass(device)
        await run_diagonal_right_up(device)
        await slide_tackle(device)

async def play_loop_24(device):
    for _ in range(6):
        await run_backward(device)
        await dribble(device)
        await run_diagonal_right_down(device)
        await through_ball(device)
        await run_forward(device)
        await shoot(device)

async def play_loop_25(device):
    for _ in range(6):
        await run_diagonal_left_up(device)
        await short_pass(device)
        await run_forward(device)
        await defend(device)
        await run_diagonal_right_down(device)
        await cross(device)

async def play_loop_26(device):
    for _ in range(6):
        await run_diagonal_right_up(device)
        await long_pass(device)
        await run_backward(device)
        await dribble(device)
        await run_forward(device)
        await slide_tackle(device)

async def play_loop_27(device):
    for _ in range(6):
        await run_forward(device)
        await change_player(device)
        await run_diagonal_left_down(device)
        await through_ball(device)
        await run_diagonal_right_up(device)
        await defend(device)

async def play_loop_28(device):
    for _ in range(6):
        await run_backward(device)
        await short_pass(device)
        await run_diagonal_right_down(device)
        await dribble(device)
        await run_forward(device)
        await shoot(device)

async def play_loop_29(device):
    for _ in range(6):
        await run_diagonal_left_up(device)
        await dribble(device)
        await run_forward(device)
        await change_player(device)
        await run_diagonal_right_down(device)
        await cross(device)

async def play_loop_30(device):
    for _ in range(6):
        await run_diagonal_right_up(device)
        await short_pass(device)
        await run_backward(device)
        await through_ball(device)
        await run_forward(device)
        await slide_tackle(device)

async def play_loop_31(device):
    for _ in range(6):
        await run_forward(device)
        await change_player(device)
        await run_diagonal_left_down(device)
        await defend(device)
        await run_diagonal_right_up(device)
        await shoot(device)

async def play_loop_32(device):
    for _ in range(6):
        await run_backward(device)
        await dribble(device)
        await run_diagonal_right_down(device)
        await long_pass(device)
        await run_forward(device)
        await cross(device)

async def play_loop_33(device):
    for _ in range(6):
        await run_diagonal_left_up(device)
        await short_pass(device)
        await run_forward(device)
        await change_player(device)
        await run_diagonal_right_down(device)
        await defend(device)

async def play_loop_34(device):
    for _ in range(6):
        await run_diagonal_right_up(device)
        await dribble(device)
        await run_backward(device)
        await through_ball(device)
        await run_forward(device)
        await slide_tackle(device)

async def play_loop_35(device):
    for _ in range(6):
        await run_forward(device)
        await change_player(device)
        await run_diagonal_left_down(device)
        await defend(device)
        await run_diagonal_right_up(device)
        await shoot(device)

async def play_loop_36(device):
    for _ in range(6):
        await run_backward(device)
        await short_pass(device)
        await run_diagonal_right_down(device)
        await dribble(device)
        await run_forward(device)
        await cross(device)

async def play_loop_37(device):
    for _ in range(6):
        await run_diagonal_left_up(device)
        await dribble(device)
        await run_forward(device)
        await through_ball(device)
        await run_diagonal_right_down(device)
        await defend(device)

async def play_loop_38(device):
    for _ in range(6):
        await run_diagonal_right_up(device)
        await short_pass(device)
        await run_backward(device)
        await change_player(device)
        await run_forward(device)
        await slide_tackle(device)

async def play_loop_39(device):
    for _ in range(6):
        await run_forward(device)
        await change_player(device)
        await run_diagonal_left_down(device)
        await long_pass(device)
        await run_diagonal_right_up(device)
        await shoot(device)

async def play_loop_40(device):
    for _ in range(6):
        await run_backward(device)
        await dribble(device)
        await run_diagonal_right_down(device)
        await through_ball(device)
        await run_forward(device)
        await cross(device)

#forzare serie di x per 20 sec
#almeno 6
#1 comando sempre una x