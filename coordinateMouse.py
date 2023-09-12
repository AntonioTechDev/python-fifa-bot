from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Coordinates: x={x}, y={y}")

print("Coordinate script started. Click anywhere to get coordinates. Press Ctrl+C to exit.")

# Avvia il listener del mouse
with mouse.Listener(on_click=on_click) as listener:
    listener.join()