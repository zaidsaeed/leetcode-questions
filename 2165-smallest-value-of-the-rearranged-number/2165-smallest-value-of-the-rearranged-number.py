import heapq

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            return self.negFunc(abs(num))
        elif num > 0:
            return self.posFunc(num)
        return num
    
    def posFunc(self, num):
        heap = []
        numZeros = 0
        ans = 0
        while num != 0:
            rem = num % 10
            num = num // 10
            if rem != 0:
                heapq.heappush(heap, rem)
            else:
                numZeros += 1
        
        ans = ans + heapq.heappop(heap)
        ans = ans * pow(10, numZeros)
        
        exp = 1
        while heap:
            num = heapq.heappop(heap)
            ans = ans * pow(10, exp) + num
        
        return ans
    
    
    def negFunc(self, num):
        heap = []
        numZeros = 0
        ans = 0
        while num != 0:
            rem = num % 10
            num = num // 10
            if rem != 0:
                heapq.heappush(heap, rem)
            else:
                numZeros += 1
                
        exp = 0
        while heap:
            num = heapq.heappop(heap)
            ans = ans + (-1 * num * pow(10, exp))
            exp += 1
        
        return (ans * pow(10, numZeros))
            