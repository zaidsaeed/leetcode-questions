import random
class Solution:

    def __init__(self, w: List[int]):
	    self.prefix = self.genPrefix(w)

    def pickIndex(self) -> int:
        randomNum = random.randint(1, self.prefix[-1])
        return self.findIndex(randomNum)

    def genPrefix(self, w):
        ans = []
        rSum = 0
        for elem in w:
            rSum += elem
            ans.append(rSum)
        return ans

    def findIndex(self, target):
        l = 0
        h = len(self.prefix) - 1
        ans = 0
        while l < h:
            m = l + ((h-l) // 2)
            if self.prefix[m] == target:
                return m
            elif self.prefix[m] < target:
                ans = m
                l = m + 1
            elif self.prefix[m] > target:
                h = m
        return l
