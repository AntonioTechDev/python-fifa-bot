import time

def inizialize_controller(device):
    print("Guarda lo schermo")
    time.sleep(10)
    device.controller.start()