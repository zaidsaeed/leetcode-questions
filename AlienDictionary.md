ordering = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

# ordering = [
#   "z",
#   "x"
# ]

# ordering = [
#   "z",
#   "x",
#   "z"
# ]

def soln(ordering):
    cycle = []
    def createGraph(ordering):
        graphMap = {}
        for i in range(len(ordering)-1):
            firstWord = ordering[i]
            secondWord = ordering[i+1]
            minLength = min(len(firstWord), len(secondWord))
            for j in range(minLength):
                firstChar = firstWord[j]
                secondChar = secondWord[j]
                if firstChar != secondChar:
                    if firstChar in graphMap:
                        graphMap[firstChar].append(secondChar)
                    else:
                        graphMap[firstChar] = [secondChar]
                    break
        return graphMap
    
    def topoRec(graphMap, key, visited, stack, traversal, cycle):
        if key not in visited:
            visited.append(key)
            traversal.append(key)
            for neighbor in graphMap.get(key,[]):
                if len(cycle) > 0:
                    return
                elif neighbor in traversal:
                    cycle.append(True)
                    break
                elif neighbor not in visited:
                    topoRec(graphMap, neighbor, visited, stack, traversal, cycle)
            if len(cycle) == 0:
                stack.insert(0, key)
    
    def topoParent(graphMap, visited, stack, cycle):
        for key in graphMap.keys():
            if len(cycle) > 0:
                break
            if key not in visited:
                topoRec(graphMap, key, visited, stack, [], cycle)
            
    graphMap = createGraph(ordering)
    visited, stack = [], []
    topoParent(graphMap, visited, stack, cycle)
    if len(cycle) > 0:
        return 'None'
    else:
        return ''.join(stack)

print(soln(ordering))

'''
{'t': ['f'], 'w': ['e'], 'r': ['t'], 'e': ['r']}
                                    ^
  
 visited = [t, f, w, e, r]
 stack = [w, e, r, t, f]
'''
        
