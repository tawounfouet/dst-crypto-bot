import logging
import os
from datetime import datetime

class IncrementalLogger:
    def __init__(self, base_filename, log_dir='/data/logs'):
        self.base_filename = base_filename
        self.log_dir = log_dir
        self.logger = logging.getLogger(__name__)
        self.setup_logger()

    def setup_logger(self):
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_filename = f"{self.base_filename}_{timestamp}.log"
        full_path = os.path.join(self.log_dir, log_filename)

        file_handler = logging.FileHandler(full_path, mode='w')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.setLevel(logging.DEBUG)

        # Ajout de la version et des auteurs au début du fichier
        from crypto_bot import VERSION, AUTHORS
        self.logger.info(f"Version: {VERSION}")
        self.logger.info(f"Authors: {', '.join(AUTHORS)}")

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
  