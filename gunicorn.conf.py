# Gunicorn configuration file
import multiprocessing
import os

# Get the base directory of the project
base_dir = '/home/mbesthc/selmitech'
# Ensure the log directory exists
os.makedirs(os.path.join(base_dir, 'logs'), exist_ok=True)


# Adjust these as needed
bind = "unix:/home/mbesthc/selmitech/realestate.sock" # Specify a unique socket file
workers = 3
# Timeout for worker processes
timeout = 30
# Logging
accesslog = os.path.join(base_dir, 'logs', 'gunicorn_access.log')
errorlog = os.path.join(base_dir, 'logs', 'gunicorn_error.log')
loglevel = 'info'
capture_output = True  # Capture Gunicorn output to logs


