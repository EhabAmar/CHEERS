from MathOperations import MathOperation


class Solution():
    @staticmethod
    def alpha():
        firstGuess = 2.0
        pi = MathOperation.pi()
        delta = firstGuess - MathOperation.sin(firstGuess) - pi / 2
        alpha = firstGuess
        while (delta <= 1 / MathOperation.powers(10, 3)):
            delta = alpha - MathOperation.sin(alpha) - pi / 2;
            alpha += 1 / MathOperation.powers(10, 2)

        return alpha

    @staticmethod
    def getLenght(radius):
        alpha = Solution.alpha()
        return 2.0 * radius * (1.0 - MathOperation.cos(alpha / 2))
