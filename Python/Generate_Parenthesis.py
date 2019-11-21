""" 22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
from typing import List


def generate(n: int) -> List[str]:
    if n == 0:
        return []
    return generate_helper('', n, 0)


def generate_helper(curr, open_paren, closed_paren):
    if open_paren == 0:
        return [curr + ')' * closed_paren]
    elif closed_paren == 0:
        return generate_helper(curr + '(', open_paren - 1, closed_paren + 1)
    return generate_helper(curr + '(', open_paren - 1, closed_paren + 1) \
        + generate_helper(curr + ')', open_paren, closed_paren - 1)


print(generate(3))


