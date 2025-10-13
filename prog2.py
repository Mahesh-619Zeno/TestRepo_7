import os
import json
import uuid
import datetime
import logging
#import requests  

# Setup logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


os.makedirs(DATA_DIR, exist_ok=True)

try:
    from extra_config import EXTRA_DATA 
except ImportError:
    logger.warning("extra_config module not found, using default extra data")
    EXTRA_DATA = {
        "role": "user",
        "department": "unknown"
    }

# Sample data
data = {
    "id": str(uuid.uuid4()),
    "name": "SampleUser",
    "timestamp": datetime.datetime.now().isoformat(),
    "email": "user@example.com",
    "last_login": None
}

data.update(EXTRA_DATA)

file_path = os.path.join(DATA_DIR, FILE_NAME)

with open(file_path, "w") as f:
    json.dump(data, f, indent=4)

logger.info(f"Data written to {file_path}")

try:
    response = requests.get("https://example.com")  # This will fail
except NameError as e:
    logger.error(f"Missing import used: {e}")
