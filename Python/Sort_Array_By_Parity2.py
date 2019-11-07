""" 922. Sort Array By Parity II
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
You may return any answer array that satisfies this condition.

Example 1:
Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
"""

from typing import List


def is_even(num):
    if num % 2 is 0:
        return True
    return False


def sort_array_by_parity(A: List[int]) -> List[int]:
    result = []
    even = []
    odd = []
    for i in range(len(A)):
        if is_even(A[i]):
            even.append(A[i])
        else:
            odd.append(A[i])
    for i in range(len(A)):
        if is_even(i):
            result.append(even.pop())
        else:
            result.append(odd.pop())
    return result


# a more pythonic solution
def sort_array_by_parity1(A: List[int]) -> List[int]:
    odd = [x for x in A if not is_even(x)]
    even = [x for x in A if is_even(x)]
    result = []

    for x, y in zip(even, odd):
        result.append(x)
        result.append(y)
    return result


x = [4, 2, 5, 7]
print(sort_array_by_parity1(x))
