""" 336. Palindrome Pairs
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation
of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Example 2:
Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
"""
def is_palindrome(string):
    return string == string[::-1]

# Too slow
# def palindrome_pairs(words):
#     result = []
#     for word1 in words:
#         for word2 in words:
#             if word1 is word2:
#                 continue
#             if is_palindrome(word1+word2):
#                 result.append([words.index(word1), words.index(word2)])
#     return result

def palindrome_pairs(words):
    result = []
    words_dic = {w:i for i, w in enumerate(words)}
    for i, word in enumerate
    return result


pairs = ["abcd","dcba","lls","s","sssll"]
res = palindrome_pairs(pairs)
print(res)
