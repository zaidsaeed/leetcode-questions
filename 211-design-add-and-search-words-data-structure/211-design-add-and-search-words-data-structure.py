class Node:
    def __init__(self, letter, wordEnd):
        self.letter = letter
        self.wordEnd = wordEnd
        self.neighbors = {}    


class WordDictionary:

    def __init__(self):
        self.root = Node(None, None)
        

    def addWord(self, word: str) -> None:
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
        return self.searchRec(word, self.root)
        
    def searchRec(self, word, pointer):
        if word == '':
            return pointer.wordEnd
        for i in range(len(word)):
            char = word[i]
            if char == '.':
                found = False
                for node in pointer.neighbors.values():
                    if self.searchRec(word[i+1:], node):
                        return True
                return False 
            elif not char in pointer.neighbors:
                return False
            else:
                pointer = pointer.neighbors[char]
        return pointer.wordEnd


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)