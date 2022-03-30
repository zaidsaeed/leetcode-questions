# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import heapq

graph = {
    'A': [[3, 'B'], [2, 'C']],
    'B': [[6, 'C']],
    'C': [[4, 'D']],
    'D': [[3, 'A']]
}


def primsAlgo(graph):
    unvisited = list(graph.keys())[1:]
    visited = list(graph.keys())[0:1]
    root = visited[0]
    heap, ans = [], []
    for edge in graph[root]:
        heapq.heappush(heap, edge)
    while unvisited:
        edge = heapq.heappop(heap)
        target = edge[1]
        if target in unvisited:
            ans.append(edge)
            unvisited.remove(target)
            visited.append(target)
            for edge in graph[target]:
                heapq.heappush(heap, edge)
    return ans
    


print(primsAlgo(graph))
