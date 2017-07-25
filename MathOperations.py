"""
Python file for Math Operations
"""


class MathOperation:
    """
    This class is responsible for performing various math operations need for the project
    """

    PRECISION = 9

    @staticmethod
    def powers(base=float, exp=int):
        """
        This method is responsible for calculating the exponential number
        :param base: float
        :param exp: int
        :return: float value
        """
        result = 1.0
        for i in range(0, exp):
            result *= base
        return result

    @staticmethod
    def factorials(input=int):
        """
        This method for performing the factorial on a given number
        :param input: int
        :return: float factorial value
        """
        if input == 0 or input == 1:
            return 1
        else:
            return input * MathOperation.factorials(input - 1)

    @staticmethod
    def drange(start=float, stop=float, step=float):
        """
        This method is used for the computing the value of the pi
        :param start: float
        :param stop: float
        :param step: float
        :return: float value
        """
        while start < stop:
            yield start
            start += step

    @staticmethod
    def pi():
        """
        This method is responsible for calculating the value of pi
        :return: float pi
        """
        n = MathOperation.powers(10, 5)
        sign = 1.0
        temp = 0.0
        for i in MathOperation.drange(2.0, n, 2.0):
            temp = temp + sign * (1 / (i * (i + 1) * (i + 2)))
            sign *= -1
        pi = 3 + (4 * temp)
        return pi

    @staticmethod
    def sin(input=float):
        """
        This method is responsible for computing the value of sin
        :param input: float
        :return:float sin value
        """
        result = input
        for i in range(1, MathOperation.PRECISION):
            if i % 2 == 0:
                result += MathOperation.powers(input, 2 * i + 1) / MathOperation.factorials(2 * i + 1)
            else:
                result -= MathOperation.powers(input, 2 * i + 1) / MathOperation.factorials(2 * i + 1)
        return result

    @staticmethod
    def cos(input=float):
        """
        This method is responsible for computing the value of cos
        :param input: float
        :return: float cos value
        """
        result = 1.0
        for i in range(1, MathOperation.PRECISION):
            if i % 2 == 0:
                result += MathOperation.powers(input, 2 * i) / MathOperation.factorials(2 * i)
            else:
                result -= MathOperation.powers(input, 2 * i) / MathOperation.factorials(2 * i)
        return result
