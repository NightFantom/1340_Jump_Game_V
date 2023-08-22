from unittest import TestCase

from main import Solution


class TestSolution(TestCase):

    def test_1(self):
        arr = [6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12]
        d = 2
        expected = 4
        result = Solution().maxJumps(arr, d)
        self.assertEqual(expected, result)

    def test_2(self):
        arr = [3, 3, 3, 3, 3]
        d = 3
        expected = 1
        result = Solution().maxJumps(arr, d)
        self.assertEqual(expected, result)

    def test_3(self):
        arr = [7, 6, 5, 4, 3, 2, 1]
        d = 1
        expected = 7
        result = Solution().maxJumps(arr, d)
        self.assertEqual(expected, result)

    def test_4(self):
        length = 1000
        arr = list(range(length))
        d = length
        expected = length
        result = Solution().maxJumps(arr, d)
        self.assertEqual(expected, result)

    def test_5(self):
        arr = [22, 29, 52, 97, 29, 75, 78, 2, 92, 70, 90, 12, 43, 17, 97, 18, 58, 100, 41, 32]
        d = 17
        expected = 6
        result = Solution().maxJumps(arr, d)
        self.assertEqual(expected, result)

    def test_6(self):
        arr = [22, 29, 52, 97, 29, 75, 78, 2, 92]
        d = 17
        expected = 5
        result = Solution().maxJumps(arr, d)
        self.assertEqual(expected, result)
