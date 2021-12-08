# Solution One

### O(n^3) Solution Runtime
### O(n) space complexity

Solution:
```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                subStr = s[i:(j+1)]
                if (not self.hasRepeats(subStr)):
                    if len(subStr) > res:
                        res = len(subStr)      
        return res
    
    
    def hasRepeats(self, subStr):
        dict = {}
        for char in subStr:
            if char in dict:
                return True
            else:
                dict[char] = True
        return False
```

# Solution Two
