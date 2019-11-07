""" 1200. Minimum Absolute Difference
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute
difference of any two elements.
Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

Example 1:
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

Example 2:
Input: arr = [1,3,6,10,15]
Output: [[1,3]]

Example 3:
Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
"""

from typing import List
import sys


def min_abs_diff(arr: List[int]) -> List[List[int]]:
    result = []
    curr_min = sys.maxsize

    # sort array so min diff pairs are next to each other
    arr.sort()

    for i in range(1, len(arr)):
        curr_diff = arr[i] - arr[i - 1]

        if curr_diff < curr_min:
            curr_min = curr_diff
            result.clear()
            result.append([arr[i-1], arr[i]])
        elif curr_diff is curr_min:
            result.append([arr[i-1], arr[i]])

    return result


x = [4, 2, 1, 3]
print(min_abs_diff(x))
y = [3, 8, -10, 23, 19, -4, -14, 27]
print(min_abs_diff(y))
