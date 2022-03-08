```
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : ['5'],
  '4' : ['8'],
  '8' : []
}

counter = 0

visited = []

def dfs(graph, visited, node):
    if not node in visited:
        print(node)
        visited.append(node)
        for neighbor in graph[node]:
            dfs(graph, visited, neighbor)
            
inOut = {
  '5' : [0, 0],
  '3' : [0, 0],
  '7' : [0, 0],
  '2' : [0, 0],
  '4' : [0, 0],
  '8' : [0, 0]
}
            
def dfsEdgeTypes(graph, visited, node):
    global counter
    if not node in visited:
        inOut[node][0] = counter
        counter += 1
        visited.append(node)
        for neighbor in graph[node]:
            dfsEdgeTypes(graph, visited, neighbor)
        inOut[node][1] = counter
            
dfsEdgeTypes(graph, visited, '5')
print(inOut)
```
