"""
Given a string consisting of N letters 'a' and/or 'b'. In one move, you can swap one letter for another ('a' for 'b'
and 'b' for 'a').

Write a function that given such string, returns the minimum number of moves required to obtain a string containing
no instances of three identical letters

*N is a integer within the range [0..200,000]
*string consists only of the characters 'a' and/or 'b'
"""
import unittest


def min_move(string: str) -> int:
    if not string or len(string) <= 3:
        return 0

    result = a_count = b_count = 0
    for i in range(len(string)):
        if string[i] is 'a':
            a_count += 1
            b_count = 0
        else:
            b_count += 1
            a_count = 0
        if (a_count or b_count) is 3:
            result += 1
            a_count = b_count = 0
    return result


class Test_MinMoveString(unittest.TestCase):

    def test_string_should_return_0(self):
        tests = ['a', 'b', 'ab', 'bab', 'baabab']
        for test in tests:
            assert min_move(test) == 0

    def test_should_return_1(self):
        assert min_move('baaaaa') == 1

    def test_string_should_return_2(self):
        assert min_move('baaabbaabbba') == 2

    def test_string_should_return_3(self):
        assert min_move('baaaaaaaaaab') == 3


if __name__ == '__main__':
    unittest.main()
