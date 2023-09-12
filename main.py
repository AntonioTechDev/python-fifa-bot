import pyautogui
import time
import os
import cv2
import numpy as np

def start_remote_play():
#   Start Remote Play directly
    remote_play_path = "C:\\Program Files (x86)\\Sony\\PS Remote Play\\RemotePlay.exe"
    os.startfile(remote_play_path)

#   Wait for Remote Play to load
    time.sleep(10)

#   Click the button
    x, y = 2981, 611   #button coordinates
    pyautogui.moveTo(x, y)
    pyautogui.click()

    time.sleep(5)
    current_screenshot = pyautogui.screenshot()
    current_screenshot.save("current_view.png")

#   Check if the click was successful
    # if check_success():
    #     print("Click successful!")
        
    #     return True
    # else:
    #     print("Click failed!")
    #     return False

def check_success():
#   Check for the presence of an element that indicates success
#   Replace 'success_screenshot.png' with the path to your screenshot
    location = pyautogui.locateOnScreen('success_screenshot.png', confidence=0.7)
    if location:
        return True
    return False

start_remote_play()

# x= 2976, y=626 // buttton
# x=3039, y= 166 // clousure

image1 = cv2.imread("success_screenshot.png")
image2 = cv2.imread("current_view.png")

difference = cv2.subtract(image1, image2)
b, g, r = cv2.split(difference)

if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
    print("Le immagini sono identiche")
else:
    print("Le immagini sono diverse")
    cv2.imwrite("difference.png", difference)