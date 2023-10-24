"""
Usage Example for MagikSetup class.

This module offers a hands-on demonstration of integrating the MagikSetup
and MagikLogger classes within a sample project framework. By following
the practices in this examples:

- Users can understand how to efficiently set up and configure the logger
  using MagikSetup.

- Experience the versatility of MagikLogger's features, including dynamic
  log level adjustments, custom log formatting, color-coded logging, and
  more.

- Discover best practices for initializing and employing a logger within
  a project setting.

The ExampleProject class acts as a reference architecture, illustrating
the integration of logging mechanisms within a software system's infrastructure.
By leveraging the capabilities of MagikLogger and MagikSetup, developers
can augment the system's resilience, traceability, and diagnostic capabilities,
optimizing the development lifecycle and ensuring operational efficiency.
For detailed configurations and advanced logging capabilities, consult the
MagikLogger documentation.
"""

import os

from magiklogger.magiklogger.setup.magik_setup import MagikSetup


class ExampleProject:
    """
    A sample class representing an examples project that requires
    logging capabilities.

    Parameters:
    -----------
    config_path: Optional[str]
        Path to the logger configuration file.
        If not provided, the default configuration path will be used.

    Attributes:
    -----------
    magik_setup: MagikSetup
        Instance of the MagikSetup class to handle logger configurations
        and initialization.

    logger: MagikLogger
        Logger instance initialized via MagikSetup, offering various
        logging functionalities.

    Methods:
    --------
    run():
        Demonstrate various logging capabilities of the MagikLogger.
    """

    def __init__(self, config_path=None):
        # Initialize a MagikSetup instance with the provided configuration path.
        self.magik_setup = MagikSetup(config_path=config_path)

        # Load configurations from the specified path or use the default configuration.
        self.magik_setup.initialize_config()

        # Set up and initialize the logger based on the loaded configurations.
        self.magik_setup.initialize_logger()

        # Retrieve the logger instance from MagikSetup for use within this class.
        self.logger = self.magik_setup.logger

    def run(self):
        """
        A sample method to demonstrate the logging capabilities after initialization.
        """

        # 1. Basic Logging
        self.logger.info("Starting the ExampleProject...")
        self.logger.debug("This is a debug message.")
        self.logger.warning("This is a warning message.")
        self.logger.error("This is an error message.")

        # 2. Changing the log level dynamically
        self.logger.set_log_level("DEBUG")
        self.logger.debug("Now this debug message will appear after changing the log level.")

        # 3. Enable file logging
        self.logger.enable_file_logging()
        self.logger.info("This message will be logged to both the console and a file.")

        # 4. Customizing log format
        custom_format = '%(asctime)s | %(levelname)s | %(message)s'
        self.logger.set_log_format(custom_format)
        self.logger.info("Log format has been changed to showcase date, log level, and the message.")

        # 5. Using color-coded logging (assuming the feature's implementation in MagikLogger)
        self.logger.error("This is an error message in color.")
        self.logger.critical("This is a critical message in color.")

        # 6. Disabling file logging
        self.logger.enable_file_logging(enable=False)
        self.logger.info("This info message will only appear in the console since file logging is disabled.")

        # 7. Displaying a snippet from the log file (assuming logger is set to default 'logs' directory)
        log_file_path = os.path.join("logs", "MagikLogger.log")
        if os.path.exists(log_file_path):
            with open(log_file_path, 'r') as file:
                lines = file.readlines()
                self.logger.info("\n\nDisplaying the first lines from the log file:")
                for line in lines[:5]:
                    self.logger.info(line.strip())

        self.logger.info("Finishing the ExampleProject...")


if __name__ == "__main__":

    # Using the default MagikSetup configuration
    project = ExampleProject()
    project.run()

    # Optionally, you could provide a custom config path when initializing the ExampleProject:
    # project_with_custom_config = ExampleProject(config_path="path/to/custom/config.json")
    # project_with_custom_config.run()
