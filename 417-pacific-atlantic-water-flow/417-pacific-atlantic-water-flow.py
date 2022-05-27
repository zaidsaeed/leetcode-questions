class Solution:
    
    directions = [[0,1], [1,0], [0,-1],  [-1,0]]
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        pacificMatrix, atlanticMatrix = self.getMatricies(n, m)
        ans = []
        
        for i in range(n):
            self.dfs(heights, pacificMatrix, float('-inf'), i, 0, n, m)
            self.dfs(heights, atlanticMatrix, float('-inf'), i, m-1, n, m)
        
        for j in range(m):
            self.dfs(heights, pacificMatrix, float('-inf'), 0, j, n, m)
            self.dfs(heights, atlanticMatrix, float('-inf'), n-1, j, n, m)
        
        for i in range(n):
            for j in range(m):
                if pacificMatrix[i][j] and atlanticMatrix[i][j]:
                    ans.append([i, j])
        
        return ans
            
    def dfs(self, matrix, visited, height, x, y, n, m):
        if x < 0 or x >= n or y < 0 or y >= m or visited[x][y] or (height > matrix[x][y]):
            return
        visited[x][y] = 1
        for d in self.directions:
            self.dfs(matrix, visited, matrix[x][y], x + d[0], y + d[1], n, m)
        
    
    def getMatricies(self, n, m):
        atlanticMatrix = [[0 for j in range(m)] for i in range(n)]
        pacificMatrix = [[0 for j in range(m)] for i in range(n)]
        return pacificMatrix, atlanticMatrix