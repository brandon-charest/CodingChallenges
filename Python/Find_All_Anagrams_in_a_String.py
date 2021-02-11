""" 438. Find All Anagrams in a String
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both
strings s and p will not be larger than 20,100.

The order of output does not matter.
Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"
Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
from typing import List
from collections import Counter


def find_anagrams(s: str, p: str) -> List[int]:
    if not s or len(p) > len(s):
        return []
    result = []
    counter = [0] * 26
    for c in p:
        counter[ord(c) - ord('a')] += 1

    for i, c in enumerate(s):
        counter[ord(c) - ord('a')] -= 1

        if i >= len(p):
            counter[ord(c) - ord('a')] += 1

        if i >= len(p) - 1 and all(x == 0 for x in counter):
            result.append(i - (len(p) - 1))

    return result


string1 = "cbaebabacd"
p1 = "abc"

print(find_anagrams(string1, p1))