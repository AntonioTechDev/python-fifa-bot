import pyautogui

def trova_e_clicca(immagine_ricerca):
    # Effettua uno screenshot dello schermo
    screenshot = pyautogui.screenshot()

    # Ricerca le coordinate dell'immagine all'interno dello screenshot
    posizione_elemento = pyautogui.locateOnScreen(immagine_ricerca, confidence=0.8)

    if posizione_elemento:
        # Calcola il punto centrale del bottone
        x, y, width, height = posizione_elemento
        centro_x = x + width / 2
        centro_y = y + height / 2
        
        # Simula un clic sul centro del bottone
        pyautogui.click(centro_x, centro_y)
        print(f"Bottone trovato e cliccato alle coordinate: ({centro_x}, {centro_y})")
    else:
        print("Bottone non trovato.")
