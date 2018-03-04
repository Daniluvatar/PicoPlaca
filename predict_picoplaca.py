from Vehicle import Car

"""
Pico y placa predictor program that can
be run on command line 
"""


if __name__ == "__main__":
    plate = input("Enter plate number: ")
    date = input("Enter date: ")
    time = input("Enter time: ")
    car = Car(plate)
    car.canBeOnRoad(date, time)

