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

def get_captcha_public_key(driver):
    try:
        element = driver.find_element(By.ID, 'FunCaptcha-Token')
        value = element.get_attribute('value')
        for item in value.split('|'):
            if item.startswith('pk='):
                return item.split('=')[1]
    except Exception as e:
        print(f"Errore durante la ricerca della chiave pubblica: {e}")
        return None


def solve_captcha(api_key, public_key, page_url):
    MAX_RETRIES = 5
    DELAY = 10  # ritardo in secondi

    try:
        response = requests.post('http://2captcha.com/in.php', {
            'key': api_key,
            'method': 'funcaptcha',
            'publickey': public_key,
            'pageurl': page_url,
            'json': 1
        })

        request_id = response.json().get('request')

        for i in range(MAX_RETRIES):
            time.sleep(DELAY)  # Attendere prima di fare la richiesta di soluzione
            solution_response = requests.get(f'http://2captcha.com/res.php?key={api_key}&action=get&id={request_id}&json=1')
            solution = solution_response.json().get('request')

            if solution != "CAPCHA_NOT_READY":
                return solution
            else:
                print(f"Soluzione non pronta, tentativo {i+1}/{MAX_RETRIES}. Attendere {DELAY} secondi...")

        print("Numero massimo di tentativi raggiunto senza ottenere una soluzione valida.")
        return None

    except Exception as e:
        print(f"Errore durante la risoluzione del captcha: {e}")
        return None

def esegui_login(index, account, password, secret, proxy=None, user_agent=None):
    chrome_options = Options()
    if user_agent:
        chrome_options.add_argument(f"user-agent={user_agent}")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    driver.get("https://www.playstation.com/it-it/playstation-network/")
    time.sleep(10)

    try:
        url_before = driver.current_url
        print(url_before)
        driver.find_element(By.CSS_SELECTOR, '#sb-social-toolbar-root .psw-root button.web-toolbar__signin-button').click()
        # driver.find_element_by_css_selector("#sb-social-toolbar-root .psw-root .web-toolbar__signin-button").click()
        time.sleep(10)
        url_after = driver.current_url
        print("Dopo il click, URL:", url_after)
        driver.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys(account)
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, '#signin-entrance-button').click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, '#signin-password-form-password input[aria-label="Password"]').send_keys(password)
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, '#signin-password-button').click()
        time.sleep(7)

        driver.execute_script("document.title = 'Istanza:  + {index};'")

        iframe_element = driver.find_element(By.CSS_SELECTOR, '[data-e2e*="enforcement-frame"]')
        driver.switch_to.frame(iframe_element)

        public_key = get_captcha_public_key(driver)

        # Supponiamo che l'iframe abbia un ID "my_iframe"
        driver.switch_to.frame("game-core-frame")
        # Ora cerca l'elemento all'interno dell'iframe

        time.sleep(5)

        try:
            # Prova a trovare e fare clic sul primo elemento
            driver.find_element(By.CSS_SELECTOR, '.home button.button').click()
        except:
            # Se il primo elemento non viene trovato, cerca e fai clic sul secondo elemento
            driver.find_element(By.CSS_SELECTOR, '#verifyButton').click()

        driver.switch_to.default_content()

        time.sleep(10)

        if public_key:
            captcha_solution = solve_captcha('34ece13990a4234b7fb1f439fe790535', public_key, driver.current_url)
            if captcha_solution:
                # Use the captcha_solution as needed
                print("Soluzione CAPTCHA:", captcha_solution)
            else:
                print("Impossibile ottenere la soluzione captcha.")
        else:
            print("Chiave pubblica non trovata.")

    except Exception as e:
        print(f"Errore durante il processo di login: {e}")

    time.sleep(50)

def main():
    df = pd.read_excel("./python_account.xlsx", engine='openpyxl')
    with ThreadPoolExecutor(max_workers=10) as executor:
        for index, row in df.iterrows():
            account = row["Account"]
            password = row["Password"]
            secret = row["Secret"]
            proxy = row.get("Proxy", None)
            user_agent = USER_AGENTS[index % len(USER_AGENTS)]
            executor.submit(esegui_login, index, account, password, secret, proxy, user_agent)
            

if __name__ == "__main__":
    main()
