import logging

# Setting up logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger instance
logger = logging.getLogger("LopezLogger")

# Log a message with your name
logger.info("This is a log message from Lopez."
