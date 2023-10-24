"""
This module provides the LoggerValidators class, a collection of static methods
explicitly designed to validate logging-related parameters. Through type checks
and boundary conditions, it ensures consistent and valid configurations for the
MagikLogger logging utility.

Version: 1.0.0
"""

import os
import pathlib

from typing import Optional, Set


class LoggerValidators:
    """
    A utility class providing static methods for parameter validation.

    This class contains methods designed to ensure the validity of parameters
    commonly used within the MagikLogger logging utility. Each method checks
    a specific type of parameter (e.g., string, boolean, integer), and raises
    appropriate exceptions if the input doesn't meet the expected criteria.
    """

    @staticmethod
    def validate_string_parameter(param: str,
                                  param_name: str) -> None:
        """
        Validates if a given parameter is a non-empty string.

        Parameters
        ----------
        param: str
            The parameter to validate.

        param_name: str
            The name of the parameter.

        Raises
        ------
        TypeError
            If the provided parameter is not of type 'str'.

        ValueError
            If the provided string is empty or consists solely of whitespace.

        Example
        -------
        >>> LoggerValidators.validate_string_parameter("info", "example_param")
        """

        # Check if the parameter is a string
        if not isinstance(param, str):
            invalid_type = type(param)
            raise TypeError(
                f"LoggerValidators Error.\n"
                f"The provided {param_name} ({param}) should be of type 'str'. "
                f"Got '{invalid_type}'.")

        # Check if the string is not empty or just whitespace
        if not param.strip():
            raise ValueError(
                f"LoggerValidators Error.\n"
                f"Provided {param_name} cannot be an empty string or consist of whitespace.")

    @staticmethod
    def validate_boolean_parameter(param: bool,
                                   param_name: str) -> None:
        """
        Validates if a given parameter is a boolean.

        Parameters
        ----------
        param: bool
            The parameter to validate.

        param_name: str
            The name of the parameter.

        Raises
        ------
        TypeError
            If the provided parameter is not of type 'bool'.

        Example
        -------
        >>> LoggerValidators.validate_boolean_parameter(True, "example_param")
        """

        # Check if the parameter is a boolean
        if not isinstance(param, bool):
            invalid_type = type(param)
            raise TypeError(
                f"LoggerValidators Error.\n"
                f"The provided {param_name} ({param}) should be of type 'bool'. "
                f"Got '{invalid_type}'.")

    @staticmethod
    def validate_integer_parameter(param: int,
                                   param_name: str,
                                   min_val: Optional[int] = None,
                                   max_val: Optional[int] = None) -> None:
        """
        Validates if a given parameter is an integer within the specified
        range.

        Parameters
        ----------
        param: int
            The parameter to validate.

        param_name: str
            The name of the parameter.

        min_val: int, default=None
            The minimum acceptable value for the parameter.

        max_val: int, default=None
            The maximum acceptable value for the parameter.

        Raises
        ------
        TypeError
            If the provided parameter is not of type 'int'.

        ValueError
            If the provided integer is not within the specified range.

        Example
        -------
        >>> LoggerValidators.validate_integer_parameter(150, "example_param")
        """

        # Check if the parameter is an integer
        if not isinstance(param, int):
            invalid_type = type(param)
            raise TypeError(
                f"LoggerValidators Error.\n"
                f"The provided {param_name} ({param}) should be of type 'int'. "
                f"Got '{invalid_type}'.")

        # Check if the integer is within the provided range
        if ((min_val is not None and param < min_val) or
                (max_val is not None and param > max_val)):
            raise ValueError(
                f"LoggerValidators Error.\n"
                f"The provided {param_name} should be between {min_val} and {max_val}. "
                f"Got {param}.")

    @staticmethod
    def validate_logger_name(logger_name: str) -> None:
        """
        Validate the provided logger_name parameter.

        Parameters
        ----------
        logger_name: str
            The logger name to validate.
        """

        # Validate that the provided logger_name parameter is a string
        LoggerValidators.validate_string_parameter(param=logger_name,
                                                   param_name="logger_name")

    @staticmethod
    def validate_logger_path(logger_path: str) -> None:
        """
        Validate the provided logger_path parameter.

        Parameters
        ----------
        logger_path: str
            Path to the log file to validate.
        """

        # Validate that the provided logger_path parameter is a string
        LoggerValidators.validate_string_parameter(param=logger_path,
                                                   param_name="logger_path")

    @staticmethod
    def validate_log_level(log_level: str,
                           valid_log_levels: Set[str]) -> None:
        """
        Validate the provided log_level parameter.

        Parameters
        ----------
        log_level: str
            Log level to validate.

        valid_log_levels: Set[str]
            A set of valid log levels.

        Raises
        ------
        ValueError
            If the provided log_level is not among the accepted levels.
        """

        # Validate that the provided log_level parameter is a string
        LoggerValidators.validate_string_parameter(param=log_level,
                                                   param_name="log_level")

        # Check if the log_level value is in the accepted levels
        if log_level.upper().strip() not in valid_log_levels:
            raise ValueError(
                f"LoggerValidators Error.\n"
                f"Invalid log level: {log_level}. "
                f"Log level must be one of: {', '.join(valid_log_levels)}.")

    @staticmethod
    def validate_log_to_console(log_to_console: bool) -> None:
        """
        Validates the 'log_to_console' parameter.

        Parameters
        ----------
        log_to_console: bool
            A flag determining whether logs should be output to the console.
        """

        # Validate if log_to_console is a boolean
        LoggerValidators.validate_boolean_parameter(param=log_to_console,
                                                    param_name="log to console")

    @staticmethod
    def validate_log_to_file(log_to_file: bool) -> None:
        """
        Validates the 'log_to_file' parameter.

        Parameters
        ----------
        log_to_file: bool
            A flag determining whether logs should be written to a file.
        """

        # Validate if log_to_file is a boolean
        LoggerValidators.validate_boolean_parameter(param=log_to_file,
                                                    param_name="log to file")

    @staticmethod
    def validate_max_bytes(max_bytes: int) -> None:
        """
        Validate the provided max_bytes parameter.

        Parameters
        ----------
        max_bytes: int
            Maximum size of log file (in bytes).
            Should be a positive integer less than or equal to 50,000,000.
        """

        # Using the existing integer validation method
        LoggerValidators.validate_integer_parameter(param=max_bytes,
                                                    param_name="max_bytes",
                                                    min_val=1,
                                                    max_val=50000000)

    @staticmethod
    def validate_backup_count(backup_count: int) -> None:
        """
        Validate the provided backup_count parameter.

        Parameters
        ----------
        backup_count: int
            Number of backup log files to keep.
            Should be a positive integer less than or equal to 20.
        """

        # Using the existing integer validation method
        LoggerValidators.validate_integer_parameter(param=backup_count,
                                                    param_name="backup_count",
                                                    min_val=1,
                                                    max_val=20)

    @staticmethod
    def validate_log_format(log_format: str,
                            valid_formats: Set[str]) -> None:
        """
        Validate the provided log_format parameter.

        Parameters
        ----------
        log_format: str
            The format string for log messages.

        valid_formats: Set[str]
            A set of acceptable formats.

        Raises
        ------
        ValueError
            If log_format parameter is not a string or not among
            acceptable formats.
        """

        # Using the existing string validation method
        LoggerValidators.validate_string_parameter(param=log_format,
                                                   param_name="log_format")

        if log_format not in valid_formats:
            raise ValueError(
                f"LoggerValidators Error.\n"
                f"Invalid log message format: {log_format}. "
                f"Format must be one of: {', '.join(valid_formats)}.")

    @staticmethod
    def validate_use_color(use_color: bool) -> None:
        """
        Validates the 'use_color' parameter.

        Parameters
        ----------
        use_color: bool
            A flag determining whether logs should be color-coded for
            enhanced readability.
        """

        # Using the existing boolean validation method
        LoggerValidators.validate_boolean_parameter(param=use_color,
                                                    param_name="use_color")

    @staticmethod
    def validate_directory_is_writable(directory: pathlib.Path) -> None:
        """
        Check if the directory is writable.

        Parameters
        ----------
        directory: pathlib.Path
            The path to validate.

        Raises
        ------
        ValueError
           If the provided directory path is not writable.
        """

        # Check if the directory is writable
        if not os.access(directory, os.W_OK):
            raise ValueError(
                f"LoggerValidators Error.\n"
                f"Directory path is not writable: {directory}. "
                f"Ensure you have the necessary permissions.")
