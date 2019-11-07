"""
Write a function that, given an array A consisting of N integers, returns the maximum sum
of two numbers whose digits add up to an equal sum. If there are no two numbers whose digits have an equal sum,
the function should return -1.

Example:
Given A = [51,71,17,42], the function should return 93. There are two pairs of numbers whose digits add up to an equal
sum: (51,42) and (17,71). The first pair sums up to 93.


"""

import unittest
from typing import List


def find_digit_sum(num: int) -> int:
    res = 0
    while num:
        res += num % 10
        num //= 10
    return res


def equal_digit_sum(A: List[int]) -> int:
    dict = {}
    result = []
    unique = True
    for i in A:
        digit_sum = find_digit_sum(i)
        if digit_sum in dict:
            result.append(dict[digit_sum] + i)
            unique = False
        else:
            dict[digit_sum] = i
    if unique:
        return -1
    return max(result)


class Test_Equal_Digit_Sum(unittest.TestCase):

    def setUp(self) -> None:
        self.A = [51, 71, 17, 42]
        self.B = [42, 33, 60]
        self.C = [51, 32, 43]

    def test_should_return_93(self):
        assert equal_digit_sum(self.A) == 93

    def test_should_return_102(self):
        assert equal_digit_sum(self.B) == 102

    def test_should_return_neg1(self):
        assert equal_digit_sum(self.C) == -1


if __name__ == '__main__':
    unittest.main()
