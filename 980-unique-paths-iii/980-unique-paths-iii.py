class Solution:
    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.ans = 0
        
        def getStartZero(grid, n, m):
            start = None
            zeroCount = 0
            for i in range(n):
                for j in range(m):
                    elem = grid[i][j]
                    if elem == 1:
                        start = (i, j)
                    elif elem == 0:
                        zeroCount += 1
            return (zeroCount, start)
        
        def dfs(x, y, n, m, grid, zeroCount, vCount):
            if (x >= 0 and x < n and y >= 0 and y < m):
                elem = grid[x][y]
                if elem == 1:
                    grid[x][y] = -1
                    dfs(x+1, y, n, m, grid, zeroCount, vCount)
                    dfs(x-1, y, n, m, grid, zeroCount, vCount)
                    dfs(x, y+1, n, m, grid, zeroCount, vCount)
                    dfs(x, y-1, n, m, grid, zeroCount, vCount)
                    # grid[x][y] = 1
                elif elem == 0:
                    grid[x][y] = -1
                    dfs(x+1, y, n, m, grid, zeroCount, vCount + 1)
                    dfs(x-1, y, n, m, grid, zeroCount, vCount + 1)
                    dfs(x, y+1, n, m, grid, zeroCount, vCount + 1)
                    dfs(x, y-1, n, m, grid, zeroCount, vCount + 1)
                    grid[x][y] = 0 
                elif elem == 2:
                    if vCount == zeroCount:
                        self.ans += 1
                        
        n = len(grid)
        m = len(grid[0])
        zeroCount, start = getStartZero(grid, n, m)
        dfs(start[0], start[1], n, m, grid, zeroCount, 0)
        
        return self.ans
            
        