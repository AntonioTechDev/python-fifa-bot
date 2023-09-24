import threading
import atexit
import asyncio
from pyremoteplay.receiver import QueueReceiver

def start_session(device):
    users = device.get_users()
    if not users:
        print("No users registered")
        return None
    user = users[0]
    receiver = QueueReceiver()
    device.create_session(user, receiver=receiver)
    thread = threading.Thread(target=worker, args=(device,), daemon=True)
    thread.start()
    atexit.register(lambda: stop(device, thread))
    device.wait_for_session()
    return device, thread

def worker(device):
    loop = asyncio.new_event_loop()
    task = loop.create_task(device.connect())
    loop.run_until_complete(task)
    loop.run_forever()

def stop(device, thread):
    loop = device.session.loop
    device.disconnect()
    loop.stop()
    thread.join(3)
    print("stopped")
