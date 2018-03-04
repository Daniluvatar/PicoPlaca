from calendar import monthrange
from datetime import datetime

# My libraries
from MyExceptions import InputError, FormatError


class ValidTypes:
    """
    This class validates that the data types to be sent
    as arguments are the expected ones
    """

    @staticmethod
    def validateString(string):
        if not isinstance(string, str):
            raise ValueError("Argument should be a string")

    @staticmethod
    def validateNumber(number):
        number_types = (int, float, complex)
        if not isinstance(number, number_types):
            raise ValueError("Argument should be a number")

    @staticmethod
    def validateInteger(integer):
        if not isinstance(integer, int):
            raise ValueError("Argument should be an integer")

    @staticmethod
    def validateList(list_arg):
        if not isinstance(list_arg, list):
            raise ValueError("Argument should be a list")


class ValidDates:
    """
    This class has the methods used to validate all
    kind of date arguments
    """

    @staticmethod
    def validateMonth(month):
        ValidTypes.validateNumber(month)
        if month < 1 or month > 12:
            raise InputError("validateMonth", "Month should be between 1 and 12")

    @staticmethod
    def __validateDateValues(year, month, day):
        ValidTypes.validateInteger(year)
        ValidTypes.validateInteger(month)
        ValidTypes.validateInteger(day)

    @staticmethod
    def validateDate(year, month, day):
        """
        This method validates that all year, month and day values
        are consistent
        :param year: integer
        :param month: integer
        :param day: integer
        """
        ValidDates.__validateDateValues(year, month, day)
        ValidDates.validateMonth(month)
        last_day = monthrange(year, month)[1]
        if day < 1 or day > last_day:
            message = "Day of month " + str(month) + \
                      ", should be between 1 and " + str(last_day)
            raise InputError("validateDay", message)

    @staticmethod
    def validateDateFormat(date_str):
        try:
            datetime.strptime(date_str, '%d-%m-%Y')
            return True
        except ValueError:
            raise ValueError("Incorrect date format, should be DD-MM-YYYY")

    @staticmethod
    def validateDay(day):
        """
        This method validates that the day belongs
        to a correct weekday digit representation
        :param day: integer between 1 and 7
        """
        ValidTypes.validateInteger(day)
        if day < 1 or day > 7:
            raise InputError("ValidDates", "Day should be between 1 and 7")


class ValidTime:
    """
    This class has the methods used to validate all
    kind of time arguments
    """

    @staticmethod
    def __validateTimeValues(time_list):
        """
        Since the time argument is string, additional controls
        are required for consistency
        :param time_list: List representing time e.g 8:30 is ["8", "30"]
        :return:
        """
        if len(time_list) > 2:
            raise FormatError("__validTimeValues", "Time", "HH:MM")
        try:
            if int(time_list[0]) < 0 or int(time_list[0]) > 23:
                raise InputError("__validTimeValues", "Time must follow the 24-hour convention")
            if int(time_list[1]) < 0 or int(time_list[1]) > 59:
                raise InputError("__validTimeValues", "Minutes should be between 0 and 59")
        except ValueError:
            raise ValueError("Argument should be an integer")

    @staticmethod
    def validateTime(time):
        """
        This method validates that time values are consistent
        :param time: time as string
        :return:
        """
        ValidTypes.validateString(time)
        if time.split(":") == [time]:  # Control for arguments other than ":" separator
            raise FormatError("validateTime", "Time", "HH:MM")
        else:
            ValidTime.__validateTimeValues(time.split(":"))


class ValidCustom:
    """
    This class has all the custom methods required to
    validate user input
    """

    @staticmethod
    def validatePlate(plate):
        """
        A simplistic validation of the plate number
        :param plate: plate number
        """
        ValidTypes.validateString(plate)
        plate_list = plate.split("-")
        if plate_list == [plate]:  # Control for arguments other than "-" separator
            raise FormatError("validateTime", "Plate", "CCC-NNNN or CCC-NNN")
        else:
            ValidTypes.validateString(plate_list[0])
        try:
            int(plate_list[1])  # Control for the number portion of the plate number
        except ValueError:
            raise ValueError("Wrong plate number format, should be CCC-NNNN or CCC-NNN")
