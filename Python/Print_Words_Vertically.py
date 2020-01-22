"""Print Words Vertically
Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.

Example 1:
Input: s = "HOW ARE YOU"
Output: ["HAY","ORO","WEU"]
Explanation: Each word is printed vertically.
 "HAY"
 "ORO"
 "WEU"

Example 2:
Input: s = "TO BE OR NOT TO BE"
Output: ["TBONTB","OEROOE","   T"]
Explanation: Trailing spaces is not allowed.
"TBONTB"
"OEROOE"
"   T"

Example 3:
Input: s = "CONTEST IS COMING"
Output: ["CIC","OSO","N M","T I","E N","S G","T"]
"""

from typing import List
def printVertically(s: str) -> List[str]:
    words = s.split()
    depth = max(len(w) for w in words)
    matrix = [[' ' for i in range(len(words))] for j in range(depth)]
    count = -1

    for word in words:
        count += 1
        for i in range(len(word)):
            matrix[i][count] = word[i]

    for m in range(len(matrix)):
        matrix[m] = ''.join(matrix[m]).rstrip()
        
    return matrix

s = "TO BE OR NOT TO BE"
printVertically(s)