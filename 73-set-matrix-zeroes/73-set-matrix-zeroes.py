class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        
        rows = [0 for i in range(n)]
        cols = [0 for i in range(m)]
        
        for row in range(n):
            for col in range(m):
                elem = matrix[row][col]
                if elem == 0:
                    rows[row] = 1
                    cols[col] = 1
        
        for i in range(n):
            row = rows[i]
            if row == 1:
                for j in range(m):
                    matrix[i][j] = 0
                    
        for j in range(m):
            col = cols[j]
            if col == 1:
                for i in range(n):
                    matrix[i][j] = 0
        
                    
'''

[
 [0,1,2,0],
 [3,4,5,2],
 [1,3,1,5]
]
 
 rows = [1, 0, 0]
 cols = [1, 0, 0, 1]

'''