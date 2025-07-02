import logging
import os
from datetime import datetime
import logging.handlers 



def setup_logger(name="pipeline", log_dir="./logs", level=logging.INFO):
    """
    Sets up a named logger that logs to a file and the console.

    Returns:
        logging.Logger
    """
    os.makedirs(log_dir, exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid adding multiple handlers if logger is already configured
    if not logger.handlers:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(log_dir, f"{name}_{timestamp}.log")

        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter(
            '[%(levelname)s] %(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(
            '[%(levelname)s] %(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
