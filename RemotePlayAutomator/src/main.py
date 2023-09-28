from remote_play.connect import connect_to_device, disconnect_from_device
from remote_play.controller import inizialize_controller
from remote_play.session import start
from bot_actions.main import commands
from image_processing.capture import capture_frame, save_image_correctly
import asyncio

ip_address = '192.168.1.12' #YOUR ID OF PS
MAX_RETRIES = 10  # Numero massimo di tentativi

async def main():
    retries = 0
    device = None
    connected = False
    phase = 0
    disconnected_before = False  # Variabile per tenere traccia delle disconnessioni

    while retries < MAX_RETRIES:
        try:
            initialized = False

            if not connected:
                device = connect_to_device(ip_address)
                if device:
                    print("Connesso con successo al dispositivo Remote Play!")
                    connected = True
                    if disconnected_before:  # Se ci siamo disconnessi in precedenza, eseguiamo la funzione
                        await on_successful_reconnect()  # Supponendo che tu abbia una funzione di questo tipo
                    else:
                        start(device)
                else:
                    print("Impossibile connettersi al dispositivo Remote Play.")
                    retries += 1
                    continue

            await asyncio.sleep(5)
            image = await capture_frame(device)
            print(type(image))
            print(len(image))  # Mostra la lunghezza della lista
            print(image[:5])
            await save_image_correctly(image, 'test.jpg')

            if connected and not initialized:
                await inizialize_controller(device)
                initialized = True

            if initialized:
                await commands(device, phase)

        except Exception as e:
            print(f"Errore: {e}. Tentativo {retries + 1} di {MAX_RETRIES}.")
            retries += 1
            if retries < MAX_RETRIES:
                print("Tentativo di riconnessione e ripristino...")
                connected = False
                disconnected_before = True  # Impostiamo la variabile a True dato che ci siamo disconnessi
                await asyncio.sleep(5)
            else:
                print("Raggiunto il numero massimo di tentativi. Uscita.")

    await disconnect_from_device(device)

if __name__ == "__main__":
    asyncio.run(main())

async def on_successful_reconnect(device):
    for _ in range(4):
        device.controller.button("CIRCLE", "tap")
        await asyncio.sleep(4)