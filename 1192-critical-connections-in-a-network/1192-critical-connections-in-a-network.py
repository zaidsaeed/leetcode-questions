class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.timer = 0
    
        def genGraph(connections, n):
            graphMap = {}
            for i in range(n):
                graphMap[i] = []
            for connection in connections:
                fromNode = connection[0]
                toNode = connection[1]
                graphMap[fromNode].append(toNode)
                graphMap[toNode].append(fromNode)
            return  graphMap
        
        def getBridgesUtil(u, low, visited, disc, parent, ans):
            visited[u] = True
            disc[u] = self.timer
            low[u] = self.timer
            self.timer += 1
            for v in graph[u]:
                if not visited[v]:
                    getBridgesUtil(v, low, visited, disc, u, ans)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        ans.append([u, v])
                        
                elif v != parent:
                        low[u] = min(low[u], disc[v])
                    
        def getBridges(n, graph):
            low = [float('inf') for i in range(n)]
            visited = [False for i in range(n)]
            disc = [float('inf') for i in range(n)]
            ans = []
            getBridgesUtil(0, low, visited, disc, -1, ans)
            return ans
        
        graph = genGraph(connections, n)
        return getBridges(n, graph)
        
        