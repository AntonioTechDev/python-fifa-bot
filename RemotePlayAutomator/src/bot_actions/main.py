from .game_bot_automation import go_to_ps_home, launch_fifa_game, go_to_squadBattle, play_autonomously

async def commands(device, phase):

    if phase <= 0:
        await device.async_wait_for_session()

    if device.ready:
        if phase <= 1:
            await go_to_ps_home(device)
            phase = 1

        if phase <= 2:
            await launch_fifa_game(device)
            phase = 2

        if phase <= 3:
            await go_to_squadBattle(device)
            phase = 3

        if phase <= 4:
            await play_autonomously(device)
            phase = 4