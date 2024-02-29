class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n, ans = len(matrix[0]), len(matrix), []
        self.dfs(0, 0, m, n, matrix, ans)
        return ans
        
    def dfs(self, i, j, m, n, matrix, ans):
        ans.append(matrix[i][j])
        matrix[i][j] = ["visited", matrix[i][j]]
        
        isUpVisited = i - 1 > -1 and isinstance(matrix[i-1][j], int)

        #right
        if j + 1 < m and isinstance(matrix[i][j+1], int) and not isUpVisited:
            return self.dfs(i, j+1, m, n, matrix, ans)
        #down
        if i + 1 < n and isinstance(matrix[i+1][j], int):
            return self.dfs(i+1, j, m, n, matrix, ans)
        #left
        if j - 1 > -1 and isinstance(matrix[i][j-1], int):
            return self.dfs(i, j-1, m, n, matrix, ans)
        #up
        if i - 1 > -1 and isinstance(matrix[i-1][j], int):
            return self.dfs(i-1, j, m, n, matrix, ans)

