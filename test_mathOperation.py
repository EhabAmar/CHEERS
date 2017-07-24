from unittest import TestCase

from MathOperations import MathOperation

class TestMathOperation(TestCase):
    """
    This class is responsible for testing the method of MathOperation class
    """
    def test_pi(self):
        """
        Test case for testing pi method
        :return:nothing
        """
        self.assertEqual(3.14159265359, MathOperation.pi())

    def test_sin(self):
        """
        Test case for  testing sin method
        :return:nothing
        """

        self.assertEqual(0.8414709848078965, MathOperation.sin(1.0))

    def test_negative_sin(self):
        """
        Test Case for testing sin method against a negative value
        :return:nothing
        """
        self.assertEqual(-0.8414709848078965, MathOperation.sin(-1.0))

    def test_cos(self):
        """
        Test case for testing cos method
        :return:nothing
        """
        self.assertEqual(0.5403023058681398, MathOperation.cos(1.0))

    def test_cos_negativevalue(self):
        """
        Test case for testing cos method against negative value
        :return:nothing
        """
        self.assertEqual(0.5403023058681398, MathOperation.cos(-1.0))
