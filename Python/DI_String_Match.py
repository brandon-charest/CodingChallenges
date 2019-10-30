"""
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]


Example 1:

Input: "IDID"
Output: [0,4,1,3,2]
"""
from typing import List


class DiStringMatch:
    @staticmethod
    def di_string_match(s: str) -> List[int]:
        min_num, max_num, result = 0, len(s), []
        for c in s:
            if c == 'I':
                result.append(min_num)
                min_num += 1
            elif c == 'D':
                result.append(max_num)
                max_num -= 1
        result.append(max_num)
        return result


string_match = DiStringMatch()
res = string_match.di_string_match("IDID")
print(res)
res = string_match.di_string_match("III")
print(res)
res = string_match.di_string_match("DIDI")
print(res)
res = string_match.di_string_match("DDI")
print(res)
