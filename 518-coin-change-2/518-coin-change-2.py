class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dpl1 = [0 for i in range(amount + 1)]
        
        
        for i in range(0, amount + 1):
            if i % coins[0] == 0:
                dpl1[i] = 1
        dpl2 = dpl1.copy()
        
        for i in range(1, len(coins)):
            for j in range(1, amount + 1):
                temp = 0
                if j - coins[i] == 0:
                    temp = 1
                elif j - coins[i] > 0:
                    temp = dpl2[j - coins[i]]
                dpl2[j] = temp + dpl1[j]
            dpl1 = dpl2
        
        return dpl2[-1]
                    