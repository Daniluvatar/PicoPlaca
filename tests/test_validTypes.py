from unittest import TestCase, main

# My libraries
from Validations import ValidTypes


class TestValidTypes(TestCase):

    def test_validateString(self):
        ValidTypes.validateString("a")
        ValidTypes.validateString("word")

    def test_validateString_arg_numbers(self):
        self.assertRaises(ValueError, ValidTypes.validateString, 7541)

    def test_validateString_arg_not_string(self):
        self.assertRaises(ValueError, ValidTypes.validateString, [4, 5])
        self.assertRaises(ValueError, ValidTypes.validateString, (14, 15))

    def test_validateNumber(self):
        ValidTypes.validateNumber(1451)
        ValidTypes.validateNumber(5.4)

    def test_validateNumber_arg_string(self):
        self.assertRaises(ValueError, ValidTypes.validateNumber, "7541")

    def test_validateNumber_arg_not_string(self):
        self.assertRaises(ValueError, ValidTypes.validateString, [4, 5])
        self.assertRaises(ValueError, ValidTypes.validateString, (14, 15))

    def test_validateInt(self):
        ValidTypes.validateInteger(7)

    def test_validateInt_invalid_args(self):
        self.assertRaises(ValueError, ValidTypes.validateInteger, "7")
        self.assertRaises(ValueError, ValidTypes.validateInteger, 0.7)
        self.assertRaises(ValueError, ValidTypes.validateInteger, [7])

    def test_validateList(self):
        ValidTypes.validateList([10, 20])

    def test_validateList_invalid_args(self):
        self.assertRaises(ValueError, ValidTypes.validateList, "10")
        self.assertRaises(ValueError, ValidTypes.validateList, (10, 20))


if __name__ == "__main__":
    main()
