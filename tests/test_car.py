from unittest import TestCase, main

# My libraries
from Vehicle import Car
from MyExceptions import FormatError


class TestCar(TestCase):

    def setUp(self):
        self.car = Car("PBD-7541")

    def test_canBeOnRoad_weekend(self):
        self.assertTrue(self.car.canBeOnRoad("04-03-2018", "8:30"))
        self.assertTrue(self.car.canBeOnRoad("03-03-2018", "8:30"))

    def test_canBeOnRoad_weekday_morning(self):
        self.assertTrue(self.car.canBeOnRoad("05-03-2018", "9:45"))

    def test_canBeOnRoad_weekday_afternoon(self):
        self.assertTrue(self.car.canBeOnRoad("05-03-2018", "15:00"))

    def test_canBeOnRoad_weekday(self):
        self.assertTrue(self.car.canBeOnRoad("07-03-2018", "9:45"))

    def test_cannotBeOnRoad_weekday_morning(self):
        self.assertFalse(self.car.canBeOnRoad("05-03-2018", "08:45"))

    def test_cannotBeOnRoad_weekday_afternoon(self):
        self.assertFalse(self.car.canBeOnRoad("05-03-2018", "18:00"))

    def test_canBeOnRoad_invalid_date_time(self):
        self.assertRaises(ValueError, self.car.canBeOnRoad, "date", "time")

    def test_canBeOnRoad_invalid_date(self):
        self.assertRaises(ValueError, self.car.canBeOnRoad, "date", "8:30")

    def test_canBeOnRoad_invalid_time(self):
        self.assertRaises(FormatError, self.car.canBeOnRoad, "05-03-2018", "time")

    def test_canBeOnRoad_invalid_date_format(self):
        self.assertRaises(ValueError, self.car.canBeOnRoad, "03/03/2018", "8:30")

    def test_canBeOnRoad_invalid_time_format(self):
        self.assertRaises(FormatError, self.car.canBeOnRoad, "05-03-2018", "8h30")


if __name__ == "__main__":
    main()
