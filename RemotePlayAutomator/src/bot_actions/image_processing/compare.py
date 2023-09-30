import cv2
import numpy as np
import os
import datetime
import av 

async def capture_frame(device):
    """Cattura l'ultimo frame video dal dispositivo."""
    frame = device.session.receiver.video_frames
    print(f"Frame type: {type(frame)}")
    return frame

async def convert_frame_to_image(image_or_frames):
    """Converte un av.VideoFrame in una immagine utilizzabile da OpenCV."""
    if isinstance(image_or_frames, list) and all(isinstance(frame, av.VideoFrame) for frame in image_or_frames):
        # Prendi il primo frame come esempio, puoi ciclare per tutti se vuoi
        frame = image_or_frames[0]
        # Converti il frame in numpy array
        image = frame.to_ndarray(format='bgr24')  # 'bgr24' è il formato usato da OpenCV

        print(f"Converted image type: {type(image)}")
        print(f"Image type after conversion: {type(image)}")
        print(f"Image shape: {image.shape}")
        
        return image
    elif isinstance(image_or_frames, np.ndarray):
        return image_or_frames
    else:
        raise ValueError("Tipo di input non riconosciuto.")


async def find_element(immagine_ricerca, device):

    os.makedirs("./bot_actions/image_processing/images/debug_images/", exist_ok=True)

    frame = await capture_frame(device)
    sfondo = await convert_frame_to_image(frame)
    sfondo_gray = cv2.cvtColor(sfondo, cv2.COLOR_BGR2GRAY)

    # Salva le immagini localmente con un timestamp nel nome del file per evitare sovrascritture
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    cv2.imwrite(f"./bot_actions/image_processing/images/debug_images/sfondo_{timestamp}.png", sfondo_gray)

    immagine_ricerca_img = cv2.imread(immagine_ricerca)
    immagine_ricerca_gray = cv2.cvtColor(immagine_ricerca_img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f"./bot_actions/image_processing/images/debug_images/immagine_ricerca_{timestamp}.png", immagine_ricerca_gray)

    # Usa matchTemplate per trovare le corrispondenze
    res = cv2.matchTemplate(sfondo_gray, immagine_ricerca_gray, cv2.TM_CCOEFF_NORMED)
    print(f"Max correlation value: {res.max()}")
    threshold = 0.7  # Puoi modificare questa soglia come preferisci
    loc = np.where(res >= threshold)

    # Evidenzia le corrispondenze
    w, h = immagine_ricerca_gray.shape[::-1]
    for pt in zip(*loc[::-1]):
        cv2.rectangle(sfondo, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    
    # Salva l'immagine con le corrispondenze evidenziate
    cv2.imwrite(f"./bot_actions/image_processing/images/debug_images/matched_{timestamp}.png", sfondo)

    if len(loc[0]) > 0:
        print(f"Elemento trovato.")
        return True
    else:
        print("Elemento non trovato.")
        return False
