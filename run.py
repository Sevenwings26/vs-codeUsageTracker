print('Design Tracker for monitoring software usage')

import psutil 
from datetime import datetime as dt
import time

from log_usage import *

def get_software_name():
    software_name = input("Enter the name of program to track - ").title()
    return software_name

def monitor_software_usage(software_name):
    programStartTime = None
    while True:
        is_running = any(proc.info['name'] == software_name for proc in psutil.process_iter(['name']))

        if is_running and programStartTime is None:
            programStartTime = dt.now()
            print(f"{software_name} started at {programStartTime}.")

        if not is_running and programStartTime is not None:
            programEndTime = dt.now()
            duration = programEndTime - programStartTime
            print(f"{software_name} stopped at {programEndTime}.")
            print(f"Total usage duration: {duration}")
            log_usage(software_name,programStartTime, programEndTime, duration)
        time.sleep(1) 


prog = get_software_name()
monitor_software_usage(prog)

