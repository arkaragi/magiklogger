# Changelog for BaseLogger Class

## Version 1.0.0 - [2023-10-24]

### Added

    Introduced the BaseLogger class, a comprehensive abstraction over Python's built-in logging module.

    Implemented support for customizable console and/or file logging with options such as:
        - Specifying log level
        - Defining log message format
        - Controlling log file size and the number of backup log files

    Provided integration with the 'coloredlogs' library for color-coded console output.

    Integrated comprehensive validation checks for initialization parameters using the LoggerValidators class.

    Added methods for setting up and configuring handlers:
        - Console handler setup with optional colored output
        - File handler setup with file rotation capabilities

    Implemented utility methods:
        - Configuring handlers with the desired log level and formatter
        - Directory creation for log file storage
        - Removal of existing logger handlers

    Provided detailed docstrings for the class and its methods, ensuring clear understanding and ease of use.

    Implemented properties for accessing logger configurations like logger name, path, level, format, etc.
    
    Added a test suite for the base.py module.


### Future Extensions

    Implement a configuration dictionary or class for cleaner management of default parameters.

    Extend color customizations for console logging, allowing users to specify colors for different log levels.

    Introduce support for logger initialization from a configuration file.

    Refactor utility methods into a separate utility mixin or class to streamline the BaseLogger class structure.
