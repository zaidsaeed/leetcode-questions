from collections import deque
class Solution:
    def racecar(self, target: int) -> int:
        # (steps, position, speed)
        q = deque([(0, 0, 1)])
        
        while q:
            steps, position, speed = q.popleft()
            
            if position == target:
                return steps
            
            q.append((steps +1, position + speed, speed * 2))
                
            if position + speed > target and speed > 0:
                q.append((steps + 1, position, -1))
            
            if position + speed < target and speed < 0:
                q.append((steps +1, position, 1))
