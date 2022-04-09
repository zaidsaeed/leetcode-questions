class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        matrix = [[0 for i in range(m)] for j in range(n)]
        
        for i in range(m): # set first row to all ones
            matrix[0][i] = 1
        
        for i in range(n): # set first col to all ones
            matrix[i][0] = 1
        
        for i in range(1, n):
            for j in range(1, m):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        
        return matrix[n-1][m-1]        