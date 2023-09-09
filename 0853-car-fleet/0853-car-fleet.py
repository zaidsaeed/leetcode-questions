class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        timeToDestArr = self.createTimeToDestArr(target, position, speed)
        i = len(timeToDestArr) - 1
        while (i > 0 and i < len(timeToDestArr)):
            car1, car2 = timeToDestArr[i-1][1], timeToDestArr[i][1]
            if car1 <= car2:
                timeToDestArr.pop(i-1)
            i -= 1

        return len(timeToDestArr)
    
    def createTimeToDestArr(self, target, position, speed):
        n = len(position)
        timeToDestArr = []
        for i in range(n):
            time = (target-position[i])/speed[i]
            timeToDestArr.append((position[i], time))
        timeToDestArr.sort()
        return timeToDestArr



'''
1) create timeToReachDest array
2) create (pos, timeToReachDest) array
3) sort based on pos
4) join based on fleets (from left to right)
5) return len(arr from step 2)
'''