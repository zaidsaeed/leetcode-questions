class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def coinChangeRec(coins, amount, cache, count):
    
            if amount in cache:
                return cache[amount]
            
            if amount == 0:
                return count
            
            if amount < 0:
                return float('inf')
            
            ans = float('inf')
            for coin in coins:
                remainder = amount-coin
                ans = min(ans, coinChangeRec(coins, remainder, cache, count))
            
            cache[amount] = ans + 1
            
            return cache[amount]
        
        cache = {}
        res = coinChangeRec(coins, amount, cache, 0)
        if res == float('inf'):
            return -1
        return res

    '''
        coins = [1,2,5], amount = 11
                        
                        11
                    10   9  6
        
    
    '''