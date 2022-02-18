class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(0, rows):
            for j in range(0, cols):
                cell = grid[i][j]
                if cell == '1':
                    count += 1
                    self.dfs(i, j, grid)
        return count
    
    def dfs(self, i, j, grid):
        rows = len(grid)
        cols = len(grid[0])
        grid[i][j] = 'T'
        if (i - 1 > -1):
            up = grid[i-1][j]
            if up == '1':
                self.dfs(i-1, j, grid)
        if (i + 1 < rows):
            down = grid[i+1][j]
            if down == '1':
                self.dfs(i+1, j, grid)
        if (j - 1 > -1):
            left = grid[i][j-1]
            if left == '1':
                self.dfs(i, j-1, grid)
        if (j + 1 < cols):
            right = grid[i][j+1]
            if right == '1':
                self.dfs(i, j+1, grid)
            