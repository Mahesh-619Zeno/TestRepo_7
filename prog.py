import os
import json
import uuid
import logging
from datetime import datetime

# Configure logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Constants
DATA_DIR = "output_data"
FILE_NAME = "data.json"

# Ensure output directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Create sample data
data = {
    "id": str(uuid.uuid4()),
    "name": "SampleData",
    "timestamp": datetime.utcnow().isoformat() + "Z"  # ISO 8601 format with UTC suffix
}

# Write JSON to file
file_path = os.path.join(DATA_DIR, FILE_NAME)
try:
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)
    logger.info(f"✅ Data written to {file_path}")
except Exception as e:
    logger.error(f"❌ Failed to write data: {e}")
