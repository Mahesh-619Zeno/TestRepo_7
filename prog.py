import os
import json
import uuid
import logging
from datetime import datetime

# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

# Constants
DATA_DIR = "output_data"
FILE_NAME = "data.json"

# Ensure directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Create sample data
data = {
    "id": str(uuid.uuid4()),
    "name": "SampleData",
    "timestamp": datetime.now().isoformat(timespec='seconds')
}

file_path = os.path.join(DATA_DIR, FILE_NAME)

# Write JSON data safely
try:
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    logger.info(f"✅ Data successfully written to {file_path}")
except (OSError, json.JSONDecodeError) as e:
    logger.error(f"Failed to write data file: {e}")
