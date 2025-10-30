import os
import logging
from datetime import datetime

# Function to get the numeric value of log level
def get_log_level(level):
    levels = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }
    return levels.get(level.upper(), logging.INFO)

# Main function to set up logger and log messages
def main():
    # Get log level from environment variable, default to INFO if not set
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    numeric_log_level = get_log_level(log_level)

    # Configure logging
    logging.basicConfig(level=numeric_log_level, format='%(asctime)s [%(levelname)s] %(message)s')

    # Sample log messages at different levels
    logging.debug("This is a DEBUG message")
    logging.info("This is an INFO message")
    logging.warning("This is a WARNING message")
    logging.error("This is an ERROR message")
    logging.critical("This is a CRITICAL message")

if __name__ == "__main__":
    main()
