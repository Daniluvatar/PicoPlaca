from unittest import TestCase, main

# My libraries
from Validations import ValidCustom
from MyExceptions import FormatError


class TestValidCustom(TestCase):

    def test_validatePlate(self):
        ValidCustom.validatePlate("PBD-7541")

    def test_validatePlate_invalid_format(self):
        self.assertRaises(FormatError, ValidCustom.validatePlate, "PBD7541")
        self.assertRaises(FormatError, ValidCustom.validatePlate, "PBD:7541")
        self.assertRaises(FormatError, ValidCustom.validatePlate, "plate")

    def test_validatePlate_invalid_input(self):
        self.assertRaises(ValueError, ValidCustom.validatePlate, "PBD-PBD")
        self.assertRaises(ValueError, ValidCustom.validatePlate, "PBD-X7400")
        self.assertRaises(ValueError, ValidCustom.validatePlate, "PBD-74X0")


if __name__ == "__main__":
    main()
