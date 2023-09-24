from remote_play.connect import connect_to_device, disconnect_from_device
from remote_play.controller import inizialize_controller
from remote_play.controller import inizialize_controller
from remote_play.session import start_session
from commands.test_button import send_commands

def main():
    ip_address = '192.168.1.12'
    device = connect_to_device(ip_address)
    if device:
        print("Connesso con successo al dispositivo Remote Play!")
        device, thread = start_session(device)

        inizialize_controller(device)
        send_commands(device)

        input("Premi un tasto per terminare...")
        disconnect_from_device(device)
    else:
        print("Impossibile connettersi al dispositivo Remote Play.")

if __name__ == "__main__":
    main()
