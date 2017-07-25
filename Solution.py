from MathOperations import MathOperation

"""
Python file for implementing the solution of the project
"""


class Solution:
    """
    This class is responsible for the calculation of the value of alpha and the length between the two coasters of same radius
    """

    @staticmethod
    def alpha():
        """
        This static method calculates the value of alpha
        :return:float alpha
        """
        firstGuess = 2.0
        pi = MathOperation.pi()
        delta = firstGuess - MathOperation.sin(firstGuess) - pi / 2
        alpha = firstGuess
        while delta <= 1 / MathOperation.powers(10, 3):
            delta = alpha - MathOperation.sin(alpha) - pi / 2
            alpha += 1 / MathOperation.powers(10, 2)

        return alpha

    @staticmethod
    def getLenght(radius):
        """
        This static method calculates the length based on the value of alpha
        :param radius:
        :return:float length
        """
        alpha = Solution.alpha()
        return 2.0 * radius * (1.0 - MathOperation.cos(alpha / 2))
