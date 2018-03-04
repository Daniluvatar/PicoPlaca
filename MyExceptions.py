class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class FormatError(Error):
    """Exception raised for formatting errors.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
        expected_format -- the format which is expected as input
    """

    def __init__(self, expression, message, expected_format):
        self.expression = expression
        self.message = message + " format is " + expected_format


class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
