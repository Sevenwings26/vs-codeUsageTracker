import psutil
import time
from datetime import datetime
import csv
import platform

def get_program_name():
    default_program_name = "Code.exe" if platform.system() == "Windows" else "code"
    # program_name = input(f"Enter the name of the program to track (default: {default_program_name}): ")

    # return program_name if program_name else default_program_name

    program_name = "Code.exe"
    return program_name

def monitor_program_usage(program_name):
    program_start_time = None
    while True:
        # Check if the program is running
        is_running = any(proc.info['name'] == program_name for proc in psutil.process_iter(['name']))
        
        if is_running and program_start_time is None:
            # Program just started
            program_start_time = datetime.now()
            print(f"{program_name} started at {program_start_time}")
        
        if not is_running and program_start_time is not None:
            # Program just stopped
            program_end_time = datetime.now()
            duration = program_end_time - program_start_time
            print(f"{program_name} stopped at {program_end_time}")
            print(f"Total usage duration: {duration}")
            log_usage(program_name, program_start_time, program_end_time, duration)
            program_start_time = None

        time.sleep(1)  # Check every second

def log_usage(program_name, start_time, end_time, duration):
    with open('program_usage.csv', 'a', newline='') as csvfile:
        fieldnames = ['program_name', 'start_time', 'end_time', 'duration']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header if the file is new
        if csvfile.tell() == 0:
            writer.writeheader()
        
        writer.writerow({
            'program_name': program_name,
            'start_time': start_time,
            'end_time': end_time,
            'duration': str(duration)
        })

if __name__ == "__main__":
    program_name = get_program_name()
    monitor_program_usage(program_name)
