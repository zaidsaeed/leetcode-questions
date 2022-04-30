class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        ans = 0
        for i in range(2, len(n)):
            dig = n[i]
            if dig == '1':
                ans += 1
        return ans