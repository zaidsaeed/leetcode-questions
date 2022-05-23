class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        q, dp = [], [float('inf') for i in range(amount+1)]
        
        for coin in coins:
            if coin < amount:
                dp[coin] = 1
                q.append(coin)
            elif coin == amount:
                return 1
            
        while q:
            val = q.pop(0)
            count = dp[val]
            # print(val)
            # print(count)
            # print('     ')
            for coin in coins:
                if val + coin < amount and dp[val + coin] == float('inf'):
                    q.append(val + coin)
                    dp[val+coin] = min(dp[val+coin], count+1)
                elif val + coin == amount:
                    return count + 1
        
        return -1


    '''
        coins = [1,2,5], amount = 11
        dp = [_, 1, 1, _, _, 1, 2, 2, 3, _, 3]    
                  
                       
        
    
    '''