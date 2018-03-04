from unittest import TestCase, main
from Utilities import StringOperations


class TestStringOperations(TestCase):

    def test_getLastChar(self):
        last_char = StringOperations.getLastChar("PBD-7541")
        self.assertEqual("1", last_char)

    def test_getLastChar_arg_not_string(self):
        self.assertRaises(ValueError, StringOperations.getLastChar, 123)

    def test_getDay(self):
        sunday = StringOperations.getDay("04-03-2018")
        self.assertEqual(7, sunday)

    def test_getDay_invalid_arg(self):
        self.assertRaises(ValueError, StringOperations.getDay, 2018)

    def test_getDay_invalid_string(self):
        self.assertRaises(ValueError, StringOperations.getDay, "day")


if __name__ == "__main__":
    main()
