
import csv

# from run import get_software_name, monitor_software_usage

def log_usage(program_name, start_time, end_time, duration):
    with open('', 'a', newline='') as csvfile:
        fieldnames = ['program_name','start_time','end_time','duration']
        write = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:
            write.writeheader()

        write.writerow({
            'program_name': program_name,
            'start_time': start_time,
            'end_time': end_time,
            'duration': str(duration)
        })

