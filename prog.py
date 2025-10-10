import os
import json
import uuid
import logging

# Setup logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Shared variables
DATA_DIR = "output_data"
FILE_NAME = "data.json"
BACKUP_FILE = "data_backup.json"

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

file_path = os.path.join(DATA_DIR, FILE_NAME)
backup_path = os.path.join(DATA_DIR, BACKUP_FILE)

# Create some sample data
data = {
    "id": str(uuid.uuid4()),
    "name": "SampleData",
    "timestamp": logging.Formatter("%(asctime)s").format(logging.LogRecord("", "", "", 0, "", (), None))
}

# If original exists, backup it first
if os.path.exists(file_path):
    os.replace(file_path, backup_path)
    logger.info(f"Existing file backed up to {backup_path}") 
    
file_path = os.path.join(DATA_DIR, FILE_NAME)

# Write the data to JSON
with open(file_path, "w") as f:
    json.dump(data, f)

logger.info(f"Data written to {file_path}")
