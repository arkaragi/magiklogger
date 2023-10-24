# MagikLogger

Experience the magic of effortless logging with MagikLogger - a powerful, intuitive logging utility specifically
designed for Python applications. Crafted with an emphasis on simplicity and flexibility, MagikLogger strives to 
simplify application-level logging, transforming it from a chore into a charm.

Whether your needs are as simple as console logging or as complex as file-based logging with log rotation, 
MagikLogger caters to a broad spectrum of logging needs. Its dynamic capabilities and user-focused design 
ensure that your logging requirements, regardless of scale or complexity, are met with seamless efficiency.

Join us on this magical journey and discover the future of hassle-free, efficient logging with MagikLogger. 
Let's make your logging experiences not just productive, but also magical!

## Key Features

    - Simple Setup: Get started with MagikLogger with just a few lines of code.

    - Console Logging: Get instant feedback during your development and debugging process with console logs.
    
    - File Logging: Save your logs to files for long-term storage or detailed post-mortem analysis.
    
    - Dynamic Log Levels: Adjust log levels during runtime to control the detail of logs you want to record.

    - Log Formatting: Customize your logs with metadata like timestamps, log levels, and message content.

    - Log Rotation: Prevent unmanageable log files and exhausted disk space with log rotation based on file size.

    - Color-Coded Logging: Enhance your console logs with color-coded outputs based on the log level, 
      ensuring better readability and instant recognition of log severities.

## Getting Started

### Prerequisites

    Python 3.8 or above

### Installation

To install MagikLogger, follow these steps:

1. Clone the MagikLogger repository from GitHub:

       git clone https://github.com/arkaragi/magiklogger.git

2. Change your current directory to the cloned repository

       cd magiklogger

3. Install the package using pip

       pip install .

### Basic Usage

Import the MagikLogger from the magik_logger package. Initialize the logger with your desired configuration.

Here's a simple example: 
    
    from magiklogger.magik.magik_logger import MagikLogger
    
    # Create a logger instance
    logger = MagikLogger(logger_name="AppLogger",
                         logger_path="logs",
                         log_to_console=True,
                         log_to_file=False,
                         log_level="INFO")
    
    # Log a message
    logger.info("This is a test log message.")


### Running Tests

MagikLogger has comprehensive tests to ensure the reliability and robustness of both basic and advanced features. 
To run the tests and validate the integrity of the logger, ensure you're in the root directory of the repository,
and run the following command in your terminal:

    python -m unittest tests/test_logger.py

If all tests pass, your logger is good to go! 
If you encounter any issues, please report them in our GitHub issues section.

## Contributing

We're excited that you're considering contributing to the MagikLogger project!
Every contribution, no matter how small, helps us make this tool better. 
Whether you're tackling existing issues, suggesting new features, improving the
documentation, or even correcting a tiny typo, we appreciate your help.

## License

This project is licensed under the MIT License. For more information, see LICENSE.