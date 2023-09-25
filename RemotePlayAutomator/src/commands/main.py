from .ps_home.hub import go_to_ps_home
from .ps_home.hub import launch_fifa_game
from .fifa_hub.fc_hub import go_to_squadBattle
from .fifa_hub.fc_hub import launch_squadBattle
from .fifa_hub.fc_squad_battle import random_play

async def commands(device):
    # Attendi che la sessione sia pronta
    await device.async_wait_for_session()
    
    # Assicurati che la sessione sia pronta prima di procedere
    if device.ready:
        await go_to_ps_home(device)
        await launch_fifa_game(device)
        await go_to_squadBattle(device)
        await launch_squadBattle(device)
        await random_play(device)
    else:
        print("La sessione non è pronta!")
