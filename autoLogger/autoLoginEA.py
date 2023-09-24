# DA COMPLETARE !!!!
# DA COMPLETARE !!!!
# DA COMPLETARE !!!!
# DA COMPLETARE !!!!

import pandas as pd
import pyotp
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor
import time
from screen import trova_e_clicca
import os
import pyautogui
#style-manager-styling


USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
]

def generate_totp_code(secret):
    totp = pyotp.TOTP(secret)
    return totp.now()

def perform_action(image_path, action=None, delay_after=5):
    try:
        trova_e_clicca(image_path)
        if action:
            action()
        time.sleep(delay_after)
        return True
    except Exception as e:
        print(f"Errore durante l'esecuzione dell'azione per l'immagine {image_path}. Dettagli: {e}")
        return False

    time.sleep(10)

def esegui_login(df, index, account, password, secret, proxy=None, user_agent=None):
    chrome_options = Options()
    if user_agent:
        chrome_options.add_argument(f"user-agent={user_agent}")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    driver.get("https://www.ea.com/it-it/ea-sports-fc/ultimate-team/web-app/")
    time.sleep(10)

    try:

        driver.execute_script("document.title = 'Istanza:  + {index};'")

        perform_action('./images/loginEA.png', delay_after=10)
        time.sleep(10)

        perform_action('./images/emailEA.png', action=lambda: pyautogui.write(account), delay_after=5)
        perform_action('./images/emailPSW.png', action=lambda: pyautogui.write(password), delay_after=5)
        perform_action('./images/signInButtonEA.png')
        time.sleep(10)

        perform_action('./images/gauthEA.png')
        time.sleep(5)
        perform_action('./images/gauthButtonFistStepEA.png')
        time.sleep(5)

        gauthEA = generate_totp_code(secret)
        perform_action('./images/sendButtonGauthEA.png', action=lambda: pyautogui.write(gauthEA), delay_after=5)
        perform_action('./images/signInButtonLastStepEA.png')

        time.sleep(20)
        success = perform_action('./images/transferList.png')

        # Aggiungi il codice per colorare l'email in Excel
        if success:
            df.at[index, 'Account'] = f"=HYPERLINK(\"{account}\")"
            df.at[index, 'Color'] = 'Green'
        else:
            df.at[index, 'Account'] = f"=HYPERLINK(\"{account}\")"
            df.at[index, 'Color'] = 'Red'

    except Exception as e:
        print(f"Errore durante il processo di login: {e}")

    time.sleep(50)

def main():
    df = pd.read_excel("./AccountBot.xlsx", engine='openpyxl')
    with ThreadPoolExecutor(max_workers=2) as executor:
        for index, row in df.iterrows():
            account = row["Account"]
            password = row["Password"]
            secret = row["Secret"]
            proxy = row.get("Proxy", None)
            user_agent = USER_AGENTS[index % len(USER_AGENTS)]
            executor.submit(esegui_login, df, index, account, password, secret, proxy, user_agent)
            

if __name__ == "__main__":
    main()
