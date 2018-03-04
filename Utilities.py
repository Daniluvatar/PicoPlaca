from Validations import ValidTypes, ValidDates
from datetime import datetime


class StringOperations:

    """
    This class should implement all the methods needed
    to process all kind of string operations
    """


    @staticmethod
    def getLastChar(string_var):
        """
        Returns the last element of a string
        :param string_var: String
        :return: Last character
        """
        ValidTypes.validateString(string_var)
        return string_var[-1]

    @staticmethod
    def getDay(date_str):
        """
        Get the day of a given date
        :param date_str: Date as string
        :return: Weekday as integer
        """
        ValidTypes.validateString(date_str)
        ValidDates.validateDateFormat(date_str)
        date = datetime.strptime(date_str, '%d-%m-%Y')
        day = date.isoweekday()
        return day
