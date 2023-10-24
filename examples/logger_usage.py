"""
Usage Example for MagikLogger.

This module demonstrates the various capabilities of the MagikLogger class.
It provides hands-on examples for initializing the logger, adjusting its
settings, logging messages of different severities, and making dynamic changes
to its configurations.
"""

import os

from magiklogger.magiklogger.magik.magik_logger import MagikLogger


def main():

    # 1. Initializing MagikLogger with custom settings.
    logger = MagikLogger(
        logger_name="CustomLogger",
        logger_path="custom_logs",
        log_level="INFO",
        log_to_console=True,
        log_to_file=False,
        max_bytes=1000,
        backup_count=3,
        use_color=True
    )
    logger.info("Logger initialized with custom settings.")

    # 2. Logging messages at different levels.
    logger.debug("This is a debug message (won't appear due to default INFO level).")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")

    # 3. Changing the log level dynamically.
    logger.set_log_level("DEBUG")
    logger.debug("Now this debug message will appear after changing the log level.")

    # 4. Enable file logging.
    logger.enable_file_logging()
    logger.info("This message will be logged to both the console and a file.")

    # 5. Customizing log format.
    custom_format = '%(asctime)s | %(levelname)s | %(message)s'
    logger.set_log_format(custom_format)
    logger.info("Log format has been changed to showcase date, log level, and the message.")

    # 6. Disabling console logging.
    logger.enable_console_logging(enable=False)
    logger.warning("This warning message will only be logged to the file, not the console.")

    # 7. Using color-coded logging (assuming the feature's implementation in MagikLogger).
    logger.enable_console_logging(enable=True)
    logger.info("Re-enabled console logging with color-coding.")

    logger.error("This is an error message in color.")
    logger.critical("This is a critical message in color.")

    # 8. Demonstrate log rotation (to visually show this, you'd need a more elaborate setup).
    for _ in range(10000):
        logger.debug("This is a repetitive debug message to fill up the log and demonstrate rotation.")

    # 9. Disabling file logging after enabling it.
    logger.enable_file_logging(enable=False)
    logger.info("This info message will only appear in the console since file logging is disabled.")

    # 10. Displaying the beginning of the log file's content.
    log_file_path = os.path.join("custom_logs", "CustomLogger.log")
    with open(log_file_path, 'r') as file:
        lines = file.readlines()
        print("\n\nDisplaying the first lines from the log file:")
        for line in lines[:10]:
            print(line.strip())

    # 11. Showcasing backup files created due to rotation.
    log_directory = "custom_logs"
    all_files = os.listdir(log_directory)
    backup_files = [file for file in all_files if "CustomLogger" in file]
    print("\n\nList of log files and backup files due to rotation:")
    for backup in sorted(backup_files):
        print(backup)

    logger.info("End of the demonstration. Check the logs directory for rotated log files.")


if __name__ == "__main__":
    main()
