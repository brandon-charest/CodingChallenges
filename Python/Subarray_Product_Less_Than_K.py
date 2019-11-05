

from typing import List
from collections import deque


# sliding window
def subarray_lessthan_k(nums: List[int], k: int) -> int:
    prod, res = 1, 0
    dq = deque()

    for i in nums:
        dq.append(i)
        prod *= i
        while prod >= k and dq:
            prod /= dq.popleft()
        res += len(dq)
    return res


arr = [10, 5, 2, 6]
k = 100
print(subarray_lessThan_K(arr, k))
