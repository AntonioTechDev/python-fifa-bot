import cv2
from PIL import Image
import numpy as np

def capture_frame(device):
    """Cattura l'ultimo frame video dal dispositivo."""
    return device.session.receiver.video_frames

def save_frame_as_image(frame, filename="output_image.jpg"):
    """Salva il frame come immagine."""
    cv2.imwrite(filename, frame)

