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
    
    def getR(self):
        return self.root       

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
                return False, None
            else:
                pointer = pointer.neighbors[char]
        return True, pointer


class Solution:
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        x = len(board)
        y = len(board[0])
        ans = set()
        trie = Trie()
        
        for word in words:
            trie.insert(word)
            
            
        for i in range(x):
            for j in range(y):
                board[i][j] = [board[i][j], True]
        
        root = trie.getR()
        for i in range(x):
            for j in range(y):
                boardChar = board[i][j][0]
                boardCharFree = board[i][j][1]
                if trie.startsWith(boardChar)[0]:
                    board[i][j][1] = False
                    self.expand(i, j, board, ans, root.neighbors[boardChar], boardChar)
                    board[i][j][1] = True
        
        return ans
    
    
    def expand(self, i, j, board, ans, node, string):
        x = len(board)
        y = len(board[0])
        
        if node.wordEnd:
            ans.add(string)

        up = None
        if i - 1 >= 0:
            up = board[i-1][j][0]
            upFree = board[i-1][j][1]
            if upFree and node.neighbors.get(up, None):
                board[i-1][j][1] = False
                self.expand(i-1, j, board, ans, node.neighbors[up], string+up)
                board[i-1][j][1] = True


        left = None
        if j - 1 >= 0:
            left = board[i][j-1][0]
            leftFree = board[i][j-1][1]
            if leftFree and node.neighbors.get(left, None):
                board[i][j-1][1] = False
                self.expand(i, j-1, board, ans, node.neighbors[left], string+left)
                board[i][j-1][1] = True

        down = None
        if i + 1 < x:
            down = board[i+1][j][0]
            downFree = board[i+1][j][1]
            if downFree and node.neighbors.get(down, None):
                board[i+1][j][1] = False
                self.expand(i+1, j, board, ans, node.neighbors[down], string+down)
                board[i+1][j][1] = True

        right = None
        if j+1 < y:
            right = board[i][j+1][0]
            rightFree = board[i][j+1][1]
            if rightFree and node.neighbors.get(right, None):
                board[i][j+1][1] = False
                self.expand(i, j+1, board, ans, node.neighbors[right], string+right)
                board[i][j+1][1] = True