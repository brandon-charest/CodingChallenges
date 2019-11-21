""" 11. Container With Most Water
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical
lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together
with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49

"""
from typing import List
import unittest


def max_area(height: List[int]) -> int:
    area, left, right = 0, 0, len(height) - 1
    while left < right:
        l = right - left
        h = min(height[left], height[right])
        a = l * h
        area = max(area, a)
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return area


class Test_Max_Area(unittest.TestCase):

    def test_returns_49(self):
        assert max_area([1,8,6,2,5,4,8,3,7]) == 49

    def test_returns_1(self):
        assert max_area([1,1]) == 1

    def test_returns_6(self):
        assert max_area([1,5,4,3]) == 6

    def test_returns_24(self):
        assert max_area([1,3,2,5,25,24,5]) == 24


if __name__ == '__main__':
    unittest.main()