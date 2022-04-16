class Solution:
    
    # minE = 1
    # ans = 5
    #
    #
    # [7,1,5,3,6,4]
               
    def maxProfit(self, prices: List[int]) -> int:
        minElem = float('inf')
        ans = float('-inf')
        
        ptr = 0
        
        while ptr < len(prices):
            num = prices[ptr]
            if num < minElem:
                minElem = num
            ans = max(ans, num-minElem)
            ptr += 1
        
        return ans