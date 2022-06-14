class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = {}
        
        for coin in coins:
            cache[coin] = 1
        
        def coinChangeRec(coins, amount, cache):
            if amount < 0:
                return float('inf')
            
            if amount == 0:
                return 0
            
            if amount in cache:
                return cache[amount]
            
            ans = float('inf')
            
            for coin in coins:
                subProbAns = coinChangeRec(coins, amount - coin, cache)
                if subProbAns != -1:
                    subProbAns += 1
                else:
                    subProbAns = float('inf')
                ans = min(ans, subProbAns)
            
            if ans == float('inf'):
                cache[amount] = -1
            else:
                cache[amount] = ans
            
            return cache[amount]
        
        return coinChangeRec(coins, amount, cache)       