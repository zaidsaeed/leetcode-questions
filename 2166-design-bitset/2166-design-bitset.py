class Bitset:

    def __init__(self, size: int):
        self.arr = [0 for i in range(size)]
        self.arrInv = [1 for i in range(size)]
        self.sum = 0
        self.size = size

    def fix(self, idx: int) -> None:
        if self.arr[idx] != 1:
            self.arr[idx] = 1
            self.sum += 1
        
        if self.arrInv[idx] != 0:
            self.arrInv[idx] = 0
        

    def unfix(self, idx: int) -> None:
        if self.arr[idx] != 0:
            self.arr[idx] = 0
            self.sum -= 1
        
        if self.arrInv[idx] != 1:
            self.arrInv[idx] = 1
        

    def flip(self) -> None:
        temp = self.arr
        self.arr = self.arrInv
        self.arrInv = temp
        self.sum = self.size - self.sum
        
        
    def all(self) -> bool:
        return self.sum == len(self.arr)
        

    def one(self) -> bool:
        return self.sum > 0
        
    def count(self) -> int:
        return self.sum
        

    def toString(self) -> str:
        ans = ''
        for num in self.arr:
            ans = ans + str(num)
        return ans
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()