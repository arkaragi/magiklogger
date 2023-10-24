# Changelog for MagikLogger Class

## Version 1.0.0 - [2023-10-24]

### Added

    Released the MagikLogger class, offering a versatile and high-performance Python logging toolkit. 
    This toolkit is designed for exceptional debugging experiences and general application logging.
    
    Introduced capabilities for logging messages to both console and file systems, allowing users to specify 
    their preferences during logger instantiation.
    
    Integrated support for different logging levels, allowing users to specify upon object initialization and 
    dynamically change the log level post-creation.
    
    Incorporated a rotating file handler mechanism to ensure log files don't grow indefinitely. 
    This auto-rotation triggers when log files reach a specified size, preserving older logs in backup files.
    
    Presented a comprehensive API, including utility methods like:
        - _log_message: For logging messages at specified levels with robust exception handling.
        - _set_log_format: For changing the log message format across all handlers.
        - _set_log_level: To dynamically adjust the logger's log level.
        - _enable_logging: A versatile method to enable or disable logging for specific handler types.
        - _handler_exists, _add_handler, _remove_handler: Methods to manage logger handlers seamlessly.
    
    Offered public methods (debug, info, warning, error, critical) to log messages at respective log levels, 
    providing an intuitive interface for users.
    
    Integrated the ability to dynamically change log format and level post-logger creation using set_log_format 
    and set_log_level methods.
    
    Incorporated methods to enable or disable specific logging channels (console or file) dynamically, 
    enhancing flexibility.
    
    Ensured a high level of robustness and validation, making sure that the logger operates effectively 
    without causing disruptions to the parent application.
    
    Delivered thorough documentation with comprehensive docstrings for each method and the class, 
    ensuring a clear understanding for developers.


### Future Extensions

    Explore advanced handler configurations, such as integrating with external logging services or databases.
    
    Introduce mechanisms to handle multi-threading and multi-processing scenarios seamlessly.
    
    Extend customization capabilities, including advanced formatting options, meta information logging, and more.
    
    Evaluate and integrate performance improvements, ensuring that the logger remains efficient even under heavy logging loads.
