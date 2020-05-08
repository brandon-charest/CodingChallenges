class Trie:

    def __init__(self):
        self.head = {}
        pass

    def add(self, word):
        curr = self.head
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr['*'] = True

    def search(self, word):
        curr = self.head

        for ch in word:
            if ch not in curr:
                return False
            curr = curr[ch]
        if '*' in curr:
            return True
        else:
            return False

    def starts_with(self, prefix):
        curr = self.head
        for ch in prefix:
            if ch not in curr:
                return None
            curr


trie = Trie()
trie.add("Hello")
trie.add("Help")
trie.add("Helm")
trie.add("Helmet")

print(trie.search("Helm"))
print(trie.search("Helmet"))


