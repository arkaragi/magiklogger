"""
MagikSetup: Configuration Manager for MagikLogger

The MagikSetup class is a part of the MagikLogger suite, which aims to facilitate
the setup, and management of logging configurations. While the main functionality
of logging resides in MagikLogger, the MagikSetup class is designed to streamline
the initialization process by leveraging configurations from external JSON files.

Features
--------
- Centralized Configuration Management: Use a single JSON file to set up and
  modify logging configurations without changing the code.
- Flexibility: Comes with a set of default logging settings but allows users
  to define custom settings to adapt to specific project needs.
- Seamless Integration: Designed to work hand-in-hand with MagikLogger,
  ensuring a cohesive logging experience.

Note: For more detailed configurations and logging capabilities, refer to the
MagikLogger documentation.

Version: 1.0.0
"""

import datetime
import json
import logging
import pathlib

from typing import Optional

from magiklogger.magik.magik_logger import MagikLogger


class MagikSetup:
    """
    MagikSetup is a utility class that centralizes logging setup and management
    based on configurations from a specified JSON file.

    While it comes equipped with a set of default logging settings suitable for
    general use, it offers the flexibility for users to define their own settings
    in the configuration file, adapting to specific project needs.

    Parameters
    ----------
    config_path: Optional[str]
        Path to the configuration file. If not provided, a default will be used.

    Attributes
    ----------
    DEFAULT_LOGGER_SETTINGS: dict
        A dictionary of default settings for the logger.

    config: dict
        Dictionary holding configurations read from the provided JSON file.

    logger: MagikLogger
        An initialized logger based on the configurations.

    Example
    -------
    >>> magik_setup = MagikSetup()
    >>> magik_setup.initialize_config()
    >>> magik_setup.initialize_logger()
    >>> magik_setup.logger.info("This is an info log!")
    """

    # Defines the file path to the JSON file containing config settings
    CONFIG_PATH = (
            pathlib.Path(__file__).parent.parent / "config" / "config.json"
        )

    # A dictionary of default settings for the logger.
    # - `logger_name`: The default name for the log file.
    # - `logger_path`: The default directory where the log files will be stored.
    # - `log_level`: The default logging level (e.g., INFO, DEBUG, WARNING, etc.)
    # - `log_to_console`: A boolean indicating if logs should also be printed to the console.
    # - `log_to_file`: A boolean indicating if logs should be written to a file.
    DEFAULT_LOGGER_SETTINGS = {
            "logger_name": "MagikLogger",
            "logger_path": "logs",
            "log_level": "INFO",
            "log_to_console": True,
            "log_to_file": False,
            "max_bytes": 5000000,
            "backup_count": 5,
            "log_format": "%(asctime)s - %(levelname)s - %(message)s",
            "use_color": True,
        }

    def __init__(self,
                 config_path: Optional[str] = None):
        if config_path:
            self.config_path: pathlib.Path = pathlib.Path(config_path)
        else:
            self.config_path: pathlib.Path = self.CONFIG_PATH

        self.config = None
        self.logger = None

    def initialize_config(self) -> None:
        """
        Initialize the configuration for the MagikSetup class.

        This method reads the JSON configuration file named "config.json" and
        stores its contents in a dictionary for further use.

        By default, the "config.json" is expected to be located in a "config"
        directory at the same level as the directory containing this module.
        Specifically, the path is:
            - [directory containing this module]/../config/config.json

        Raises
        ------
        FileNotFoundError:
            If the configuration file does not exist at the specified
            location.

        json.JSONDecodeError:
            If there's an error while parsing the configuration JSON
            file.

        PermissionError:
            If the method lacks the necessary permissions to read the
            configuration file.

        UnicodeDecodeError:
            If the configuration file contains characters that are not
            valid UTF-8.

        OSError:
            For other system-related errors while trying to read the
            configuration file.
        """

        try:
            # Read the configuration file and parse its contents
            self.config = json.loads(self.config_path.read_bytes())

        except FileNotFoundError:
            msg = (f"Configuration file not found: {self.config_path}. "
                   "Ensure the configuration file is properly set.")
            logging.log(logging.ERROR, msg)
            raise

        except json.JSONDecodeError as e:
            msg = (f"Failed to parse the configuration file: {self.config_path}. "
                   f"Error: {str(e)}. "
                   f"Ensure the configuration file contains valid JSON.")
            logging.log(logging.ERROR, msg)
            raise

        except PermissionError:
            msg = (f"Permission denied when trying to read the configuration file: "
                   f"{self.config_path}. Ensure you have the necessary permissions.")
            logging.log(logging.ERROR, msg)
            raise

        except UnicodeDecodeError:
            msg = (f"Configuration file at {self.config_path} contains invalid UTF-8 "
                   f"characters. Ensure the file is properly encoded.")
            logging.log(logging.ERROR, msg)
            raise

        except OSError as e:
            msg = (f"An error occurred while trying to read the configuration file: "
                   f"{self.config_path}. Error: {str(e)}")
            logging.log(logging.ERROR, msg)
            raise

    def initialize_logger(self) -> None:
        """
        Initialize the logging system for the MagikSetup class.

        This method sets up the MagikLogger based on configurations fetched from
        a JSON configuration file. It's a custom logger that logs activities,
        operations, and potential issues encountered during the logger setup
        and its subsequent use.

        Raises
        ------
        KeyError:
            If the expected logger configuration key is missing from the
            configuration file.

        Exception:
            If any other error occurs during logger initialization.
        """

        # Extract the magik_logger section
        try:
            config = self.config["magik_logger"]
        except KeyError:
            msg = ("The 'magik_logger' key is missing from the configuration file. "
                   "Ensure the configuration file is correctly set up.")
            logging.log(logging.ERROR, msg)
            raise

        try:
            # Extract logger configurations with default values from the class parameter
            logger_name = config.get(
                'logger_name', self.DEFAULT_LOGGER_SETTINGS['logger_name'])
            logger_path = config.get(
                'logger_path', self.DEFAULT_LOGGER_SETTINGS['logger_path'])
            log_level = config.get(
                'log_level', self.DEFAULT_LOGGER_SETTINGS['log_level'])
            log_to_console = config.get(
                'log_to_console', self.DEFAULT_LOGGER_SETTINGS['log_to_console'])
            log_to_file = config.get(
                'log_to_file', self.DEFAULT_LOGGER_SETTINGS['log_to_file'])
            max_bytes = config.get(
                'max_bytes', self.DEFAULT_LOGGER_SETTINGS['max_bytes'])
            backup_count = config.get(
                'backup_count', self.DEFAULT_LOGGER_SETTINGS['backup_count'])
            log_format = config.get(
                'log_format', self.DEFAULT_LOGGER_SETTINGS['log_format'])
            use_color = config.get(
                'use_color', self.DEFAULT_LOGGER_SETTINGS['use_color'])

            # Initialize logger with extracted configurations
            self.logger = MagikLogger(logger_name=logger_name,
                                      logger_path=logger_path,
                                      log_level=log_level,
                                      log_to_console=log_to_console,
                                      log_to_file=log_to_file,
                                      max_bytes=max_bytes,
                                      backup_count=backup_count,
                                      log_format=log_format,
                                      use_color=use_color)

            # Informative logging messages at the initialization of MagikLogger
            self.logger.info("=" * 70)
            self.logger.info("Initializing MagikLogger")
            self.logger.info(f"- Logger Name: {logger_name}")
            self.logger.info(f"- Log Storage Path: {logger_path}")
            self.logger.info(f"- Logging Level: {log_level}")
            self.logger.info(f"- Log to Console: {log_to_console}")
            self.logger.info(f"- Log to File: {log_to_file}")
            self.logger.info(f"- Max Bytes: {max_bytes}")
            self.logger.info(f"- Backup Count: {backup_count}")
            self.logger.info(f"- Log Format: {log_format}")
            self.logger.info(f"- Use Color: {use_color}")
            self.logger.info(f"- Initialization Timestamp: {datetime.datetime.now()}")
            self.logger.info("Monitoring logger activities and potential issues...")
            self.logger.info("=" * 70)

        except Exception as e:
            msg = f"An error occurred during logger initialization: {str(e)}."
            logging.log(logging.ERROR, msg)
            raise
