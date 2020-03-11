""" 415. Add Strings
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:
The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
def add_strings(num1: str, num2: str) -> str:
    i = len(num1) - 1
    j = len(num2) - 1
    carry, res = 0, []

    def convert(str_num):
        return ord(str_num) - ord('0')

    while i >= 0 or j >= 0:
        total = carry

        if i >= 0:
            total += convert(num1[i])
        if j >= 0:
            total += convert(num2[j])

        res.append(total % 10)
        carry = total // 10
        i -= 1
        j -= 1

    if carry > 0:
        res.append(carry)
    res.reverse()
    return ''.join(str(x) for x in res)


print(add_strings('13', '124'))
