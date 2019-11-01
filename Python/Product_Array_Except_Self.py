""" 238. Product of Array Except Self
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to
the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).
"""
from typing import List


class ProductArrayExceptSelf:
    @staticmethod
    def product_array(nums: List[int]) -> List[int]:
        result = []
        if not nums:
            return result
        # product result initialized to 1s
        result = [1 for _ in range(len(nums))]

        prev = 1
        for i in range(len(nums)):
            result[i] = prev
            prev *= nums[i]

        prev = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= prev
            prev *= nums[i]

        return result


arr = [1, 2, 3, 4]
prod_arr = ProductArrayExceptSelf()
print(prod_arr.product_array(arr))
