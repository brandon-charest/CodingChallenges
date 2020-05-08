from typing import List

def helper(r, pascal):
    if r == 0:
        return pascal
    if r == 1:
        pascal.append([1])
        return pascal
    elif r == 2:
        helper(1, pascal)
        pascal.append([1, 1])
        return pascal
    helper(r-1, pascal)
    res, prev = [1], pascal[-1]
    for i in range(len(prev) - 1):
        res.append(prev[i] + prev[i+1])
    res.append(1)
    pascal.append(res)
    return pascal

def generate(num_rows: int) -> List[List[int]]:
   return helper(num_rows, [])
