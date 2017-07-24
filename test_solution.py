from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_alpha(self):
        self.assertEqual(2.329999999999993, Solution.alpha())

class TestSolution(TestCase):
    def test_getLenght(self):
        self.assertEqual(2.4209978350850294,Solution.getLenght(2))
