class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        
        def buildMatrix(n, edges):
            matrix = [[float('inf') for j in range(n)] for i in range(n)]
            
            for i in range(n):
                matrix[i][i] = 0
            
            for edge in edges:
                u = edge[0]
                v = edge[1]
                weight = edge[2]
                matrix[u][v] = weight
                matrix[v][u] = weight
            
            return matrix
        
        def fW(matrix, n, edges, thresh):
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
            
            ans = []
            cnt = 0
            for i in range(n):
                cnt = 0
                for j in range(n):
                    if i != j and matrix[i][j] <= thresh:
                        cnt += 1
                ans.append(cnt)
            minE, minI = float('inf'), 0
            print(ans)
            for i in range(n):
                if ans[i] < minE:
                    minE = ans[i]
                    minI = i
                elif ans[i] == minE:
                    minI = i
            return minI
        
        
        matrix = buildMatrix(n, edges)
        return fW(matrix, n, edges, distanceThreshold)