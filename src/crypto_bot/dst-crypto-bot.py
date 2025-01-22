#!/bin/python3
#dst-crypto-bot.py

from crypto_bot import IncrementalLogger
from src import PROJECT_NAME

if __name__ == "__main__":
    logger = IncrementalLogger(PROJECT_NAME)
    logger.info("Hello!")
    logger.debug("Hello!")
    logger.warning("Hello!")
    logger.error("Hello!")