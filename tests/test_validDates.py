from unittest import TestCase, main

# My libraries
from Validations import ValidDates
from MyExceptions import InputError


class TestValidDates(TestCase):

    def test_validateDate(self):
        ValidDates.validateDate(2018, 5, 12)

    def test_validateDate_invalid_month(self):
        self.assertRaises(InputError, ValidDates.validateDate, 2018, 14, 12)

    def test_validateDate_invalid_day(self):
        self.assertRaises(InputError, ValidDates.validateDate, 2018, 2, 29)
        self.assertRaises(InputError, ValidDates.validateDate, 2018, 3, 32)
        self.assertRaises(InputError, ValidDates.validateDate, 2018, 4, 31)

    def test_validDate_invalid_args(self):
        self.assertRaises(ValueError, ValidDates.validateDate, "2018", 5, 12)
        self.assertRaises(ValueError, ValidDates.validateDate, 2018, "5", "12")
        self.assertRaises(ValueError, ValidDates.validateDate, 2018, 5, "12")
        self.assertRaises(ValueError, ValidDates.validateDate, 2018, "5", 12)
        self.assertRaises(ValueError, ValidDates.validateDate, "2018", "5", "12")

    def test_validateMonth(self):
        ValidDates.validateMonth(7)

    def test_validateMonth_invalid(self):
        self.assertRaises(InputError, ValidDates.validateMonth, 13)
        self.assertRaises(InputError, ValidDates.validateMonth, -1)

    def test_validateMonth_invalid_args(self):
        self.assertRaises(ValueError, ValidDates.validateMonth, "4")

    def test_validateDateFormat(self):
        self.assertTrue(ValidDates.validateDateFormat("10-05-2018"))
        self.assertTrue(ValidDates.validateDateFormat("03-04-2018"))

    def test_validateDateFormat_invalid(self):
        self.assertRaises(ValueError, ValidDates.validateDateFormat, "99-99-9999")

    def test_validateDateFormat_invalid_day(self):
        self.assertRaises(ValueError, ValidDates.validateDateFormat, "55-30-2015")

    def test_validateDateFormat_invalid_month(self):
        self.assertRaises(ValueError, ValidDates.validateDateFormat, "01-30-2015")

    def test_validateDateFormat_invalid_string(self):
        self.assertRaises(ValueError, ValidDates.validateDateFormat, "pruebas")

    def test_validateDay(self):
        ValidDates.validateDay(5)

    def test_validateDay_invalid(self):
        self.assertRaises(InputError, ValidDates.validateDay, 50)
        self.assertRaises(InputError, ValidDates.validateDay, -4)

    def test_validateDay_invalid_args(self):
        self.assertRaises(ValueError, ValidDates.validateDay, "four")


if __name__ == "__main__":
    main()
