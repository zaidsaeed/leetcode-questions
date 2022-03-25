import heapq
class Solution:
    
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list) ## Initialise graph
        visited = set() ## Initialise visited set
        
        for idx, (src, dst) in enumerate(edges): ## Traverse through the edges array to update the graph
            graph[src].append((dst, succProb[idx]))
            graph[dst].append((src, succProb[idx]))
            
        probs = [0]*n ## Initialise a probablity array to indicate maximum success probablity from start node to all the other nodes
        probs[start] = 1 ## Success probablity to the start node itself is 1
        
        pq = [(-1, start)] ## Push the result to maxHeap in (prob, node) format -> Hence prob*=-1 
        heapify(pq)
        
		## Dijkstra's algorithm
        while pq:
            _, node = heappop(pq)
            for nei, currSuccProb in graph[node]:
                if not nei in visited and probs[node]*currSuccProb > probs[nei]:
                    probs[nei] = probs[node]*currSuccProb
                    heappush(pq, (-probs[nei], nei))
                
            visited.add(node)
                
        return probs[end]