"""
Test suite for the core/base.py module
"""

import logging
import logging.handlers
from logging.handlers import RotatingFileHandler
import unittest
import pathlib

from magiklogger.magiklogger.core.base import BaseLogger


class TestBaseLoggerParams(unittest.TestCase):
    """
    Test cases for the parameters of the BaseLogger class.
    """

    def setUp(self):
        """
        Set up a test environment before each test case.

        This method is called before each test case to create an instance of
        the BaseLogger class with specific configurations, that will be used
        for testing.
        """

        self.base_logger = BaseLogger(logger_name="TestBaseLoggerParams",
                                      logger_path="./logs",
                                      log_level="INFO",
                                      log_to_console=True,
                                      log_to_file=False,
                                      max_bytes=50000,
                                      backup_count=5,
                                      log_format='%(asctime)s - %(levelname)s - %(message)s',
                                      use_color=False)

    def test_logger_name(self):
        """
        Test case to check if the logger_name is correctly set.
        """

        # Assert that the name of the logger matches the provided name
        self.assertEqual(self.base_logger.logger_name, "TestBaseLoggerParams")

    def test_empty_logger_name(self):
        """
        Test case for logger initialization with an empty logger name.
        """

        # Assert that setting an empty string as logger_name
        # raises a ValueError
        with self.assertRaises(ValueError):
            BaseLogger(logger_name="",
                       logger_path="./logs",
                       log_level="INFO",
                       log_to_console=True,
                       log_to_file=False,
                       max_bytes=50000,
                       backup_count=5,
                       log_format='%(asctime)s - %(levelname)s - %(message)s',
                       use_color=False)

    def test_invalid_logger_name(self):
        """
        Test case for logger initialization with an invalid logger name.
        """

        # Assert that setting a non-string value as logger_name
        # raises a TypeError
        with self.assertRaises(TypeError):
            BaseLogger(logger_name=10,
                       logger_path="./logs",
                       log_level="INFO",
                       log_to_console=True,
                       log_to_file=False,
                       max_bytes=50000,
                       backup_count=5,
                       log_format='%(asctime)s - %(levelname)s - %(message)s',
                       use_color=False)

    def test_logger_path(self):
        """
        Test case to check if the logger_path is correctly set.
        """

        # Assert that the logger path matches the expected default value
        self.assertEqual(self.base_logger.logger_path, "./logs")

    def test_empty_logger_path(self):
        """
        Test case for logger initialization with an empty logger path.
        """

        # Assert that setting an empty string as logger_path raises a ValueError
        with self.assertRaises(ValueError):
            BaseLogger(logger_name="TestBaseLogger",
                       logger_path="",
                       log_level="INFO",
                       log_to_console=True,
                       log_to_file=False,
                       max_bytes=50000,
                       backup_count=5,
                       log_format='%(asctime)s - %(levelname)s - %(message)s',
                       use_color=False)

    def test_invalid_logger_path(self):
        """
        Test case for logger initialization with an invalid logger path.
        """

        # Assert that setting a non-string value as logger_path raises a TypeError
        with self.assertRaises(TypeError):
            BaseLogger(logger_name="TestBaseLogger",
                       logger_path=20,
                       log_level="INFO",
                       log_to_console=True,
                       log_to_file=False,
                       max_bytes=50000,
                       backup_count=5,
                       log_format='%(asctime)s - %(levelname)s - %(message)s',
                       use_color=False)

    def test_log_level(self):
        """
        Test case to check if the log_level is correctly set.
        """

        # Assert that the log_level matches the expected default value
        self.assertEqual(self.base_logger.log_level, "INFO")

    def test_invalid_log_level(self):
        """
        Test case for logger initialization with an invalid log level.
        """

        # Assert that setting an invalid value as log_level raises a ValueError
        with self.assertRaises(ValueError):
            BaseLogger(logger_name="TestBaseLogger",
                       logger_path="./logs",
                       log_level="INVALID",
                       log_to_console=True,
                       log_to_file=False,
                       max_bytes=50000,
                       backup_count=5,
                       log_format='%(asctime)s - %(levelname)s - %(message)s',
                       use_color=False)

    def test_log_to_console(self):
        """
        Test case to check if the log_to_console is correctly set.
        """

        # Assert that the log_to_console matches the expected default value
        self.assertEqual(self.base_logger.log_to_console, True)

    def test_invalid_log_to_console(self):
        """
        Test case for logger initialization with an invalid log_to_console.
        """

        # Assert that setting a non-boolean value as log_to_console raises a TypeError
        with self.assertRaises(TypeError):
            BaseLogger(logger_name="TestBaseLogger",
                       logger_path="./logs",
                       log_level="INFO",
                       log_to_console="True",
                       log_to_file=False,
                       max_bytes=50000,
                       backup_count=5,
                       log_format='%(asctime)s - %(levelname)s - %(message)s',
                       use_color=False)

    def test_log_to_file(self):
        """
        Test case to check if the log_to_file is correctly set.
        """

        # Assert that the log_to_file matches the expected default value
        self.assertEqual(self.base_logger.log_to_file, False)

    def test_invalid_log_to_file(self):
        """
        Test case for logger initialization with an invalid log_to_file.
        """

        # Assert that setting a non-boolean value as log_to_file raises a TypeError
        with self.assertRaises(TypeError):
            BaseLogger(logger_name="TestBaseLogger",
                       logger_path="./logs",
                       log_level="INFO",
                       log_to_console=True,
                       log_to_file="False",
                       max_bytes=50000,
                       backup_count=5,
                       log_format='%(asctime)s - %(levelname)s - %(message)s',
                       use_color=False)

    def test_max_bytes(self):
        """
        Test case to check if the max_bytes is correctly set.
        """

        # Assert that the max_bytes matches the expected default value
        self.assertEqual(self.base_logger.max_bytes, 50000)

    def test_invalid_max_bytes(self):
        """
        Test case for logger initialization with a negative max_bytes.
        """

        # Assert that setting a negative value as max_bytes raises a ValueError
        with self.assertRaises(ValueError):
            BaseLogger(logger_name="TestBaseLogger",
                       logger_path="./logs",
                       log_level="INFO",
                       log_to_console=True,
                       log_to_file=False,
                       max_bytes=-1,
                       backup_count=5,
                       log_format='%(asctime)s - %(levelname)s - %(message)s',
                       use_color=False)

    def test_exceeded_max_bytes(self):
        """
        Test case for logger initialization with max_bytes exceeding
        the maximum limit.
        """

        # Assert that setting a value exceeding the maximum limit
        # as max_bytes raises a ValueError
        with self.assertRaises(ValueError):
            BaseLogger(logger_name="TestBaseLogger",
                       logger_path="./logs",
                       log_level="INFO",
                       log_to_console=True,
                       log_to_file=False,
                       max_bytes=500000000,
                       backup_count=5,
                       log_format='%(asctime)s - %(levelname)s - %(message)s',
                       use_color=False)

    def test_zero_max_bytes(self):
        """
        Test case for logger initialization with zero max_bytes.
        """

        # Assert that setting a zero value as max_bytes raises a ValueError
        with self.assertRaises(ValueError):
            BaseLogger(logger_name="TestBaseLogger",
                       logger_path="./logs",
                       log_level="INFO",
                       log_to_console=True,
                       log_to_file=False,
                       max_bytes=0,
                       backup_count=5,
                       log_format='%(asctime)s - %(levelname)s - %(message)s',
                       use_color=False)

    def test_backup_count(self):
        """
        Test case to check if the backup_count is correctly set.
        """

        # Assert that the backup_count matches the expected default value
        self.assertEqual(self.base_logger.backup_count, 5)

    def test_log_format(self):
        """
        Test case to check if the log_format is correctly set.
        """

        # Assert that the log_format matches the expected default value
        default_fmt = '%(asctime)s - %(levelname)s - %(message)s'
        self.assertEqual(self.base_logger.log_format, default_fmt)

    def test_invalid_log_format(self):
        """
        Test case for logger initialization with an invalid log_format.
        """

        # Assert that setting an invalid string as log_format raises a ValueError
        with self.assertRaises(ValueError):
            BaseLogger(logger_name="TestBaseLogger",
                       logger_path="./logs",
                       log_level="INFO",
                       log_to_console=True,
                       log_to_file=False,
                       max_bytes=50000,
                       backup_count=5,
                       log_format='INVALID',
                       use_color=False)


class TestBaseLoggerMethods(unittest.TestCase):
    """
    Test cases for the methods of the BaseLogger class.
    """

    def setUp(self):
        """
        Set up a test environment before each test case.
        """

        # Initialize a BaseLogger instance with specific configurations
        self.base_logger = BaseLogger(logger_name="TestBaseLoggerMethods",
                                      logger_path="./test_logs",
                                      log_level="INFO",
                                      log_to_console=True,
                                      log_to_file=False,
                                      max_bytes=50000,
                                      backup_count=5,
                                      log_format='%(asctime)s - %(levelname)s - %(message)s',
                                      use_color=False)

        # Add a BufferingHandler to capture log messages for test validation
        self.log_capture = logging.handlers.BufferingHandler(1024)
        self.base_logger.logger.addHandler(self.log_capture)

    def tearDown(self):
        """
        Clean up the test environment after each test case.
        """

        # Remove any handlers attached to the logger
        self.base_logger._remove_handlers()

        # Delete the test directory if it exists
        test_dir = pathlib.Path("./test_logs")
        if test_dir.exists() and test_dir.is_dir():
            # Recursively remove the directory and its contents
            for item in test_dir.iterdir():
                if item.is_file():
                    item.unlink()
            test_dir.rmdir()

    def test_configure_handler(self):
        """
        Test case to check if the handler is correctly configured.
        """

        # Create and configure a StreamHandler
        handler = logging.StreamHandler()
        self.base_logger._configure_handler(log_level="INFO",
                                            handler=handler,
                                            formatter=logging.Formatter('%(message)s'))

        # Validate that the handler's level and format are set correctly
        self.assertEqual(handler.level, logging.INFO)
        self.assertEqual(handler.formatter._fmt, '%(message)s')

        # Test error scenarios: invalid log level
        with self.assertRaises(ValueError):
            self.base_logger._configure_handler(log_level="INVALID",
                                                handler=handler,
                                                formatter=logging.Formatter('%(message)s'))

    def test_directory_management(self):
        """
        Test cases related to directory management.
        """

        # Ensure the logger directory is created
        self.base_logger._make_directory()
        self.assertTrue(pathlib.Path("./test_logs").exists())

    def test_handler_management(self):
        """
        Test cases related to handler management.
        """

        # Add a StreamHandler and then remove all handlers
        self.base_logger.logger.addHandler(logging.StreamHandler())
        self.base_logger._remove_handlers()
        # Only the log_capture handler should remain.
        self.assertEqual(len(self.base_logger.logger.handlers), 1)

        # Remove the log_capture handler and ensure no handlers remain
        self.base_logger.logger.handlers = [self.log_capture]
        self.base_logger._remove_handlers()
        self.assertEqual(len(self.base_logger.logger.handlers), 0)

    def test_logger_setup(self):
        """
        Test cases related to setting up the logger.
        """

        # Setup logger and validate its log level
        self.base_logger._setup_logger()
        self.assertEqual(self.base_logger.logger.level, logging.INFO)

        # Test logger setup when console logging is disabled
        self.base_logger._log_to_console = False
        self.base_logger._setup_logger()
        self.assertTrue(
            any(isinstance(handler, logging.StreamHandler)
                for handler in self.base_logger.logger.handlers)
        )

    def test_formatter_setup(self):
        """
        Test cases related to setting up the formatter.
        """

        # Validate custom formatter setup
        formatter = self.base_logger._setup_formatter('%(message)s')
        self.assertEqual(formatter._fmt, '%(message)s')

        # Validate default formatter setup
        formatter = self.base_logger._setup_formatter()
        self.assertEqual(formatter._fmt, '%(asctime)s - %(levelname)s - %(message)s')

    def test_console_handler_setup(self):
        """
        Test cases related to setting up the console handler.
        """

        # Setup and validate a console handler
        self.base_logger._setup_console_handler("INFO", logging.Formatter('%(message)s'))
        self.assertTrue(
            any(isinstance(handler, logging.StreamHandler)
                for handler in self.base_logger.logger.handlers)
        )

        # Setup another console handler and validate the total count
        self.base_logger.logger.addHandler(logging.StreamHandler())
        self.base_logger._setup_console_handler("INFO", logging.Formatter('%(message)s'))
        stream_handlers = [handler for handler in self.base_logger.logger.handlers if
                           isinstance(handler, logging.StreamHandler)]
        self.assertEqual(len(stream_handlers), 2)

    def test_file_handler_setup(self):
        """
        Test cases related to setting up the file handler.
        """

        # Setup and validate a file handler
        self.base_logger._setup_file_handler("INFO", logging.Formatter('%(message)s'))
        self.assertTrue(
            any(isinstance(handler, RotatingFileHandler)
                for handler in self.base_logger.logger.handlers)
        )

        # Setup another file handler and validate the total count
        self.base_logger.logger.addHandler(RotatingFileHandler("./test_logs/file.log"))
        self.base_logger._setup_file_handler("INFO", logging.Formatter('%(message)s'))
        file_handlers = [handler for handler in self.base_logger.logger.handlers if
                         isinstance(handler, RotatingFileHandler)]
        self.assertEqual(len(file_handlers), 2)


if __name__ == "__main__":
    unittest.main()
