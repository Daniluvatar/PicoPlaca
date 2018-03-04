from unittest import TestCase, main

# My libraries
from Validations import ValidTime
from MyExceptions import InputError, FormatError


class TestValidTime(TestCase):

    def test_validateTime(self):
        ValidTime.validateTime("14:30")
        ValidTime.validateTime("7:37")

    def test_validateTime_invalid_format(self):
        self.assertRaises(FormatError, ValidTime.validateTime, "15:30:45")

    def test_validateTime_invalid_input(self):
        self.assertRaises(ValueError, ValidTime.validateTime, "time:time")
        self.assertRaises(ValueError, ValidTime.validateTime, 14)

    def test_validateTime_invalid_hours(self):
        self.assertRaises(InputError, ValidTime.validateTime, "30:15")

    def test_validTime_invalid_minutes(self):
        self.assertRaises(InputError, ValidTime.validateTime, "12:89")

    def test_validTime_invalid_hours_min(self):
        self.assertRaises(InputError, ValidTime.validateTime, "78:67")


if __name__ == "__main__":
    main()
