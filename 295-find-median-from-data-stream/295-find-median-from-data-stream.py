class MedianFinder:

    def __init__(self):
        self.arr = []
        self.size = 0
    
    def findIndex(self, target):
        l, h = 0, len(self.arr) - 1
        ans = -1
        while l <= h:
            m = l + ((h-l)//2)
            if self.arr[m] >= target:
                h = m - 1
            elif self.arr[m] < target:
                ans = m
                l = m + 1
        return ans 

    def addNum(self, num: int) -> None:
        ind = self.findIndex(num)
        self.arr.insert(ind+1, num)
        self.size += 1
        

    def findMedian(self) -> float:
        medianIndex = self.size // 2
        if self.size % 2 == 0:
            return (self.arr[medianIndex] + self.arr[medianIndex-1]) / 2
        else:
            return self.arr[medianIndex]
    
    '''
           [0, ]
           even = T
           mI = 0
    '''
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()