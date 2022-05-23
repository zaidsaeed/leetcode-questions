import random
class Solution:

    def __init__(self, w: List[int]):
	    self.prefix = self.genPrefix(w)

    def pickIndex(self) -> int:
        randomNum = random.randint(1, self.prefix[-1])
        return self.findIndex(randomNum)
        print('--------')
        print(self.prefix)
        print(randomNum)
        print(self.findIndex(randomNum))
        print(self.pickIndexSol(self.prefix, randomNum))
        print('--------')

    def genPrefix(self, w):
        ans = []
        rSum = 0
        for elem in w:
            rSum += elem
            ans.append(rSum)
        return ans
    
    def pickIndexSol(self, ps, target):
        l, r = 0, len(ps) - 1
        while l < r:
            m = (l + r) // 2
            if target > ps[m]: l = m + 1
            else: r = m
        return l

    def findIndex(self, target):
        l = 0
        h = len(self.prefix) - 1
        ans = h
        while l <= h:
            m = l + ((h-l + 1) // 2)
            if self.prefix[m] < target:
                l = m + 1
            elif self.prefix[m] >= target:
                ans = m
                h = m - 1
        return ans

    '''
    [3, 17, 18, 25]
     l   m       h
    '''
    