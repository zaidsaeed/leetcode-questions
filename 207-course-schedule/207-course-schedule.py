class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.cycle = False
        
        def genGraph(numCourses, prerequisites):
            graphMap = {}
            visitedMap = {}
            
            for node in range(numCourses):
                visitedMap[node] = False
            
            for arr in prerequisites:
                fromNode = arr[1]
                toNode= arr[0]
                arr = graphMap.get(fromNode, [])
                arr.append(toNode)
                graphMap[fromNode] = arr
            
            return graphMap, visitedMap
        
        def dfsRec(graph, visited, node, visitedMap):
            for neighbor in graph.get(node, []):
                if neighbor in visited:
                    print(node)
                    self.cycle = True
                    return
                elif not visitedMap[neighbor]:
                    visited.append(neighbor)
                    visitedMap[neighbor] = True
                    dfsRec(graph, visited, neighbor, visitedMap)
                    visited.remove(neighbor)
            
        
        def dfs(graph, numCourses, visitedMap):
            for node in range(numCourses):
                if not self.cycle and not visitedMap[node]:
                    visited = []
                    visited.append(node)
                    dfsRec(graph, visited, node, visitedMap)
        
        
        graph, visitedMap = genGraph(numCourses, prerequisites)
        print(graph)
        dfs(graph, numCourses, visitedMap)

        return not self.cycle