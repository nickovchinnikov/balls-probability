import unittest
from black_white_balls import combinations, black_white_balls


class TestBlackWhite(unittest.TestCase):

    def test_combinator_2_5(self):
        self.assertEqual(combinations(2, 5), 10)

    def test_combinator_5_10(self):
        self.assertEqual(combinations(5, 10), 252)

    def test_black_white_balls_error(self):
        with self.assertRaises(ValueError):
            black_white_balls(14, 6, 0)

    def test_black_white_balls1(self):
        self.assertEqual(black_white_balls(14, 6, 5), 0.972027972027972)

    def test_black_white_balls2(self):
        self.assertEqual(black_white_balls(10000, 500, 100), 0.9942327551246828)


if __name__ == '__main__':
    unittest.main()
