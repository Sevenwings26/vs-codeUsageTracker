import psutil
import time

# Define the target software name (replace with your application name)
target_software = "Visual Studio Code"  # Modify this line

# Variables to track usage
prev_running = False
start_time = None
total_usage = 0

while True:
  # Check for running processes
  for process in psutil.process_iter():
    try:
      # Get process name
      if process.name() == target_software:
        # Software found
        running = True
        break
    except (psutil.NoSuchProcess, psutil.AccessDenied):
      pass
  else:
    running = False

  # Update usage based on process state
  if running and not prev_running:
    # Software started, record start time
    # Software started, record start time
    start_time = time.time()
  elif not running and prev_running:
    # Software stopped, calculate duration and update total usage
    end_time = time.time()
    duration = end_time - start_time
    total_usage += duration
    start_time = None
  
  # Update previous running state
  prev_running = running

#   Print current usage (optional)
  print(f"Total Time Spent on {target_software}: {total_usage:.2f} seconds")

  # Optional: Choose a suitable loop interval (e.g., 1 second)
#   time.sleep(1) 
