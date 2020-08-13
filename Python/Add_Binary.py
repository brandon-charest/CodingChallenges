""" 67. Add Binary
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
"""
import unittest


class Solution2():
    def addBinary(self, a: str, b: str) -> str:
        x = bin(int(a,2))
        y = bin(int(b,2))
        z = int(x, 2) + int(y, 2)
        # cut off 0b from answer
        return bin(z)[2:]


class Solution:
    @staticmethod
    def _add(a, b, c=0):
        if a + b + c == 2:
            return 0, 1
        elif a + b + c == 3:
            return 1, 1
        else:
            return (a + b + c), 0

    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        res, carry = [], 0
        while i >= 0 and j >= 0:
            temp, carry = self._add(int(a[i]), int(b[j]), carry)
            res.append(temp)
            i -= 1
            j -= 1

        while i >= 0:
            temp, carry = self._add(int(a[i]), carry)
            res.append(temp)
            i -= 1
        while j >= 0:
            temp, carry = self._add(int(b[j]), carry)
            res.append(temp)
            j -= 1
        if carry == 1:
            res.append(1)
        return ''.join(map(str, res[::-1]))

class Test(unittest.TestCase):
    test = [["11", "1"], ["111", "111"], ["0", "0"], ["1", "111"], ["101111", "10"]]
    answer = ["100", "1110", "0", "1000", "110001"]

    def test_Solution_correct(self):
        s = Solution()
        for i in range(len(self.test)):
            assert s.addBinary(self.test[i][0], self.test[i][1]) == self.answer[i]

    def test_Solution2_correct(self):
        s = Solution2()
        for i in range(len(self.test)):
            assert s.addBinary(self.test[i][0], self.test[i][1]) == self.answer[i]


if __name__ == '__main__':
    unittest.main()

