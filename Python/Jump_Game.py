""" 55. Jump Game
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example 1:
Input: [2,3,1,1,4]
Output: true

Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: [3,2,1,0,4]
Output: false

Explanation:
You will always arrive at index 3 no matter what. Its maximum
jump length is 0, which makes it impossible to reach the last index.
"""

def can_jump(nums) -> bool:
    if not nums:
        return False
    last_good = nums[-1]
    for i in range(len(nums)-1,-1,-1):
        if nums[i] + i >= last_good:
            last_good = i
    return last_good == 0


print(can_jump([2,3,1,1,4]))