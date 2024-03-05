class Node:
    def __init__(self, val = None, wordEnd = False):
        self.val = val
        self.siblings = {}
        self.wordEnd = wordEnd

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        ptr = self.root
        for i in range(len(word)):
            char = word[i]
            wordEnd = (i == (len(word) - 1))
            if not (char in ptr.siblings):
                ptr.siblings[char] = Node(char, wordEnd)
            ptr = ptr.siblings[char]
        ptr.wordEnd = True

    def search(self, word: str) -> bool:
        ptr = self.root
        for i in range(len(word)):
            char = word[i]
            if not (char in ptr.siblings):
                return False
            ptr = ptr.siblings[char]
        return ptr.wordEnd
        

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for i in range(len(prefix)):
            char = prefix[i]
            if not (char in ptr.siblings):
                return False
            ptr = ptr.siblings[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix) 