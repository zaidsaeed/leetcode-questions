https://www.geeksforgeeks.org/program-to-count-number-of-connected-components-in-an-undirected-graph/

```

def buildGraph(v, edges):
    graphMap = {}
    for i in range(v):
        graphMap[i] = []
    
    for edge in edges:
        inNode, outNode = edge[0], edge[1]
        graphMap[inNode].append(outNode)
        
    return graphMap
    
def dfsParent(graph):
    visited = []
    paths = []
    for vertex in graph.keys():
        if vertex not in visited:
            currentPath = []
            dfsRec(graph, vertex, visited, currentPath)
            paths.append(currentPath)
    print(paths)
    return len(paths)
    
def dfsRec(graph, vertex, visited, currentPath):
    if vertex not in visited:
        visited.append(vertex)
        currentPath.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfsRec(graph, neighbor, visited, currentPath)


graph = buildGraph(6, [[0, 2], [2,4], [1,5]])
print(graph)

print(dfsParent(graph))
        
```
