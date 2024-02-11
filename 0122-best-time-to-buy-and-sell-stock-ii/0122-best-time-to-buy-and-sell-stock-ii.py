class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buyPoint = prices[0]
        for i in range(1, len(prices)):
            price = prices[i]
            if price < buyPoint:
                buyPoint = price
            elif price > buyPoint:
                ans += (price - buyPoint)
                buyPoint = price
        return ans
    
    '''
        [7,1,5,3,6,4]
                   ^
         ans = 7
         bP = 3
    '''