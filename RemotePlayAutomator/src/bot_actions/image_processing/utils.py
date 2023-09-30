import cv2
import os

def load_reference_images(path):
    """Carica tutte le immagini di riferimento da un determinato percorso."""
    images = {}
    for filename in os.listdir(path):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            filepath = os.path.join(path, filename)
            images[filename.split('.')[0]] = cv2.imread(filepath)
    return images
