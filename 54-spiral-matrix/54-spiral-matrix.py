class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
#         def isUpperRow(i, j, n, m, matrix):
#             if matrix[i][j] == 'v':
#                 return False
#             if j != m - 1 and i == 0:
#                 return True
#             if j <= m-2:
#                 if matrix[i-1][j] == 'v' and matrix[i][j+1] != 'v':
#                     return True
#             return False
        
#         def isRightCol(i, j, n, m, matrix):
#             if matrix[i][j] == 'v':
#                 return False
#             if i != n-1 and j == m-1:
#                 return True
#             if i <= n-2:
#                 if matrix[i][j+1] == 'v' and matrix[i+1][j] != 'v':
#                     return True
#             return False
        
#         def isBottomRow(i, j, n, m, matrix):
#             if matrix[i][j] == 'v':
#                 return False
#             if j != 0 and i == n - 1:
#                 return True
#             if j > 1:
#                 if matrix[i+1][j] == 'v' and matrix[i][j-1] != 'v':
#                     return True
#             return False
        
#         def isLeftCol(i, j, n, m, matrix):
#             if matrix[i][j] == 'v':
#                 return False
#             if i != 0 and j == 0:
#                 return True
#             if j <= m - 1:
#                 if matrix[i][j-1] == 'v' and matrix[i-1][j] != 'v':
#                     return True
#             return False
        
        def dfs(i, j, n, m, matrix, ans):
            isUpVisited = (i == 0) or (i > 0 and matrix[i-1][j] == 'v')
            isRightVisited = (j == m-1) or (j < m-1 and matrix[i][j+1] == 'v')
            isDownVisited = (i == n-1) or (i < n-1 and matrix[i+1][j] == 'v')
            isLeftVisited = (j == 0) or (j > 0 and matrix[i][j-1] == 'v')
            ans.append(matrix[i][j])
            matrix[i][j] = 'v'
            
            
            if not isRightVisited and isUpVisited:
                return dfs(i, j+1, n, m, matrix, ans)
            if not isDownVisited:
                return dfs(i+1, j, n, m, matrix, ans)
            if not isLeftVisited:
                return dfs(i, j-1, n, m, matrix, ans)
            if not isUpVisited:
                return dfs(i-1, j, n, m, matrix, ans)
            
            return ans
            
                        
        return dfs(0, 0, len(matrix), len(matrix[0]), matrix, [])

    
# 01 02 03 04 05 
# 06 07 08 09 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25