Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

```

n = 5
edges = [[0,1], [0,2], [0,3], [1,4]]

def buildTree(n, edges):
    treeMap = {}
    
    for i in range(n):
        treeMap[i] = []
    
    for edge in edges:
        fromNode = edge[0]
        toNode = edge[1]
        treeMap[fromNode].append(toNode)
    
    return treeMap

def ans(n, edges):
    start = edges[0][0]
    visited = set()
    treeMap = buildTree(n, edges)
    
    ans = dfs(start, visited, treeMap)
    if ans == False:
        return False
    return len(visited) == n

def dfs(node, visited, treeMap):
    if node in visited:
        return False
    else:
        visited.add(node)
    for neighbor in treeMap[node]:
        res = dfs(neighbor, visited, treeMap)
        if res == False:
            return False
    return True

print(ans(n ,edges))

```
