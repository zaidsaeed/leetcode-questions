import heapq
class Solution:
    
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        def setUp(n, edges, succProb, start):
            graph = {}
            matrix = []
            heap = []
            for i in range(n):
                if (i == start):
                    matrix.append(1)
                    heap.append((-1, i))
                else:
                    matrix.append(0)
                graph[i] = []
            for edge, weight in zip(edges, succProb):
                u = edge[0]
                v = edge[1]
                graph[u].append((v, weight))
                graph[v].append((u, weight))
            heapq.heapify(heap)
            return graph, matrix, heap
        
        def dijkstra(graph, matrix, heap, start, end):
            visited = set()
            while heap:
                u = heapq.heappop(heap)[1]
                for info in graph[u]:
                    v = info[0]
                    weight = info[1]
                    if not v in visited and (matrix[u] * weight > matrix[v]):
                        matrix[v] = max(matrix[v], matrix[u] * weight)
                        heapq.heappush(heap, (-1 * matrix[v], v))
                visited.add(u)
            return matrix[end]
                
        graph, matrix, heap = setUp(n, edges, succProb, start)
        return dijkstra(graph, matrix, heap, start, end)