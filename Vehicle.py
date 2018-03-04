from Restrictions import PicoPlaca


class Car:
    """
    Class used to represent car objects
    """

    def __init__(self, plate):
        self.plate = plate

    def canBeOnRoad(self, date, time):

        if PicoPlaca.isRestrictionDay(date, self.plate) and PicoPlaca.isRestrictionTime(time):
            print(f"The car cannot be on the road because of \"Pico y Placa\" restriction")
            return False
        else:
            print(f"The car can be on the road. Start the car... ")
            return True
