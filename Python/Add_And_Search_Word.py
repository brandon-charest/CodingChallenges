""" 211. Add and Search Word - Data structure design
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or
.. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""

class WordDictionary:
    def __init__(self):
        self.head = {}

    def addWord(self, word: str) -> None:
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur["*"] = True

    def search(self, word: str, cur=None) -> bool:
        if cur is None:
            cur = self.head
        for i in range(len(word)):
            ch = word[i]
            if ch == ".":
                for path in cur:
                    if path == "*":
                        continue
                    if self.search(word[i + 1:], cur[path]):
                        return True
                return False
            else:
                if ch not in cur:
                    return False
                cur = cur[ch]
        if "*" in cur:
            return True
        return False
