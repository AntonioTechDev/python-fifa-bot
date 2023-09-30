import cv2
from PIL import Image
import numpy as np
import av

async def capture_frame(device):
    """Cattura l'ultimo frame video dal dispositivo."""
    return device.session.receiver.video_frames

async def save_image_correctly(image_or_frames, filename="output_image.jpg"):
    # Se è una lista di av.VideoFrame
    if isinstance(image_or_frames, list) and all(isinstance(frame, av.VideoFrame) for frame in image_or_frames):
        # Prendi il primo frame come esempio, puoi ciclare per tutti se vuoi
        frame = image_or_frames[0]
        
        # Converti il frame in numpy array
        image = frame.to_ndarray(format='bgr24')  # 'bgr24' è il formato usato da OpenCV
        
    elif isinstance(image_or_frames, np.ndarray):
        image = image_or_frames
    else:
        raise ValueError("Tipo di input non riconosciuto.")

    # Salva l'immagine con OpenCV
    cv2.imwrite(filename, image)

