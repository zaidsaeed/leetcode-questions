class Solution:
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ans = False
        rows = len(board)
        cols = len(board[0])
        
        for i in range(0, rows):
            for j in range(0, cols):
                board[i][j] = [board[i][j], False]
        
        for i in range(0, rows):
            for j in range(0, cols):
                char = board[i][j][0]
                if char == word[0] and not self.ans:
                    board[i][j][1] = True
                    self.dfs(i, j, board, word[1:], rows, cols)
                    board[i][j][1] = False
                    
        return self.ans
    
    def dfs(self, i, j, board, word, rows, cols):
        if word == '':
            self.ans = True
            return
        
        char = word[0]
        
        up = None
        if (i-1 >= 0):
            up = board[i-1][j][0]
            upVisited = board[i-1][j][1] 
            if not upVisited and up == char:
                board[i-1][j][1] = True
                self.dfs(i-1, j, board, word[1:], rows, cols)
                board[i-1][j][1] = False

        down = None
        if (i+1 < rows):
            down = board[i+1][j][0]
            downVisited = board[i+1][j][1] 
            if not downVisited and down == char:
                board[i+1][j][1] = True
                self.dfs(i+1, j, board, word[1:], rows, cols)
                board[i+1][j][1] = False

        left = None
        if (j-1 >= 0):
            left = board[i][j-1][0]
            leftVisited = board[i][j-1][1]
            if not leftVisited and left == char:
                board[i][j-1][1] = True
                self.dfs(i, j-1, board, word[1:], rows, cols)
                board[i][j-1][1] = False
                
        right = None
        if (j+1 < cols):
            right = board[i][j+1][0]
            rightVisited = board[i][j+1][1]
            if not rightVisited and right == char:
                board[i][j+1][1] = True
                self.dfs(i, j+1, board, word[1:], rows, cols)
                board[i][j+1][1] = False
        
            
            