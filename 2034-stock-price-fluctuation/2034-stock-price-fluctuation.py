import heapq

class StockPrice:    
    #[timestamp, price]    
    def __init__(self):
        self.valMap = {}
        self.maxHeap = []
        self.minHeap = []
        self.currentArr = [float('-inf'), None]

    def update(self, timestamp: int, price: int) -> None:
        if timestamp >= self.currentArr[0]:
            self.currentArr = [timestamp, price]
        
        self.valMap[timestamp] = price
        heapq.heappush(self.maxHeap, ((-1*price), timestamp))
        heapq.heappush(self.minHeap, (price, timestamp))        

    def current(self) -> int:
        timestamp, value = self.currentArr
        return value

    def maximum(self) -> int:
        found = None
        while not found:
            value, timestamp = heapq.heappop(self.maxHeap)
            value *= -1
            if self.valMap[timestamp] == value:
                found = True
                heapq.heappush(self.maxHeap, ((value * -1), timestamp))
                return value

    def minimum(self) -> int:
        found = None
        while not found:
            value, timestamp = heapq.heappop(self.minHeap)
            if self.valMap[timestamp] == value:
                found = True
                heapq.heappush(self.minHeap, (value, timestamp))
                return value


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()

'''
    map -> contains most up to date values
    maxheap -> 
    minheap -> 
    current -> constant
'''