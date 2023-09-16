import time
import os
import numpy as np
from screen import trova_e_clicca
import pyautogui

def start_remote_play():
#   Start Remote Play directly
    remote_play_path = "C:\\Program Files (x86)\\Sony\\PS Remote Play\\RemotePlay.exe"
    os.startfile(remote_play_path)

#   Wait for Remote Play to load
    time.sleep(5)
    trova_e_clicca('./images/1step.png')

    time.sleep(10)
    trova_e_clicca('./images/2step.png')

    pyautogui.write('antoniodebiase2003@gmail.com')
    time.sleep(5)

    trova_e_clicca('./images/3step.png')
    time.sleep(5)

    trova_e_clicca('./images/4step.png')
    pyautogui.write('test')

    time.sleep(5)
    trova_e_clicca('./images/5step.png')

start_remote_play()