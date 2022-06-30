from collections import deque 

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # [i , j, obstacles removed, moves done]
        q = deque([[0, 0, 0, 0]])
        
        visited = [[float('inf') for j in range(len(grid[0]))] for i in range(len(grid))]
        
        visited[0][0] = 0
        
        while q:
            # print(q)
            elem = q.popleft()
            i, j, obstaclesRemoved, movesDone = elem
            
            if i == (len(grid) - 1) and j == (len(grid[0]) - 1):
                return movesDone
            
            #up
            if i-1 >= 0:
                newObstaclesRemoved = obstaclesRemoved+grid[i-1][j]
                if newObstaclesRemoved <= k and newObstaclesRemoved < visited[i-1][j]:
                    visited[i-1][j] = newObstaclesRemoved
                    q.append([i-1, j, newObstaclesRemoved, movesDone+1])
            
            #down
            if i+1 < len(grid):
                newObstaclesRemoved = obstaclesRemoved+grid[i+1][j]
                if newObstaclesRemoved <= k and newObstaclesRemoved < visited[i+1][j]:
                    visited[i+1][j] = newObstaclesRemoved
                    q.append([i+1, j, newObstaclesRemoved, movesDone+1])
            
            #left
            if j - 1 >= 0:
                newObstaclesRemoved = obstaclesRemoved+grid[i][j-1]
                if newObstaclesRemoved <= k and newObstaclesRemoved < visited[i][j-1]:
                    visited[i][j-1] = newObstaclesRemoved
                    q.append([i, j-1, newObstaclesRemoved, movesDone+1])
            
            #right
            if j+1 < len(grid[0]):
                newObstaclesRemoved = obstaclesRemoved+grid[i][j+1]
                if newObstaclesRemoved <= k and newObstaclesRemoved < visited[i][j+1]:
                    visited[i][j+1] = newObstaclesRemoved
                    q.append([i, j+1, newObstaclesRemoved, movesDone+1])
        
        return -1
                

        