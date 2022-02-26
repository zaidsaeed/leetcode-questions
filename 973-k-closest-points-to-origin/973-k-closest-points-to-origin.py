import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            distances.append(self.kDist(point))
        distances.sort(key=lambda dist: dist[0])
        return [distances[i][1] for i in range(k)]
    
    def kDist(self, point):
        if point:
            a = point[0]
            b = point[1]
            a = pow(a, 2)
            b = pow(b, 2)
            
            return [math.sqrt((a+b)), point]
        return float('inf')
        
        