""" 1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
from typing import List


def two_sum(nums: List[int], target: int):
    result = {}

    for i in range(len(nums)):
        value = target - nums[i]
        if value in result:
            return [i, result[value]]
        result.update({nums[i]: i})

    return result


numbers = [2, 7, 11, 15]
t = 9

print(two_sum(numbers, t))
