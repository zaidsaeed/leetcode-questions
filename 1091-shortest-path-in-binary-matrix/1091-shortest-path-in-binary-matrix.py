import collections

def helper(i, j):
    res = [
        [i-1, j],
        [i+1, j],
        [i, j-1],
        [i, j+1],
        [i-1, j-1],
        [i-1, j+1],
        [i+1, j-1],
        [i+1, j+1],
    ]
    return res

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        n = len(grid)
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        my_queue = collections.deque()  # idx, idx, distance
        my_queue.append([0, 0, 1])
        visited = set((0, 0))
        while my_queue:
            i, j, d = my_queue.popleft()
            if i == n-1 and j == n - 1:
                return d
            next_steps = helper(i, j)
            for i, j in next_steps:
                if 0 <= i < n and 0 <= j < n and (i, j) not in visited:
                    if grid[i][j] == 0:
                        my_queue.append([i, j, d+1])
                        visited.add((i, j))
        return -1