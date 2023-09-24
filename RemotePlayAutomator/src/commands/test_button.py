import time

def send_commands(device):
        # modificare posizione
    device.controller.button("cross", "tap")
    time.sleep(3)
    device.controller.button("SQUARE", "tap")
    time.sleep(3)
    device.controller.button("CIRCLE", "tap")
    time.sleep(3)
    device.controller.button("DOWN", "tap")
    time.sleep(3)