"""
Test cases for module: magik_logger.py
"""

import logging
import pathlib
import unittest

from unittest.mock import patch

from magiklogger.magiklogger.magik.magik_logger import MagikLogger


class TestMagikLogger(unittest.TestCase):
    """
    Test cases for the MagikLogger class.
    """

    def setUp(self):
        """
        Set up a test environment before each test case.

        This method is called before each test case to create an instance of
        the MagikLogger class with specific configurations, that will be used
        for testing.
        """
        # Create a MagikLogger instance with specified configurations
        self.logger = MagikLogger(logger_name="MagikLogger",
                                  logger_path="./logs",
                                  log_to_console=True,
                                  log_to_file=False,
                                  log_level="DEBUG")

    def tearDown(self):
        """
        Clean up the test environment after each test case.
        """

        # Remove any handlers attached to the logger
        self.logger._remove_handlers()

        # Delete the test directory if it exists
        test_dir = pathlib.Path("./logs")
        if test_dir.exists() and test_dir.is_dir():
            # Recursively remove the directory and its contents
            for item in test_dir.iterdir():
                if item.is_file():
                    item.unlink()
            test_dir.rmdir()

    @patch.object(MagikLogger, '_log_message')
    def test_debug(self, mock_log):
        """
        Test the debug method.
        """
        # Define a debug message and call the debug method
        msg = "Debug message"
        self.logger.debug(msg)
        # Assert the mock method was called with the correct parameters
        mock_log.assert_called_with(logging.DEBUG, msg)

    @patch.object(MagikLogger, '_log_message')
    def test_info(self, mock_log):
        """
        Test the info method.
        """
        # Define an info message and call the info method
        msg = "Info message"
        self.logger.info(msg)
        # Assert the mock method was called with the correct parameters
        mock_log.assert_called_with(logging.INFO, msg)

    @patch.object(MagikLogger, '_log_message')
    def test_warning(self, mock_log):
        """
        Test the warning method.
        """
        # Define a warning message and call the warning method
        msg = "Warning message"
        self.logger.warning(msg)
        # Assert the mock method was called with the correct parameters
        mock_log.assert_called_with(logging.WARNING, msg)

    @patch.object(MagikLogger, '_log_message')
    def test_error(self, mock_log):
        """
        Test the error method.
        """
        # Define an error message and call the error method
        msg = "Error message"
        self.logger.error(msg)
        # Assert the mock method was called with the correct parameters
        mock_log.assert_called_with(logging.ERROR, msg)

    @patch.object(MagikLogger, '_log_message')
    def test_critical(self, mock_log):
        """
        Test the critical method.
        """
        # Define a critical message and call the critical method
        msg = "Critical message"
        self.logger.critical(msg)
        # Assert the mock method was called with the correct parameters
        mock_log.assert_called_with(logging.CRITICAL, msg)

    @patch.object(MagikLogger, '_log_message')
    def test_log_levels(self, mock_log):
        """
        Combined log levels tests
        """
        # Define the log levels and their corresponding constants
        log_levels = {
            "debug": logging.DEBUG,
            "info": logging.INFO,
            "warning": logging.WARNING,
            "error": logging.ERROR,
            "critical": logging.CRITICAL
        }
        # Iterate through the log levels and test each one
        for level, log_const in log_levels.items():
            msg = f"{level} message"
            getattr(self.logger, level)(msg)
            mock_log.assert_called_with(log_const, msg)

    def test_logger_creation(self):
        """
        Test the creation of the TerasLogger instance.

        This method verifies if the TerasLogger instance is created correctly
        with the provided configurations during the setup process.
        """
        # Assert that the TerasLogger instance is not None
        self.assertIsNotNone(self.logger)

        # Assert that the logger_name attribute is set correctly
        expected_name = "MagikLogger"
        self.assertEqual(self.logger.logger_name, expected_name)

        # Assert that the logger_path attribute is set correctly
        expected_path = "./logs"
        self.assertEqual(self.logger.logger_path, expected_path)

        # Assert that the log_to_console attribute is set correctly
        self.assertTrue(self.logger.log_to_console)

        # Assert that the log_to_file attribute is set correctly
        self.assertFalse(self.logger.log_to_file)

    def test_enable_console_logging(self):
        """
        Test the enable_console_logging method.

        This method verifies if the enable_console_logging method correctly
        updates the log_to_console attribute.
        """
        # Set enable to True
        enable = True
        self.logger.enable_console_logging(enable)

        # Assert that the log_to_console attribute is set correctly
        error_msg = "The log_to_console attribute was not correctly set to True"
        self.assertTrue(self.logger.log_to_console, msg=error_msg)

    def test_disable_console_logging(self):
        """
        Test the disable_console_logging method.

        This method verifies if the enable_console_logging method correctly
        updates the log_to_console attribute when passed a False argument.
        """
        # Set enable to False
        enable = False
        self.logger.enable_console_logging(enable)

        # Assert that the log_to_console attribute is set correctly
        error_msg = "The log_to_console attribute was not correctly set to False"
        self.assertFalse(self.logger.log_to_console, msg=error_msg)

    def test_enable_file_logging(self):
        """
        Test the enable_file_logging method.

        This method verifies if the enable_file_logging method correctly
        updates the log_to_file attribute.
        """
        # Set enable to True
        enable = True
        self.logger.enable_file_logging(enable)

        # Assert that the log_to_file attribute is set correctly
        error_msg = "The log_to_file attribute was not correctly set to True"
        self.assertTrue(self.logger.log_to_file, msg=error_msg)

    def test_disable_file_logging(self):
        """
        Test the disable_file_logging method.

        This method verifies if the enable_file_logging method correctly
        updates the log_to_file attribute when passed a False argument.
        """
        # Set enable to False
        enable = False
        self.logger.enable_file_logging(enable)

        # Assert that the log_to_file attribute is set correctly
        error_msg = "The log_to_file attribute was not correctly set to True"
        self.assertFalse(self.logger.log_to_file, msg=error_msg)

    def test_log_to_file(self):
        """
        Test the file logging functionality.

        This method tests whether the logger correctly logs messages
        to a file.
        """
        # Enable file logging
        self.logger.enable_file_logging(enable=True)

        # Log a test message
        self.logger.info("Test log message to file.")

        # Assert that the log file exists and contains the test message
        log_file = pathlib.Path(self.logger.logger_path) / f"{self.logger.logger_name}.log"

        self.assertTrue(log_file.exists())

        with open(log_file, "r") as file:
            logs = file.read()
            self.assertIn("Test log message to file.", logs)

    def test_log_to_console(self):
        """
        Test the console logging functionality.

        This method tests whether the logger correctly logs messages
        to the console.
        """
        # Enable console logging
        self.logger.enable_console_logging(enable=True)
        self.logger.info("Test console log message.")

        # Log a test message
        with self.assertLogs(self.logger.logger, level='INFO') as cm:
            self.logger.logger.info("Test console log message.")

        # Assert that the message was correctly logged
        self.assertIn('Test console log message.', cm.output[0])

    def test_set_log_level(self):
        """
        Test the change_log_level method.
        """
        # Set the log level to DEBUG and check if it is updated correctly
        self.logger.set_log_level("DEBUG")
        self.assertEqual(self.logger.log_level, "DEBUG")

        # Set the log level to ERROR and check if it is updated correctly
        self.logger.set_log_level("ERROR")
        self.assertEqual(self.logger.log_level, "ERROR")

    def test_set_format(self):
        """
        Test the change_format method.
        """
        # Define a new log format
        new_format = "%(asctime)s - %(message)s"

        # Set the new format
        self.logger.set_log_format(new_format)

        # Check if the format is updated correctly for each handler in the logger
        for handler in self.logger.logger.handlers:
            self.assertEqual(handler.formatter._fmt, new_format)

    def test_file_rotation(self):
        """
        Test the file rotation functionality.
        """
        # Set a small max_bytes to trigger file rotation quickly
        self.logger._max_bytes = 100
        self.logger._backup_count = 2

        # Enable file logging
        self.logger.enable_console_logging(enable=False)
        self.logger.enable_file_logging(enable=True)

        # Log messages that exceed max_bytes
        for _ in range(500):
            self.logger.info("Test file rotation.")

        # Check for backup files
        log_dir = pathlib.Path(self.logger.logger_path)
        rotated_files = [filename.name for filename in log_dir.iterdir()
                         if filename.name.startswith(self.logger.logger_name)]

        # Check that rotation occurred by verifying that backup files exist
        self.assertTrue(len(rotated_files) > 1)


if __name__ == '__main__':
    unittest.main()
