""" 500. Keyboard Row
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of
American keyboard.

Example:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
"""

from typing import List


def in_row(word,row):
    for c in word:
        if c not in row:
            return False
    return True


def find_words(words: List[str]) -> List[str]:
    result = []
    row1 = set('qwertyuiop')
    row2 = set('asdfghjkl')
    row3 = set('zxcvbnm')

    for word in words:
        temp = word.lower()
        if in_row(temp, row1) \
                or in_row(temp, row2) \
                or in_row(temp, row3):
            result.append(word)
    return result


x = ["Hello", "Alaska", "Dad", "Peace"]
print(find_words(x))