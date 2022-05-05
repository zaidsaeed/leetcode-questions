class Node:
    def __init__(self, letter, wordEnd):
        self.letter = letter
        self.wordEnd = wordEnd
        self.neighbors = {}
    
    def __str__(self):
        return self.letter


class Trie:

    def __init__(self):
        self.root = Node(None, None)
        

    def insert(self, word: str) -> None:
        pointer = self.root
        for i in range(len(word)):
            char = word[i]
            wordEnd = (i == (len(word) - 1))
            if not char in pointer.neighbors:
                pointer.neighbors[char] = Node(char, wordEnd)
            elif wordEnd and not pointer.neighbors[char].wordEnd:
                pointer.neighbors[char].wordEnd = wordEnd
            pointer = pointer.neighbors[char]

    def search(self, word: str) -> bool:
        pointer = self.root
        for i in range(len(word)):
            char = word[i]
            if not char in pointer.neighbors:
                return False
            else:
                pointer = pointer.neighbors[char]
        return pointer.wordEnd
        

    def startsWith(self, prefix: str) -> bool:
        pointer = self.root
        for i in range(len(prefix)):
            char = prefix[i]
            if not char in pointer.neighbors:
                return False
            else:
                pointer = pointer.neighbors[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# ["Trie","insert","search","search","startsWith","insert","search"]
# [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]
#