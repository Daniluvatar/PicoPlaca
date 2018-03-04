from unittest import TestCase, main

# Mi libraries
from Restrictions import PicoPlaca
from MyExceptions import FormatError


class TestRestrictionDay(TestCase):

    def test_isRestrictionDay(self):
        self.assertTrue(PicoPlaca.isRestrictionDay("05-03-2018", "PBD-7541"))
        self.assertTrue(PicoPlaca.isRestrictionDay("07-03-2018", "PBI-7055"))

    def test_isNotRestrictionDay(self):
        self.assertFalse(PicoPlaca.isRestrictionDay("06-03-2018", "PBD-7541"))
        self.assertFalse(PicoPlaca.isRestrictionDay("08-03-2018", "PBI-7055"))

    def test_isRestrictionDay_wrong_plate(self):
        self.assertRaises(FormatError, PicoPlaca.isRestrictionDay, "05-03-2018", "plate")
        self.assertRaises(FormatError, PicoPlaca.isRestrictionDay, "05-03-2018", "PBD7541")
        self.assertRaises(FormatError, PicoPlaca.isRestrictionDay, "07-03-2018", "PBD:7541")

    def test_isRestrictionDay_invalid_date(self):
        self.assertRaises(ValueError, PicoPlaca.isRestrictionDay, "date", "PBI-7055")

    def test_isRestrictionDay_invalid_format_date(self):
        self.assertRaises(ValueError, PicoPlaca.isRestrictionDay, "07/03/2018", "PBI-7055")


if __name__ == "__main__":
    main()
