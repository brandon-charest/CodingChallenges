""" 59. Spiral Matrix II
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
from typing import List


class GenerateSpiralMatrix:

    @staticmethod
    def generate_matrix(num: int) -> List[List[int]]:
        result = [[]]
        if num <= 0:
            return result

        # make matrix of size num
        result = [[0 for x in range(num)] for y in range(num)]

        right = len(result[0]) - 1
        left = 0
        top = 0
        bottom = len(result) - 1
        count = 1

        while left <= right and top <= bottom:
            # move right
            for i in range(left, right + 1):
                result[left][i] = count
                count += 1
            top += 1
            # move down
            for i in range(top, bottom + 1):
                result[i][right] = count
                count += 1
            right -= 1

            if top <= bottom:
                # move left
                for i in range(right, left - 1, -1):
                    result[bottom][i] = count
                    count += 1
                bottom -= 1

            if left <= right:
                # move up
                for i in range(bottom, top - 1, -1):
                    result[i][left] = count
                    count += 1
                left += 1
        return result


number = int(input("Enter a number: "))
res = GenerateSpiralMatrix.generate_matrix(number)
print(res)