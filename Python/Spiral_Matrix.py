""" 54. Spiral Matrix
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

from typing import List
import unittest


class SpiralOrder:
    @staticmethod
    def spiral_order(matrix: List[List[int]]) -> List[int]:

        result = []

        if matrix is [] or len(matrix) is 0:
            return result

        right = len(matrix[0]) - 1
        left = 0
        top = 0
        bottom = len(matrix) - 1

        while left <= right and top <= bottom:
            # move right
            for i in range(left, right + 1):
                result.append(matrix[left][i])
            top += 1
            # move down
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                # move left
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                # move up
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result


three_by_three = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

four_by_three = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
]

three_by_five = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
]

result1 = SpiralOrder.spiral_order(three_by_three)
answer1 = [1, 2, 3, 6, 9, 8, 7, 4, 5]
result2 = SpiralOrder.spiral_order(four_by_three)
answer2 = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
result3 = SpiralOrder.spiral_order(three_by_five)
answer3 = [1, 2, 3, 6, 9, 12, 15, 14, 13, 10, 7, 4, 5, 8, 11]


class TestMethod(unittest.TestCase):
    def test_equal1(self):
        self.assertEqual(result1, answer1)

    def test_equal2(self):
        self.assertEqual(result2, answer2)

    def test_equal3(self):
        self.assertEqual(result3, answer3)


unittest.main()
