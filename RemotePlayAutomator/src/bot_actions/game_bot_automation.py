from .actions import *

async def play_autonomously(device):
    try:
        while True:    
            await cross(device)
    except Exception as e:
        print(f"Errore durante random_play: {e}")
        raise e  # Rilancia l'eccezione per gestirla al livello superiore se necessario

async def go_to_squadBattle(device):
    print('Verso squad battle')
    await down(device)
    await cross(device)
    await asyncio.sleep(31) # Additional 31 seconds to make it 35 seconds in total
    await r1(device)
    await r1(device)
    await cross(device)
    await r1(device)
    await r1(device)
    await cross(device)
    await up(device)

async def go_to_ps_home(device):
    print('torna alla home ps')
    
    await circle(device)
    await circle(device)
    await circle(device)
    await l1(device)
    await asyncio.sleep(1)  # Sleep aggiuntivo per raggiungere 5 secondi totali

async def launch_fifa_game(device):
    print('lancio fifa')
    
    await right(device)
    await right(device)
    # await right(device)
    await cross(device)
    await asyncio.sleep(56)  # Sleep aggiuntivo per raggiungere 60 secondi totali

# Aggiungi questa funzione (o sostituiscila con una funzione di tua scelta)
async def on_successful_reconnect(device):
    await circle(device)
    await circle(device)
    await circle(device)
    await circle(device)
