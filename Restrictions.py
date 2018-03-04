from datetime import datetime

# My libraries
from Validations import ValidTime, ValidCustom
from Utilities import StringOperations


class PicoPlaca:

    @staticmethod
    def __timeRestriction():
        """
        Time restriction representation using a
        dictionary. M: Morning, A: Afternoon
        :return: dictionary of restricted hours
        """
        restriction = {"M": ["7:00", "9:30"],
                       "A": ["16:00", "19:30"]}
        return restriction

    @staticmethod
    def __dayRestriction():
        """
        Days restriction representation using a
        dictionary. Monday: 1, ..., Sunday:7
        :return: dictionary of restricted days
        """
        restriction = {1: [1, 2], 2: [3, 4], 3: [5, 6],
                       4: [7, 8], 5: [9, 10], 6: [],
                       7: []}
        return restriction

    @staticmethod
    def __getTimeRestriction(time_day):
        """
        Return the time restriction in time format
        :param time_day: Char parameter M: Morning, A: Afternoon
        :return: time interval in which the restriction holds
        """
        time_restriction = PicoPlaca.__timeRestriction()
        time_ini = time_restriction[time_day][0]
        time_fin = time_restriction[time_day][1]
        time_ini = datetime.strptime(time_ini, "%H:%M").time()
        time_fin = datetime.strptime(time_fin, "%H:%M").time()
        return time_ini, time_fin

    @staticmethod
    def isRestrictionTime(time_str):
        """
        This method verifies if the time falls inside the
        restriction time established for pico y placa
        :param time_str: time parameter as string
        :return: True or False
        """
        ValidTime.validateTime(time_str)
        time = datetime.strptime(time_str, "%H:%M").time()
        morning_ini, morning_fin = PicoPlaca.__getTimeRestriction("M")
        if morning_ini <= time <= morning_fin:
            return True

        afternoon_ini, afternoon_fin = PicoPlaca.__getTimeRestriction("A")
        if afternoon_ini <= time <= afternoon_fin:
            return True

        return False

    @staticmethod
    def isRestrictionDay(date_str, plate):
        """
        This method verifies if the plate number is
        restricted based on the day
        :param date_str: Date as string
        :param plate: plate number
        :return: True or False
        """
        ValidCustom.validatePlate(plate)
        day = StringOperations.getDay(date_str)
        if day == 6 or day == 7:
            return False
        else:
            last_char = StringOperations.getLastChar(plate)
            last_char = int(last_char)
            day_restriction = PicoPlaca.__dayRestriction()
            plate_restriction = day_restriction[day]
            if last_char == plate_restriction[0] or last_char == plate_restriction[1]:
                return True
            else:
                return False
