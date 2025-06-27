import logging
import os
from datetime import datetime

# === Ensure log directory exists ===
log_dir = "./logs"
os.makedirs(log_dir, exist_ok=True)
def setup_logger(name="pipeline", log_dir="./logs", level=logging.INFO):

    # === Create a unique log filename with timestamp ===
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"pipeline_{timestamp}.log")
    
    # === Set up logging ===
    logging.basicConfig(
        level=logging.INFO,
        format='[%(levelname)s] %(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
