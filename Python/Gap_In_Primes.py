"""
The prime numbers are not regularly spaced. For example from 2 to 3 the gap is 1. From 3 to 5 the gap is 2.
From 7 to 11 it is 4. Between 2 and 50 we have the following pairs of 2-gaps
primes: 3-5, 5-7, 11-13, 17-19, 29-31, 41-43

A prime gap of length n is a run of n-1 consecutive composite numbers between two successive primes
(see: http://mathworld.wolfram.com/PrimeGaps.html).

We will write a function gap with parameters:

g (integer >= 2) which indicates the gap we are looking for

m (integer > 2) which gives the start of the search (m inclusive)

n (integer >= m) which gives the end of the search (n inclusive)

In the example above gap(2, 3, 50) will return [3, 5] or (3, 5) or {3, 5} which is the first pair
between 3 and 50 with a 2-gap.

So this function should return the first pair of two prime numbers spaced with a gap of g between the limits m,
n if these numbers exist otherwise nil or null or None or Nothing (depending on the language).
"""
import unittest

"""
First attempt worked but is too slow when using large number ranges. 
Did some digging and found an algorithm called Primality test
https://en.wikipedia.org/wiki/Primality_test
Implemented this below
"""
# def isPrime(num):
#     for n in range(2, num):
#         if num % n == 0:
#             return False
#     return True


def isprime(num):
    if num <= 3:
        return num > 1
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True


def gap(g, m, n):
    last_prime = 0
    for num in range(m, n + 1):
        if isprime(num):
            if last_prime == 0:
                last_prime = num
                continue
            if num - last_prime == g:
                return [last_prime, num]
            else:
                last_prime = num
    return None


class Test_Gap_In_Primes(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(gap(2, 2, 10), [3, 5])
        self.assertEqual(gap(2, 100, 110), [101, 103])

    def test_should_return_none(self):
        self.assertEqual(gap(11, 30000, 100000), None)
        self.assertEqual(gap(3, 3, 10), None)

    def test_larger_numbers(self):
        self.assertEqual(gap(2, 10000000, 11000000), [10000139, 10000141])
        self.assertEqual(gap(8, 30000, 100000), [30161, 30169])


if __name__ == '__main__':
    unittest.main()
