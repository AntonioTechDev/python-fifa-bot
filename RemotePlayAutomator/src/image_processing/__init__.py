from image_processing.capture import capture_frame
from image_processing.compare import compare_images
from image_processing.utils import load_reference_images

def process_and_compare_images(device, reference_images_path):
    """
    Cattura un frame dal dispositivo, lo confronta con le immagini di riferimento
    e invia comandi in base al risultato.
    """
    # Carica le immagini di riferimento
    reference_images = load_reference_images(reference_images_path)

    # Cattura un frame dal dispositivo
    captured_frame = capture_frame(device)

    # Confronta il frame catturato con ogni immagine di riferimento
    for name, ref_image in reference_images.items():
        similarity = compare_images(captured_frame, ref_image)
        
        # Se la somiglianza supera una certa soglia, invia comandi specifici
        if similarity > 0.95:  # Ad esempio, 0.95 è una soglia di somiglianza molto alta
            print(f"Frame corrisponde all'immagine di riferimento: {name}")
            send_commands(device)  # Puoi personalizzare questa funzione per inviare comandi specifici
            break