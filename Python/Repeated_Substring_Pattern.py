""" 459. Repeated Substring Pattern
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies
of the substring together. You may assume the given string consists of lowercase English letters only and
its length will not exceed 10000.

Example 1:
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""

"""KMP"""
def repeated_substring_pattern(s) -> bool:
    i, j, m = 1, 0, len(s)
    arr = [0] * m
    while i < m:
        if s[i] == s[j]:
            arr[i] = j + 1
            i += 1
            j += 1
        elif j == 0:
            arr[i] = 0
            i += 1
        else:
            j = arr[j - 1]
    return arr[-1] > 0 and not m % (m - arr[-1])


print(repeated_substring_pattern("abab"))
print(repeated_substring_pattern("aba"))
print(repeated_substring_pattern("abcabcabcabc"))
