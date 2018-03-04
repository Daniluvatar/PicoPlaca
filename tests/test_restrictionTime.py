from unittest import TestCase, main

# Mi libraries
from Restrictions import PicoPlaca
from MyExceptions import InputError, FormatError


class TestRestrictionTime(TestCase):

    def test_isRestrictionTime_morning(self):
        self.assertTrue(PicoPlaca.isRestrictionTime("7:54"))

    def test_isRestrictionTime_afternoon(self):
        self.assertTrue(PicoPlaca.isRestrictionTime("17:00"))

    def test_isNotRestrictionTime_morning(self):
        self.assertFalse(PicoPlaca.isRestrictionTime("09:31"))

    def test_isNotRestrictionTime_afternoon(self):
        self.assertFalse(PicoPlaca.isRestrictionTime("13:07"))

    def test_isRestrictionTime_invalid_format(self):
        self.assertRaises(FormatError, PicoPlaca.isRestrictionTime, "15:30:45")

    def test_isRestrictionTime_invalid_input(self):
        self.assertRaises(ValueError, PicoPlaca.isRestrictionTime, "time:time")
        self.assertRaises(ValueError, PicoPlaca.isRestrictionTime, 14)

    def test_isRestrictionTime_invalid_hours(self):
        self.assertRaises(InputError, PicoPlaca.isRestrictionTime, "30:15")

    def test_isRestrictionTime_invalid_minutes(self):
        self.assertRaises(InputError, PicoPlaca.isRestrictionTime, "12:89")

    def test_isRestrictionTime_invalid_hours_min(self):
        self.assertRaises(InputError, PicoPlaca.isRestrictionTime, "78:67")


if __name__ == "__main__":
    main()
