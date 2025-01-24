#!/bin/python3

import unittest
import os
import shutil
from src.crypto_bot.logger import IncrementalLogger


class TestIncrementalLogger(unittest.TestCase):
    def setUp(self):
        self.test_log_dir = './tests/test_logs'
        self.base_filename = 'test_log'
        self.logger = IncrementalLogger(self.base_filename, self.test_log_dir)

    def tearDown(self):
        # Nettoyage : suppression du répertoire de test après chaque test
        if os.path.exists(self.test_log_dir):
            shutil.rmtree(self.test_log_dir)

    def test_logger_initialization(self):
        self.assertTrue(os.path.exists(self.test_log_dir))
        self.assertIsNotNone(self.logger.logger)

    def test_log_file_creation(self):
        log_files = os.listdir(self.test_log_dir)
        self.assertEqual(len(log_files), 1)
        self.assertTrue(log_files[0].startswith(self.base_filename))
        self.assertTrue(log_files[0].endswith('.log'))

    def test_logging_methods(self):
        test_message = "Test message"
        self.logger.debug(test_message)
        self.logger.info(test_message)
        self.logger.warning(test_message)
        self.logger.error(test_message)
        self.logger.critical(test_message)

        log_file = os.path.join(
            self.test_log_dir, os.listdir(self.test_log_dir)[0])
        with open(log_file, 'r') as f:
            log_content = f.read()

        self.assertIn("DEBUG - Test message", log_content)
        self.assertIn("INFO - Test message", log_content)
        self.assertIn("WARNING - Test message", log_content)
        self.assertIn("ERROR - Test message", log_content)
        self.assertIn("CRITICAL - Test message", log_content)

    def test_version_and_authors_logging(self):
        log_file = os.path.join(
            self.test_log_dir, os.listdir(self.test_log_dir)[0])
        with open(log_file, 'r') as f:
            log_content = f.read()

        self.assertIn("Version:", log_content)
        self.assertIn("Authors:", log_content)


if __name__ == '__main__':
    unittest.main()
