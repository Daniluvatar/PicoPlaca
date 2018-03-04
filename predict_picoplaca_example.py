from Vehicle import Car

"""
A simple example of using the pico y placa predictor program
"""


def example():
    car = Car("PBD-7541")
    car.canBeOnRoad("04-03-2018", "09:35")
    car.canBeOnRoad("05-03-2018", "08:07")

    car2 = Car("PBI-7055")
    car2.canBeOnRoad("05-03-2018", "08:07")
    car2.canBeOnRoad("07-03-2018", "17:45")


if __name__ == "__main__":
    example()
