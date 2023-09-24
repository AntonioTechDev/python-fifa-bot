from remote_play.connect import connect_to_device, disconnect_from_device
from remote_play.controller import inizialize_controller
from remote_play.session import start
from commands.main import commands
import asyncio

async def main():
    ip_address = '192.168.1.12'
    device = connect_to_device(ip_address)
    if device:
        print("Connesso con successo al dispositivo Remote Play!")
        start(device)
        await inizialize_controller(device)

        await commands(device)  # Assicurati di utilizzare 'await' qui
        input("Premi un tasto per terminare...")
        await disconnect_from_device(device)
    else:
        print("Impossibile connettersi al dispositivo Remote Play.")

if __name__ == "__main__":
    asyncio.run(main())  # Esegui la funzione main() con asyncio.run
