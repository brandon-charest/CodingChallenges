""" 208. Implement Trie (Prefix Tree)
Implement a trie with insert, search, and startsWith methods.

Example:
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true

Note:
You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""


class Trie:

    def __init__(self):
        self.head = {}

    def insert(self, word: str) -> None:
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['*'] = True

    def search(self, word: str) -> bool:
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]
        if '*' in cur:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.head

        for ch in prefix:
            if ch not in cur:
                return False
            cur = cur[ch]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
param_2 = obj.search("apple")
param_3 = obj.startsWith("app")

print(param_2, param_3)