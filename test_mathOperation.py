from unittest import TestCase

from MathOperations import MathOperation


class TestMathOperation(TestCase):
    def test_pi(self):
        self.assertEqual(3.14159265359, MathOperation.pi())


class TestMathOperation(TestCase):
    def test_sin(self):
        self.assertEqual(0.8414709848078965, MathOperation.sin(1.0))

class TestMathOperation(TestCase):
    def test_sin(self):
        self.assertEqual(-0.8414709848078965, MathOperation.sin(-1.0))


class TestMathOperation(TestCase):
    def test_cos(self):
        self.assertEqual(0.5403023058681398, MathOperation.cos(1.0))

class TestMathOperation(TestCase):
    def test_cos_negativevalue(self):
        self.assertEqual(0.5403023058681398, MathOperation.cos(-1.0))
