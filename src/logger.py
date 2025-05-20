# logger.py

import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Create a timestamped log file
LOG_FILE = os.path.join(LOG_DIR, f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

# Logger getter
def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
