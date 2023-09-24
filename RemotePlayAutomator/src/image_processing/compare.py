from skimage.metrics import structural_similarity as ssim
import cv2

def compare_images(image1, image2):
    """Confronta due immagini e restituisce un valore di somiglianza."""
    # Converti le immagini in grayscale
    image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Calcola SSIM tra le due immagini
    return ssim(image1_gray, image2_gray)
