"""
This module defines the MagikLogger class, which implements a flexible event
logging system for Python applications and libraries.

The MagikLogger class supports logging messages at different levels to the
console, to a file, or both. It also supports log rotation to prevent files
from growing indefinitely. In addition, the log level can change dynamically
after the logger has been created.

Features
--------
    - Console and/or File Logging: Directs logging output to the console, a file,
      or both simultaneously depending on your requirements.

    - Variable Log Levels: Supports a range of log levels (DEBUG, INFO, WARNING,
      ERROR, CRITICAL) for granular control over the verbosity of logging output.

    - Log File Rotation: Implements a size-based log file rotation mechanism to
      prevent indefinite file growth. This ensures that older logs are archived
      and only the most recent logs are kept in the current log file.

    - Dynamic Log Level Adjustment: Allows for changing the log level on-the-fly,
      even after the logger has been instantiated.

    - Parameter Validation: Validates critical parameters such as the log level
      and logger path for robustness.

    - Color-Coded Logging: Enhance your console logs with color-coded outputs
      based on the log level, ensuring better readability and instant recognition
      of log severities.

Version: 1.0.0
"""

import logging
import traceback

from logging.handlers import RotatingFileHandler
from typing import Optional

from magiklogger.magiklogger.core.base import BaseLogger


class MagikLogger(BaseLogger):
    """
    The MagikLogger class provides a versatile and high-performance Python
    logging toolkit, designed for magical debugging experiences and general
    application logging.

    This class allows creating a customizable logger with the ability to log
    messages to both the console and a file, depending on user's preference.
    It supports different logging levels, that can be specified upon object
    initialization. Moreover, the log level can change dynamically after the
    logger has been created.

    The logger is also equipped with a rotating file handler, ensuring that
    log files don't grow indefinitely. This mechanism automatically rotates
    log files when they reach a specific size, preserving older logs across
    several backup files.

    Parameters
    ----------
    logger_name: str, default="MagikLogger.log"
        Name of the logger.

    logger_path: str, default="logs"
        Path where the log file should be stored.

    log_level: str, default="INFO"
        The level of logging. Supported values are:
        "DEBUG", "INFO", "WARNING", "ERROR" and "CRITICAL".

    log_to_console: bool, default=True
        Flag to determine if logs should be output to console.

    log_to_file: bool, default=False
        Flag to determine if logs should be written to a file.

    max_bytes: int, default=5000000
        Maximum size of a log file in bytes before it gets rotated.
        This parameter is applicable only if 'log_to_file' is True.
        The default value (5000000) means each log file will be up
        to approximately 5 MB.

    backup_count: int, default=5
        Number of backup log files to keep.
        This parameter is applicable only if 'log_to_file' is True.

    log_format: str, default='%(asctime)s - %(levelname)s - %(message)s'
        The format of the log message.
        It dictates the structure of the output messages in the log.
        Should be one of the following:
            - '%(asctime)s - %(levelname)s - %(message)s',
            - '%(asctime)s - %(message)s',
            - '%(levelname)s - %(message)s'

    use_color: bool, default=False
        If True, coloredlogs will be used to provide color-coded console output
        for different logging levels, enhancing readability in terminal environments.
        This is especially useful for quickly distinguishing between different log
        severities. If set to False, the logs will be displayed without any color
        enhancements.
    """

    def __init__(self,
                 logger_name: Optional[str] = "MagikLogger",
                 logger_path: Optional[str] = "logs",
                 log_level: str = "INFO",
                 log_to_console: bool = True,
                 log_to_file: bool = False,
                 max_bytes: int = 5000000,
                 backup_count: int = 5,
                 log_format: str = '%(asctime)s - %(levelname)s - %(message)s',
                 use_color: bool = True):
        super().__init__(logger_name,
                         logger_path,
                         log_level,
                         log_to_console,
                         log_to_file,
                         max_bytes,
                         backup_count,
                         log_format,
                         use_color)

    # # Utility Methods # #

    def _log_message(self,
                     log_level: int,
                     msg: str) -> None:
        """
        Logs a message with the specified log level.

        Parameters
        ----------
        log_level: int
            The level of the log message.

        msg: str
            The message to be logged.
        """

        try:
            # Use the built-in log method to log the message at the specified level
            self.logger.log(log_level, msg)

        # If an error occurs, log the error message and full traceback
        except AttributeError:
            error_msg = f"AttributeError encountered while logging the message"
            detailed_error = f"{error_msg}: {msg}\n{traceback.format_exc()}"
            self.logger.log(logging.ERROR, detailed_error)

        except TypeError:
            error_msg = f"TypeError encountered while logging the message"
            detailed_error = f"{error_msg}: {msg}\n{traceback.format_exc()}"
            self.logger.log(logging.ERROR, detailed_error)

        except Exception as e:
            error_msg = (f"Unexpected error {type(e).__name__} encountered while "
                         f"logging the message")
            detailed_error = f"{error_msg}: {msg}\n{traceback.format_exc()}"
            self.logger.log(logging.ERROR, detailed_error)

    def _set_log_format(self,
                        log_format: str) -> None:
        """
        Changes the format of the log message for all handlers.

        Parameters
        ----------
        log_format: str
            The new format of the log message.
        """

        # Set the new log format for log_format attribute
        self._log_format = log_format

        # Set up a new formatter using the specified format
        formatter = self._setup_formatter(log_format)

        # Iterate over all the handlers currently in the logger
        for handler in self.logger.handlers:
            # Change the formatter for each handler to the new formatter
            handler.setFormatter(formatter)

    def _set_log_level(self, log_level: str) -> None:
        """
        Changes the log level of the logger.

        Parameters
        ----------
        log_level: str
            The new level of logging. Supported values are:
            "DEBUG", "INFO", "WARNING", "ERROR" and "CRITICAL".

        Raises
        ------
        ValueError
            If the new log level is not valid or an error occurs while
            changing the log level.
        """

        # Set the new log level for log_level attribute
        self._log_level = log_level

        # Get the integer value corresponding to the log level string
        log_level_value = getattr(logging, log_level.upper(), None)

        if log_level_value is None:
            raise ValueError(f"Invalid log level provided: {log_level}")

        # Set the new log level for the logger object
        self.logger.setLevel(log_level_value)

        # Set the new log level for each handler of the logger
        for handler in self.logger.handlers:
            handler.setLevel(log_level_value)

    def _enable_logging(self,
                        enable: bool,
                        handler_type: type):
        """
        Enable or disable logging for a specific handler type.

        Parameters
        ----------
        enable: bool, default=True
            If True, enable logging for the specified handler type.
            If False, disable logging for the specified handler type.

        handler_type: logging.Handler
            The type of the handler to be enabled or disabled.
        """
        if enable:
            if not self._handler_exists(handler_type):
                # Add a handler of the specified type
                self._add_handler(handler_type)
        else:
            if self._handler_exists(handler_type):
                self._remove_handler(handler_type)

    def _handler_exists(self,
                        handler_type: type):
        """
        Checks if a handler of a specific type already exists.

        Parameters
        ----------
        handler_type: logging.Handler
            The type of the handler to be checked.

        Returns
        ----------
        exists: bool
            True if a handler of the specified type exists, False otherwise.
        """
        # Checks if a handler of a specific type already exists
        exists = any(isinstance(handler, handler_type)
                     for handler in self.logger.handlers)
        return exists

    def _add_handler(self,
                     handler_type: type):
        """
        Adds a new handler of the provided type with the initialized log level
        and format.

        Parameters
        ----------
        handler_type: logging.Handler
            The type of the handler to be added.
        """
        # Setup the log message formatter
        formatter = self._setup_formatter(self.log_format)

        # Add handler based on its type
        if handler_type is logging.StreamHandler:
            # For StreamHandler, setup a console handler
            self._setup_console_handler(self.log_level, formatter)
        elif handler_type is logging.handlers.RotatingFileHandler:
            # For RotatingFileHandler, setup a file handler
            self._setup_file_handler(self.log_level, formatter)

    def _remove_handler(self,
                        handler_type: type):
        """
        Removes all handlers of a specific type.

        Parameters
        ----------
        handler_type: logging.Handler
            The type of the handler to be removed.
        """
        # Keep only handlers which are not of the specified type
        for handler in self.logger.handlers:
            if isinstance(handler, handler_type):
                self.logger.removeHandler(handler)

    # # Public Methods # #

    def debug(self,
              msg: str) -> None:
        """
        Logs a message with the debug level.

        Parameters
        ----------
        msg: str
            The message to be logged.
        """

        # Use the _log_message private method to log at the DEBUG level
        self._log_message(logging.DEBUG, msg)

    def info(self,
             msg: str) -> None:
        """
        Logs a message with the info level.

        Parameters
        ----------
        msg: str
            The message to be logged.
        """

        # Use the _log_message private method to log at the INFO level
        self._log_message(logging.INFO, msg)

    def warning(self,
                msg: str) -> None:
        """
        Logs a message with the warning level.

        Parameters
        ----------
        msg: str
            The message to be logged.
        """

        # Use the _log_message private method to log at the WARNING level
        self._log_message(logging.WARNING, msg)

    def error(self,
              msg: str) -> None:
        """
        Logs a message with the error level.

        Parameters
        ----------
        msg: str
            The message to be logged.
        """

        # Use the _log_message private method to log at the ERROR level
        self._log_message(logging.ERROR, msg)

    def critical(self,
                 msg: str) -> None:
        """
        Logs a message with the critical level.

        Parameters
        ----------
        msg: str
            The message to be logged.
        """

        # Use the _log_message private method to log at the CRITICAL level
        self._log_message(logging.CRITICAL, msg)

    def set_log_format(self,
                       log_format: str) -> None:
        """
        Changes the format of the log message for all handlers.

        Parameters
        ----------
        log_format: str
            The format of the log message.
        """

        # Change the format of the log message for all handlers
        self._set_log_format(log_format)

    def set_log_level(self,
                      log_level: str) -> None:
        """
        Changes the log level after the logger has been created.

        Parameters
        ----------
        log_level: str
            The new level of logging. Supported values are:
            "DEBUG", "INFO", "WARNING", "ERROR" and "CRITICAL".
        """

        # Change the log level of the logger
        self._set_log_level(log_level)

    def enable_console_logging(self,
                               enable: bool = True) -> None:
        """
        Enable or disable console logging.

        Parameters
        ----------
        enable: bool, default=True
            If True, enable logging for the specified handler type.
            If False, disable logging for the specified handler type.
        """

        # Set the handler type to StreamHandler for console logging
        handler_type = logging.StreamHandler

        # Update the log_to_console parameter
        self._log_to_console = enable

        # Call the helper method to enable or disable console logging
        self._enable_logging(enable, handler_type)

    def enable_file_logging(self,
                            enable: bool = True) -> None:
        """
        Enable or disable file logging.

        Parameters
        ----------
        enable: bool, default=True
            If True, enable logging for the specified handler type.
            If False, disable logging for the specified handler type.
        """

        # Set the handler type to RotatingFileHandler for file logging
        handler_type = logging.handlers.RotatingFileHandler

        # Update the log_to_file parameter
        self._log_to_file = enable

        # Call the helper method to enable or disable file logging
        self._enable_logging(enable, handler_type)
