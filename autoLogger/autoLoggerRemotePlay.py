# DA COMPLETARE !!!!
# DA COMPLETARE !!!!
# DA COMPLETARE !!!!
# DA COMPLETARE !!!!

import time
import os
import pyautogui
import pyperclip
from screen import trova_e_clicca

def paste_text(text):
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')

def start_remote_play():
    # Percorso all'applicazione Remote Play
    remote_play_path = "C:\\Program Files (x86)\\Sony\\PS Remote Play\\RemotePlay.exe"
    
    # Verifica che il percorso esista
    if not os.path.exists(remote_play_path):
        print(f"Errore: L'applicazione Remote Play non è stata trovata in '{remote_play_path}'.")
        return

    # Avvia Remote Play
    os.startfile(remote_play_path)
    time.sleep(10)

    # Funzione di aiuto per eseguire azioni in sequenza
    def perform_action(image_path, action=None, delay_after=5):
        try:
            trova_e_clicca(image_path)
            if action:
                action()
            time.sleep(delay_after)
        except Exception as e:
            print(f"Errore durante l'esecuzione dell'azione per l'immagine {image_path}. Dettagli: {e}")

    # Esegue le azioni in sequenza
    perform_action('./images/1-step-Button.png', delay_after=10)
    perform_action('./images/2-step-button.png', action=lambda: paste_text('antoniodebiase2003@gmail.com'), delay_after=5)
    perform_action('./images/3-step-button.png', delay_after=5)
    perform_action('./images/4-step-button.png', action=lambda: paste_text('h8b#h7j^xJHn#Hoy3EmC'), delay_after=5)
    perform_action('./images/5-step-button.png', delay_after=10)

# Esegui la funzione
start_remote_play()
