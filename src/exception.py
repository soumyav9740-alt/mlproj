import sys
import os
import logging
from datetime import datetime


# -------------------------------
# Logging Configuration
# -------------------------------

LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s %(filename)s:%(lineno)d - %(message)s'
)

logger = logging.getLogger(__name__)


# -------------------------------
# Error Formatter
# -------------------------------

def format_error_message(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    err = str(error)

    error_message = (
        f"Error occurred in python script [{file_name}] "
        f"line number [{line_number}] "
        f"error message [{err}]"
    )

    return error_message


# -------------------------------
# Custom Exception
# -------------------------------

class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        super().__init__(error)
        self.error_message = format_error_message(error, error_detail)

        # Log the error
        logger.error(self.error_message, exc_info=True)

    def __str__(self):
        return self.error_message


# -------------------------------
# Test Block
# -------------------------------

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        ce = CustomException(e, sys)
        print(ce)
