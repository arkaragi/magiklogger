"""
This module provides the BaseLogger class, an abstraction over Python's built-in
logging module.

The BaseLogger class allows for customizable console and/or file logging, with
options such as specifying log level, defining log message format, controlling
log file size and the number of backup log files. It's designed for offering a
convenient and standardized way to handle application logging needs.

Additionally, this module utilizes the 'coloredlogs' library to provide color
coded console output, enhancing readability in terminal environments.

Version: 1.0.0
"""

import logging
import pathlib

from logging.handlers import RotatingFileHandler
from typing import Optional

import coloredlogs

from magiklogger.core.validators import LoggerValidators


class BaseLogger:
    """
    Base class for MagikLogger objects.

    BaseLogger simplifies logging with customizable options like log levels,
    message formats, and file rotations. Designed for diverse needs, it aids
    developers in efficiently monitoring and tracing program activities.

    If neither console nor file logging is enabled, the logger defaults to
    console logging.

    Parameters
    ----------
    logger_name: str
        The name of the logger.

    logger_path: str
        Path for storing log files.

    log_level: str
        The level of logging.

    log_to_console: bool
        Flag to determine if logs should be output to the console.

    log_to_file: bool
        Flag to determine if logs should be written to a file.

    max_bytes: int
        Maximum size (in bytes) of a log file before it gets rotated. 
        This parameter is applicable only if 'log_to_file' is True.

    backup_count: int
        Number of backup log files to keep.
        This parameter is applicable only if 'log_to_file' is True.

    log_format: str
        Format of the log message.

    use_color: bool, default=False
        If True, coloredlogs will be used to provide color-coded console
        output for different logging levels.
    """

    # Set of supported levels of logging
    VALID_LOG_LEVELS = {
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL"
    }

    # Set of acceptable formats
    VALID_FORMATS = {
        '%(asctime)s - %(levelname)s - %(message)s',
        '%(asctime)s - %(message)s',
        '%(levelname)s - %(message)s'
    }

    # Define the default color scheme for log levels
    DEFAULT_COLOR_SCHEME = {
        "DEBUG": {"color": "blue"},
        "INFO": {"color": "green"},
        "WARNING": {"color": "yellow"},
        "ERROR": {"color": "red"},
        "CRITICAL": {"color": "red", "bold": True},
    }

    def __init__(self,
                 logger_name: str,
                 logger_path: str,
                 log_level: str,
                 log_to_console: bool,
                 log_to_file: bool,
                 max_bytes: int,
                 backup_count: int,
                 log_format: str,
                 use_color: bool):

        # Validate initialization parameters
        self._validate_init_parameters(logger_name,
                                       logger_path,
                                       log_level,
                                       log_to_console,
                                       log_to_file,
                                       max_bytes,
                                       backup_count,
                                       log_format,
                                       use_color)

        # Initialize instance attributes
        self._logger_name = logger_name
        self._logger_path = logger_path
        self._log_level = log_level
        self._log_to_console = log_to_console
        self._log_to_file = log_to_file
        self._max_bytes = max_bytes
        self._backup_count = backup_count
        self._log_format = log_format
        self._use_color = use_color

        # Initialize a Logger object with a specified name
        self.logger = logging.getLogger(self._logger_name)

        # Explicitly set the logger's level
        self.logger.setLevel(self._log_level)

        # Configure the logger
        self._setup_logger()

    @property
    def logger_name(self) -> str:
        """
        Return the name of the Logger object.
        """

        return self._logger_name

    @property
    def logger_path(self) -> str:
        """
        Return the path where the log files are stored.
        """

        return self._logger_path

    @property
    def log_level(self) -> str:
        """
        Return the level of logging.
        """

        return self._log_level

    @property
    def log_to_console(self) -> bool:
        """
        Return True if logs should be output to the console,
        False otherwise.
        """

        return self._log_to_console

    @property
    def log_to_file(self) -> bool:
        """
        Return True if logs should be written to a file,
        False otherwise.
        """

        return self._log_to_file

    @property
    def max_bytes(self) -> int:
        """
        Return the maximum size (in bytes) of a log file before
        it gets rotated.
        """

        return self._max_bytes

    @property
    def backup_count(self) -> int:
        """
        Return the number of backup log files to keep.
        """

        return self._backup_count

    @property
    def log_format(self) -> str:
        """
        Return the format of the log message.
        """

        return self._log_format

    @property
    def use_color(self) -> bool:
        """
        Return the value of use_color parameter.
        """

        return self._use_color

    def _configure_handler(self,
                           log_level: str,
                           handler: logging.Handler,
                           formatter: logging.Formatter) -> None:
        """
        Configures a logging handler with provided log level and formatter,
        and then adds it to the logger.

        Parameters
        ----------
        log_level: str
            The level of logging. Supported values are:
            "DEBUG", "INFO", "WARNING", "ERROR" and "CRITICAL".

        handler: logging.Handler
            The logging handler to be configured.

        formatter: logging.Formatter
            The logging formatter.
        """

        try:
            # Set the log level for the handler
            handler.setLevel(log_level)
        except ValueError as e:
            msg = (f"Invalid log level provided: {log_level}. "
                   f"Error: {e}")
            raise ValueError(msg)

        try:
            # Set the formatter for the handler
            handler.setFormatter(formatter)
        except TypeError as e:
            msg = (f"Invalid formatter provided: {formatter}. "
                   f"Error: {e}")
            raise TypeError(msg)

        # Add the handler to the logger
        self.logger.addHandler(handler)

    def _make_directory(self) -> None:
        """
        Create the directory where log files will be stored, if it doesn't
        already exist.

        Raises
        ------
        IOError
            Raised if the specified path does not exist or is invalid.

        Exception
            Raised for other unknown errors while making the directory.
        """

        # Convert the provided path to a Path object
        directory = pathlib.Path(self.logger_path)

        try:
            # Create the directory if it doesn't exist
            directory.mkdir(parents=True, exist_ok=True)

            # Validate that the directory is writable
            LoggerValidators.validate_directory_is_writable(directory)

        except IOError as e:
            msg = (f"The specified path {directory} does not exist or is invalid. "
                   f"Error: {e}.")
            raise IOError(msg)

        except Exception as e:
            msg = (f"An unknown error occurred while making the directory. "
                   f"Error: {e}.")
            raise Exception(msg)

    def _remove_handlers(self) -> None:
        """
        Closes any existing handlers attached to the logger and removes them.
        """

        # Clear any existing handlers attached to the logger
        if self.logger.handlers:
            for handler in self.logger.handlers:
                try:
                    handler.close()
                except Exception as e:
                    # Log an error message in case of any exceptions
                    handler_details = {
                        "type": type(handler).__name__,
                        "formatter": str(handler.formatter),
                        "level": logging.getLevelName(handler.level),
                        "filters": [str(f) for f in handler.filters],
                    }
                    msg = (f"Error closing handler: {handler_details}. "
                           f"Error: {e}")
                    self.logger.error(msg)
                else:
                    self.logger.removeHandler(handler)

    def _setup_logger(self) -> None:
        """
        Prepares the logger with user-specified configurations.

        Validates log level and logger path, then initializes the logger object.
        If there are no existing handlers, sets up new console and file handlers
        based on the provided parameters.
        """

        # Clear existing handlers, if any
        self._remove_handlers()

        # Get the logging level from the string representation
        log_level = logging.getLevelName(self.log_level.upper())
        self.logger.setLevel(log_level)

        # Create a log message formatter
        formatter = self._setup_formatter()

        # If neither console nor file logging is enabled,
        # enable console logging by default
        if not self._log_to_console and not self.log_to_file:
            msg = ("At least one logging output should be enabled. "
                   "Enabling console logging by default.")
            self.logger.warning(msg)
            self._log_to_console = True

        # Set up handlers for console and file
        if self._log_to_console:
            self._setup_console_handler(log_level, formatter)

        if self._log_to_file:
            self._setup_file_handler(log_level, formatter)

    def _setup_formatter(self,
                         log_format: Optional[str] = None) -> logging.Formatter:
        """
        Sets up the log message format.

        Parameters
        ----------
        log_format: str, default=None
            The format of the log message.
            If None, the default format is used.

        Returns
        -------
        formatter: logging.Formatter
            A logging.Formatter object configured with the desired format.
        """

        # If no format is provided, use the default format
        if log_format is None:
            log_format = self.log_format

        return logging.Formatter(fmt=log_format)

    def _setup_console_handler(self,
                               log_level: str,
                               formatter: logging.Formatter) -> None:
        """
        Sets up a console handler for the logger.

        This method creates a StreamHandler instance for console logging and
        configures it with the provided log level and formatter.

        Parameters
        ----------
        log_level: str
            Logging level for the console handler.

        formatter: logging.Formatter
            A Formatter object for the console handler.
        """

        # Check if the logger already has a StreamHandler
        has_stream_handler = False
        for handler in self.logger.handlers:
            if isinstance(handler, logging.StreamHandler):
                has_stream_handler = True
                break

        if not has_stream_handler:
            # Create a StreamHandler instance for console logging
            console_handler = logging.StreamHandler()

            # Configure the console handler with the provided level and format
            self._configure_handler(log_level, console_handler, formatter)

            # Enhance the logger to show colored logs in console
            if self.use_color:
                coloredlogs.install(level=log_level,
                                    logger=self.logger,
                                    fmt=self.log_format,
                                    level_styles=self.DEFAULT_COLOR_SCHEME)

    def _setup_file_handler(self,
                            log_level: str,
                            formatter: logging.Formatter) -> None:
        """
        Sets up a file handler for the logger.

        This method creates a RotatingFileHandler instance for file logging and
        configures it with the provided log level, and formatter. This type of
        handler will rotate the log files when they reach a certain size, thus
        preserving old logs for a certain number of rotations

        Parameters
        ----------
        log_level: str
            Logging level for the file handler.

        formatter: logging.Formatter
            A Formatter object for the file handler.
        """

        # Ensure the directory for logging exists
        self._make_directory()

        # Check if the logger already has a RotatingFileHandler
        has_rotating_file_handler = False
        for handler in self.logger.handlers:
            if isinstance(handler, RotatingFileHandler):
                has_rotating_file_handler = True
                break

        if not has_rotating_file_handler:
            # Create a RotatingFileHandler instance for file logging.
            filename = pathlib.Path(self.logger_path) / self.logger_name
            file_handler = RotatingFileHandler(filename=f"{filename}.log",
                                               maxBytes=self.max_bytes,
                                               backupCount=self.backup_count)

            # Configure the file handler with the provided log level and formatter
            self._configure_handler(log_level, file_handler, formatter)

    def _validate_init_parameters(self,
                                  logger_name,
                                  logger_path,
                                  log_level,
                                  log_to_console,
                                  log_to_file,
                                  max_bytes,
                                  backup_count,
                                  log_format,
                                  use_color) -> None:
        """
        Validates the initialization parameters for the BaseLogger.
        """

        # Validate logger_name parameter
        LoggerValidators.validate_logger_name(logger_name)

        # Validate logger_path parameter
        LoggerValidators.validate_logger_path(logger_path)

        # Validate log_level parameter
        LoggerValidators.validate_log_level(log_level,
                                            self.VALID_LOG_LEVELS)

        # Validate log_to_console parameter
        LoggerValidators.validate_log_to_console(log_to_console)

        # Validate log_to_file parameter
        LoggerValidators.validate_log_to_file(log_to_file)

        # Validate max_bytes parameter
        LoggerValidators.validate_max_bytes(max_bytes)

        # Validate backup_count parameter
        LoggerValidators.validate_backup_count(backup_count)

        # Validate log_format parameter
        LoggerValidators.validate_log_format(log_format,
                                             self.VALID_FORMATS)

        # Validate use_color parameter
        LoggerValidators.validate_use_color(use_color)
