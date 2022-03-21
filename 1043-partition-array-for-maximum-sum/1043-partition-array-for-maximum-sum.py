class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0 for i in range(len(arr))]
        dp[0] = arr[0]
        
        maxElem = arr[0]
        for i in range(1, k):
            maxElem = max(arr[i], maxElem)
            dp[i] = maxElem * (i + 1)
        
        for i in range(k, len(arr)):
            maxElem = arr[i]
            for j in range(1, k+1):
                maxElem = max(maxElem, arr[i-j+1])
                newSum = (j*maxElem) + dp[i-j]
                dp[i] = max(newSum, dp[i])
                
        return dp[len(arr)-1]