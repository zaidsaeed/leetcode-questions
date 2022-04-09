class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0 for i in range(m)] for j in range(n)]
        
        obFound = False
        for i in range(m):
            if not obFound and obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            else:
                obFound = True
        
        obFound = False
        for i in range(n):
            if not obFound and obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                obFound = True
                
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[n-1][m-1]