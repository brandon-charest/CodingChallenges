"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""
from typing import List


def findDuplicates(nums: List[int]) -> List[int]:
    if nums is None or len(nums) is 0:
        return []

    res = []
    nums.sort()

    if len(nums) is 1:
        return res
    p1 = 1

    while p1 < len(nums):
        if nums[p1] == nums[p1 - 1]:
            res.append(nums[p1])
        p1 += 1
    return res



test = [4,3,2,7,8,2,3,1]
print(findDuplicates(test))