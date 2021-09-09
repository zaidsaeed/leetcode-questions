Problem: https://leetcode.com/problems/fibonacci-number/submissions/

Solution:

```
class Solution:
    def fib(self, n: int) -> int:
        arr = [0, 1]
        if n < 2:
            return arr[n]
        for i in range(2, n+1):
            arr.append(arr[i-1] + arr[i-2])
        print(arr)
        return arr[len(arr)-1]

```
