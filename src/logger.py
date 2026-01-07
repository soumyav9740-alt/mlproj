import logging
import os
from datetime import datetime

# Create logs folder
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Log file name
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='[%(asctime)s] %(lineno)d %(filename)s %(levelname)s - %(message)s',
)

if __name__ == "__main__":
    logging.info("Logging setup complete.")
    print("Log file created at:", LOG_FILE_PATH)
