import math


def combinations(k: int, n: int):
    return math.factorial(n) / (math.factorial(n - k) * math.factorial(k))


def black_white_balls(n: int, t: int, k: int):
    if k < 1:
      raise ValueError('k must be more than 1!')

    count_black_balls = n - t

    combinationsForAllBalls = combinations(k, n)

    blackBallsCombinations = combinations(k, count_black_balls)

    return 1 - blackBallsCombinations / combinationsForAllBalls
