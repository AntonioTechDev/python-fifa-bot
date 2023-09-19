import pandas as pd
import pyotp
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor

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

def esegui_login(account, password, secret, proxy=None, user_agent=None):
    chrome_options = Options()
    
    if proxy:
        chrome_options.add_argument(f"--proxy-server={proxy}")
    
    if user_agent:
        chrome_options.add_argument(f"user-agent={user_agent}")
    
    # Aggiungi le estensioni
    chrome_options.add_extension('path_to_canvas_defender.crx')
    chrome_options.add_extension('path_to_ublock_origin.crx')
    chrome_options.add_extension('path_to_privacy_badger.crx')
    chrome_options.add_extension('path_to_webrtc_network_limiter.crx')
    
    driver = webdriver.Chrome(executable_path='path_to_chromedriver', options=chrome_options)
    driver.get("http://localhost/your_login_page")

    driver.find_element_by_id("username_id").send_keys(account)
    driver.find_element_by_id("password_id").send_keys(password)
    driver.find_element_by_id("login_button_id").click()

    totp_code = generate_totp_code(secret)
    driver.find_element_by_id("totp_code_id").send_keys(totp_code)
    driver.find_element_by_id("submit_totp_code_id").click()

    driver.quit()

def main():
    df = pd.read_excel("path_to_excel_file.xlsx", engine='openpyxl')
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        for index, row in df.iterrows():
            account = row["Account"]
            password = row["Password"]
            secret = row["Secret"]
            proxy = row.get("Proxy", None)
            user_agent = USER_AGENTS[index % len(USER_AGENTS)]
            executor.submit(esegui_login, account, password, secret, proxy, user_agent)

if __name__ == "__main__":
    main()
