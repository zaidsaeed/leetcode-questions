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
## Runtime O(n^2)
## Space O(n)

```
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = float('-inf')
        ansTxt = s[0]
        for i in range(0, len(s)):
            sample = self.expandCenter(i, i, s)
            if (sample[0] > ans):
                ans = sample[0]
                ansTxt = sample[1]
                print(ans)
                print(ansTxt)
        for i in range(0, len(s)-1):
            sample = self.expandCenter(i, i+1, s)
            if (sample[0] > ans):
                ans = sample[0]
                ansTxt = sample[1]
        return ansTxt
    
    def expandCenter(self, l, r, s):
        L = -1
        R = len(s)
        found = True
        ans = 0
        while (l > L and r < R and found):
            if s[l] == s[r]:
                ans = r - l + 1
                l = l - 1
                r = r + 1
            else:
                found = False
        return (ans, s[l+1:r])
            
        
```
