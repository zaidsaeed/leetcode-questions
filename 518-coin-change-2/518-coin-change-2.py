class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        def changeRec(index, amount, coins, memo):            
            if amount == 0:
                return 1
            
            if index == len(coins):
                if amount == 0:
                    return 1
                return 0
            
            if (index, amount) in memo:
                return memo[(index, amount)]
            
            if amount - coins[index] >= 0:
                memo[(index, amount)] = changeRec(index, amount - coins[index], coins, memo) + changeRec(index+1, amount, coins, memo)
                return memo[(index, amount)]
            
            memo[(index, amount)] = changeRec(index+1, amount, coins, memo)
            return memo[(index, amount)]
        
        
        memo = {}
        
        return changeRec(0, amount, coins, memo)