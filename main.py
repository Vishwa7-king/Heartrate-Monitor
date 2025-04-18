from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime
import os
from colorama import init, Fore, Style

init()
os.system('cls')

def ask_to_log():
    os.system(f'title Heartrate Logging')
    print(f"{Fore.RED}[{Style.RESET_ALL}{Fore.WHITE}LOG{Style.RESET_ALL}{Fore.RED}] {Fore.WHITE}- {Style.RESET_ALL}", end="")
    print(f"{Fore.WHITE}Would you like to log your heartrate? Y/N{Style.RESET_ALL}", end=" ")
    user_input = input().strip().upper()
    if user_input == "Y":
        return True
    return False

def setup_log():
    if not os.path.exists('logs'):
        os.makedirs('logs')
    date_str = datetime.now().strftime("%d-%m-%y")
    log_file = f'logs/{date_str}.txt'
    return log_file

def log_heart_rate(log_file, bpm, tag, timestamp):
    with open(log_file, "a") as file:
        file.write(f"{timestamp} - BPM {bpm:>3} - {tag}\n")

log_file = None
if ask_to_log():
    log_file = setup_log()
    os.system('cls')

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
os.system(f'title Connecting...')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    url = 'https://app.hyperate.io/IDHERE' # <<< REPLACE WITH YOUR HYPERATE ID
    driver.get(url)

    wait = WebDriverWait(driver, 30)
    heart_rate_element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'p.heartrate'))
    )

    print(f"{Fore.RED}[{Style.RESET_ALL}HYPERATE{Fore.RED}]{Style.RESET_ALL} - Monitoring Heartrate...")
    os.system(f'title Monitoring Heartrate...')

    seen_valid_bpm = False

    while True:
        heart_rate = heart_rate_element.text.strip()
        bpm = int(heart_rate)

        if bpm == 0 and not seen_valid_bpm:
            time.sleep(1)
            heart_rate_element = driver.find_element(By.CSS_SELECTOR, 'p.heartrate')
            continue

        if bpm > 0:
            seen_valid_bpm = True

        current_time = datetime.now().strftime("%H:%M.%S")

        if bpm <= 65:
            tag = "LOW"
            color = Fore.CYAN
        elif 66 <= bpm <= 100:
            tag = "MODERATE"
            color = Fore.GREEN
        elif 101 <= bpm <= 130:
            tag = "MEDIUM"
            color = Fore.YELLOW
        elif 131 <= bpm <= 160:
            tag = "HIGH"
            color = Fore.RED
        elif 161 <= bpm <= 220:
            tag = "VERY HIGH"
            color = Fore.RED
        else:
            tag = "UNKNOWN"
            color = Style.RESET_ALL

        bpm_str = f"{bpm:>3}"
        tag_str = f"{tag:<10}"
        os.system(f'title Heartrate Monitor - {bpm}BPM - {tag}')
        print(f"{color}[{current_time} - BPM {bpm_str}] - {tag_str}{Style.RESET_ALL}")

        if log_file:
            log_heart_rate(log_file, bpm, tag, current_time)

        time.sleep(6)
        heart_rate_element = driver.find_element(By.CSS_SELECTOR, 'p.heartrate')

finally:
    driver.quit()
