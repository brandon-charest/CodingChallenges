""" 724. Find Pivot Index
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to
the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the
left-most pivot index.

Example 1:
Input:
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.


Example 2:
Input:
nums = [1, 2, 3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""

from typing import List

# too slow for test
# def pivot_index(nums: List[int]) -> int:
#     if not nums:
#         return -1
#     for i in range(len(nums)):
#         if sum(nums[:i]) == sum(nums[i + 1:]):
#             return i
#     return -1


def pivot_index(nums: List[int]) -> int:
    if not nums:
        return -1
    left, right = 0, sum(nums)
    for i in range(len(nums)):
        if left == right - nums[i] - left:
            return i
        left += nums[i]

    return -1


x = [1, 7, 3, 6, 5, 6]
print(pivot_index(x))
