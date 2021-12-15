## Runtime: O(n^2) Solution
## Space: O(n^2) Solution
```
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ansx = 0
        ansy = 1
        matrix = [[0 for i in range(len(s))] for i in range(len(s))]
        for i in range(0, len(s)):
            for j in range(0, len(s)-i):
                x, y = j, i+j
                print(x)
                print(y)
                if i == 0: #first diagonal 
                    matrix[x][y] = 1
                elif i == 1 and (s[x] == s[y]): #second diagonal
                        matrix[x][y] = 1
                        ansx = x
                        ansy = y + 1
                else:
                    if (matrix[x+1][y-1] == 1) and (s[x] == s[y]):
                            matrix[x][y] = 1
                            ansx = x
                            ansy = y + 1
            
        return s[ansx:ansy]

```
