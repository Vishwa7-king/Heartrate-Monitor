import time
from datetime import datetime
import os
from colorama import init, Fore, Style

init()
os.system('cls')

os.system('title Heartrate Log Viewer')

logs_dir = "logs"

if not os.path.exists(logs_dir):
    print(f"{Fore.RED}No 'logs' directory found. Make sure logs exist first.{Style.RESET_ALL}")
    exit()

log_files = [f for f in os.listdir(logs_dir) if f.endswith('.txt')]

if not log_files:
    print(f"{Fore.RED}No log files found in the 'logs' directory.{Style.RESET_ALL}")
    exit()

log_files.sort(key=lambda name: datetime.strptime(name.replace('.txt', ''), "%d-%m-%y"))

print(f"{Fore.RED}[{Style.RESET_ALL}{Fore.WHITE}LOG{Style.RESET_ALL}{Fore.RED}] {Fore.WHITE}- Available Logs:{Style.RESET_ALL}")
for f in log_files:
    print(f"  - {Fore.CYAN}{f}{Style.RESET_ALL}")

print()
selected = input(f"{Fore.RED}[{Style.RESET_ALL}{Fore.WHITE}LOG{Style.RESET_ALL}{Fore.RED}] {Fore.WHITE}- Enter the log filename to load: {Style.RESET_ALL}").strip()

log_path = os.path.join(logs_dir, selected)

if not os.path.exists(log_path):
    print(f"{Fore.RED}The file '{selected}' was not found in the logs folder.{Style.RESET_ALL}")
    exit()

print(f"\n{Fore.GREEN}--- Log Contents: {selected} ---{Style.RESET_ALL}")
with open(log_path, 'r') as file:
    for line in file:
        line = line.strip()

        if "LOW" in line:
            color = Fore.CYAN
        elif "MODERATE" in line:
            color = Fore.GREEN
        elif "MEDIUM" in line:
            color = Fore.YELLOW
        elif "HIGH" in line or "VERY HIGH" in line:
            color = Fore.RED
        else:
            color = Style.RESET_ALL

        print(f"{color}{line}{Style.RESET_ALL}")

print(f"\n{Fore.GREEN}--- End of Log ---{Style.RESET_ALL}")
