import asyncio
from pyremoteplay import RPDevice

def connect_to_device(ip_address):
    device = RPDevice(ip_address)
    if not device.get_status():
        print("No Status")
        return None
    return device

def disconnect_from_device(device):
    device.disconnect()
