# Changelog for LoggerValidators Class

## Version 1.0.0 - [10/22/2023]

## Added

    Introduced the LoggerValidators class for validating logging-related parameters.

    Implemented basic parameter type checks for strings, booleans, and integers.

    Integrated error handling, raising TypeError and ValueError exceptions as necessary.

    Added specific validation methods for logger configurations:
        - Logger name validation
        - Logger path validation
        - Log level validation
        - Console and file logging flags validation
        - Max bytes for logging validation
        - Backup count for logs validation
        - Logging format validation
        - Usage of colored output
        - Directory write permission validation

    Added a test suite for the validators.py module.
    

## Future Extensions

    Integrate more complex validation checks, such as regular expression matching for certain parameters.

    Expand the set of logger configurations that can be validated, considering more advanced logging features.
