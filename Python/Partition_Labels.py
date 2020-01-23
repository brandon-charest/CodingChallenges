"""763 Partition Labels

A string S of lowercase letters is given. We want to partition this string into as many parts as possible
so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]

Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:
S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
"""
from typing import List


def partitionLabels(S: str) -> List[int]:
    res = []
    dic = {}
    for i in range(len(S)):
        dic[S[i]] = i
    i = 0
    while i < len(S):
        end = dic[S[i]]
        j = i
        while j != end:
            end = max(end, dic[S[j]])
            j += 1
        res.append(j - i + 1)
        i = j + 1
    return res


print(partitionLabels('ababcbacadefegdehijhklij'))
