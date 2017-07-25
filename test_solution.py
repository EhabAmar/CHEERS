from unittest import TestCase
from Solution import Solution

"""
Pythom file for testing the method of solution python file
"""


class TestSolution(TestCase):
    """
    This class is responsible for testing various method of Solution class
    """

    def test_alpha(self):
        """
        Test case for testing method for computing alpha
        :return:nothing
        """
        self.assertEqual(2.329999999999993, Solution.alpha())

    def test_getLength(self):
        """
        Test case for testing method for computing Length
        :return:nothing
        """
        self.assertEqual(2.4209978350850294, Solution.getLenght(2))
