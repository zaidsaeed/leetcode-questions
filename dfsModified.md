graph = {
  '1' : ['2', '3', '8'],
  '2' : ['4'],
  '3' : ['5'],
  '4' : ['6'],
  '5' : ['4', '7', '8'],
  '6' : ['2'],
  '7': [],
  '8': []
}

counter = 0

visited = []

inOut = {
  '1' : [0, 0],
  '2' : [0, 0],
  '3' : [0, 0],
  '4' : [0, 0],
  '5' : [0, 0],
  '6' : [0, 0],
  '7': [0, 0],
  '8': [0, 0]
}

treeEdges = []
backEdges = []
crossEdges = []
forwardEdges = []

def dfsEdgeTypes(graph, visited, node):
    global counter
    global treeEdges
    global backEdges
    global crossEdges
    global forwardEdges
    
    if not node in visited:
        inOut[node][0] = counter
        counter += 1
        visited.append(node)
        for neighbor in graph[node]:
            if not neighbor in visited:
                treeEdges.append([node, neighbor])
                dfsEdgeTypes(graph, visited, neighbor)
            else:
                preU, postU = inOut[node]
                preV, postV = inOut[neighbor]
                if preU > preV and postU <= postV:
                    backEdges.append([node, neighbor])
                elif preU > preV and postU < postV:
                    crossEdges.append([node, neighbor])
                elif preU > preV and postU >= postV:
                    forwardEdges.append([node, neighbor])
        inOut[node][1] = counter
        counter += 1
            
dfsEdgeTypes(graph, visited, '1')
print(treeEdges)
print(backEdges)
print(crossEdges)
print(forwardEdges)
print(inOut)
