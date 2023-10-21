"""
Test suite for the core/validators.py module

Version: 1.0.0
"""

import unittest

from magiklogger.magiklogger.core.validators import LoggerValidators


class TestLoggerValidators(unittest.TestCase):
    """
    Test suite for the LoggerValidators class.

    This class contains unit tests for the validation methods provided by the
    LoggerValidators class. Each test focuses on a specific validation method,
    ensuring both positive and negative cases are checked.
    """

    def test_validate_string_parameter(self):
        """
        Test the validate_string_parameter method of LoggerValidators class.

        This test ensures that the method correctly validates string parameters,
        and raises appropriate exceptions for invalid inputs.
        """

        # Test with a valid string
        LoggerValidators.validate_string_parameter(param="test_string",
                                                   param_name="valid_string")

        # Test with a non-string
        with self.assertRaises(TypeError):
            LoggerValidators.validate_string_parameter(param=123,
                                                       param_name="invalid_string")

        # Test with an empty string
        with self.assertRaises(ValueError):
            LoggerValidators.validate_string_parameter(param="   ",
                                                       param_name="empty_string")

    def test_validate_boolean_parameter(self):
        """
        Test the validate_boolean_parameter method of LoggerValidators class.

        This test ensures that the method correctly validates boolean parameters
        and raises appropriate exceptions for non-boolean inputs.
        """

        # Test with a valid boolean
        LoggerValidators.validate_boolean_parameter(param=True,
                                                    param_name="valid_boolean")

        # Test with a non-boolean
        with self.assertRaises(TypeError):
            LoggerValidators.validate_boolean_parameter(param="true",
                                                        param_name="invalid_boolean")

    def test_validate_integer_parameter(self):
        """
        Test the validate_integer_parameter method of LoggerValidators class.

        This test ensures that the method correctly validates integer parameters,
        checks for their range, and raises appropriate exceptions for non-integer
        and out-of-range inputs.
        """

        # Test with a valid integer
        LoggerValidators.validate_integer_parameter(param=5,
                                                    param_name="valid_integer",
                                                    min_val=1,
                                                    max_val=10)

        # Test with a non-integer
        with self.assertRaises(TypeError):
            LoggerValidators.validate_integer_parameter(param="5",
                                                        param_name="invalid_integer")

        # Test with an out-of-range integer
        with self.assertRaises(ValueError):
            LoggerValidators.validate_integer_parameter(param=15,
                                                        param_name="out_of_range_integer",
                                                        min_val=1,
                                                        max_val=10)

    def test_validate_logger_name(self):
        """
        Test the validate_logger_name method of LoggerValidators class.

        This test ensures that the method correctly validates logger names,
        and raises appropriate exceptions for non-string and empty string inputs.
        """

        # Test with a valid logger name
        LoggerValidators.validate_logger_name("MyLogger")

        # Test with a non-string logger name
        with self.assertRaises(TypeError):
            LoggerValidators.validate_logger_name(123)

        # Test with an empty logger name
        with self.assertRaises(ValueError):
            LoggerValidators.validate_logger_name("   ")

    def test_validate_logger_path(self):
        """
        Test the validate_logger_path method of LoggerValidators class.

        This test ensures that the method correctly validates logger paths,
        and raises appropriate exceptions for non-string and empty path inputs.
        """

        # Test with a valid logger path
        LoggerValidators.validate_logger_path("/path/to/logger.log")

        # Test with a non-string logger path
        with self.assertRaises(TypeError):
            LoggerValidators.validate_logger_path(123)

        # Test with an empty logger path
        with self.assertRaises(ValueError):
            LoggerValidators.validate_logger_path("   ")

    def test_validate_log_level(self):
        """
        Test the validate_log_level method of LoggerValidators class.

        This test ensures that the method correctly validates log levels,
        and raises appropriate exceptions for log levels not in the accepted set.
        """

        valid_log_levels = {"INFO", "DEBUG", "ERROR"}

        # Test with a valid log level
        LoggerValidators.validate_log_level("INFO", valid_log_levels)

        # Test with an invalid log level
        with self.assertRaises(ValueError):
            LoggerValidators.validate_log_level("INVALID_LEVEL", valid_log_levels)

    def test_validate_log_level_case_insensitive(self):
        """
        Test the validate_log_level method of LoggerValidators class for
        case-insensitivity.

        This test ensures that the method can handle log levels written
        in different cases.
        """

        valid_log_levels = {"INFO", "DEBUG", "ERROR"}

        # Test with a valid log level in lowercase
        LoggerValidators.validate_log_level("info", valid_log_levels)

        # Test with a valid log level in mixed case
        LoggerValidators.validate_log_level("dEbuG", valid_log_levels)

    def test_validate_log_to_console(self):
        """
        Test the validate_log_to_console method of LoggerValidators class.

        This test ensures that the method correctly validates the 'log_to_console'
        flag, and raises appropriate exceptions for non-boolean inputs.
        """

        # Test with a valid boolean flag
        LoggerValidators.validate_log_to_console(True)

        # Test with a non-boolean flag
        with self.assertRaises(TypeError):
            LoggerValidators.validate_log_to_console("True")

    def test_validate_log_to_file(self):
        """
        Test the validate_log_to_file method of LoggerValidators class.

        This test ensures that the method correctly validates the 'log_to_file'
        flag, and raises appropriate exceptions for non-boolean inputs.
        """

        # Test with a valid boolean flag
        LoggerValidators.validate_log_to_file(True)

        # Test with a non-boolean flag
        with self.assertRaises(TypeError):
            LoggerValidators.validate_log_to_file("True")

    def test_validate_max_bytes(self):
        """
        Test the validate_max_bytes method of LoggerValidators class.

        This test ensures that the method correctly validates maximum bytes
        for logging, and raises appropriate exceptions for non-integer, and
        out-of-bound inputs.
        """

        # Test with a valid byte count
        LoggerValidators.validate_max_bytes(1000)

        # Test with a non-integer byte count
        with self.assertRaises(TypeError):
            LoggerValidators.validate_max_bytes("1000")

        # Test with a negative byte count
        with self.assertRaises(ValueError):
            LoggerValidators.validate_max_bytes(-5)

        # Test with an excessive byte count
        with self.assertRaises(ValueError):
            LoggerValidators.validate_max_bytes(60000000)

    def test_validate_backup_count(self):
        """
        Test the validate_backup_count method of LoggerValidators class.

        This test ensures that the method correctly validates the number of
        backup logs, and raises appropriate exceptions for non-integer, and
        out-of-bound inputs.
        """

        # Test with a valid backup count
        LoggerValidators.validate_backup_count(5)

        # Test with a non-integer backup count
        with self.assertRaises(TypeError):
            LoggerValidators.validate_backup_count("5")

        # Test with a negative backup count
        with self.assertRaises(ValueError):
            LoggerValidators.validate_backup_count(-1)

        # Test with an excessive backup count
        with self.assertRaises(ValueError):
            LoggerValidators.validate_backup_count(30)

    def test_validate_log_format(self):
        """
        Test the validate_log_format method of LoggerValidators class.

        This test ensures that the method correctly validates log message formats,
        and raises appropriate exceptions for formats not in the accepted set.
        """

        valid_formats = {"FORMAT1", "FORMAT2"}

        # Test with a valid format
        LoggerValidators.validate_log_format("FORMAT1", valid_formats)

        # Test with an invalid format
        with self.assertRaises(ValueError):
            LoggerValidators.validate_log_format("INVALID_FORMAT", valid_formats)

    def test_validate_use_color(self):
        """
        Test the validate_use_color method of LoggerValidators class.

        This test ensures that the method correctly validates the 'use_color'
        flag, and raises appropriate exceptions for non-boolean inputs.
        """

        # Test with a valid boolean flag
        LoggerValidators.validate_use_color(True)

        # Test with a non-boolean flag
        with self.assertRaises(TypeError):
            LoggerValidators.validate_use_color("True")

    def test_validate_directory_is_writable(self):
        """
        Test the validate_directory_is_writable method of LoggerValidators class.

        This test ensures that the method can correctly validate directory paths
        for existence and writability.
        """

        # Assuming a temporary directory that does exist and is writable
        temp_directory = "/tmp"

        # Test with a valid directory
        LoggerValidators.validate_directory_is_writable(temp_directory)

        # Test with a non-existent directory
        with self.assertRaises(ValueError):
            LoggerValidators.validate_directory_is_writable("/nonexistent/directory")

        # Test with a non-writable directory (assuming root-owned directory for this test)
        # This might not raise an exception if tests are run as root (not recommended)
        with self.assertRaises(ValueError):
            LoggerValidators.validate_directory_is_writable("/root")


if __name__ == "__main__":
    unittest.main()
