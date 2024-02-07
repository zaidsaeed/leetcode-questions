class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        
        '''
        1) Iterate through the array
        2) set buy pointer to element at index 0
        3) if you come across a number > pointer: calc ans and comapare with ans
           if you come across a number < pointer: change pointer to new number
        4) return ans
        '''
        ans = 0
        buyPrice = prices[0]
        for i in range(0, len(prices)):
            todayPrice = prices[i]
            if todayPrice < buyPrice:
                buyPrice = todayPrice
            elif todayPrice >= buyPrice:
                ans = max(ans, todayPrice - buyPrice)
        return ans
                