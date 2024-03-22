class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.createAdjList(numCourses, prerequisites)
        classWithNoPrereqs = self.getNextClass(graph)
        while classWithNoPrereqs != None:
            self.removeClassFromGraph(classWithNoPrereqs, graph)
            classWithNoPrereqs = self.getNextClass(graph)

        return len(graph.keys()) == 0
    
    def removeClassFromGraph(self, classToRemove, graph):
        for aclass, preqs in graph.items():
            if classToRemove in preqs:
                preqs.remove(classToRemove)
                
        del graph[classToRemove]
    
    def getNextClass(self, graph):
        for aclass, preqs in graph.items():
            if len(preqs) == 0:
                return aclass
        return None
            
    def createAdjList(self, numCourses, prerequisites):
        graph = {}
        
        for i in range(numCourses):
            graph[i] = set()
        
        for relation in prerequisites:
            course, prereq = relation
            graph[course].add(prereq)
        
        return graph
            