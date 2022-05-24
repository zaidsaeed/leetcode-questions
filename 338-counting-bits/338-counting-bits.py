class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0 for i in range(n+1)]
        for i in range(1, n+1):
            ans[i] = self.getBinary(i)
        return ans
    
    def getBinary(self, num):
        one = 0
        while num != 0:
            rem = num % 2
            num = num // 2
            if rem:
                one += 1
        return one
        
        '''
            0 --> 000
            1 --> 001
            2 --> 010
            3 --> 011
            4 --> 100
            5 --> 101
            6 --> 110
            7 --> 111
        
        '''