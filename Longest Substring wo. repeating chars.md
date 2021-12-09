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
### O(n) Solution Runtime
### O(1) space complexity

```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pt1, pt2 = 0, 0
        res = 0
        dict = {}
        while pt2 < len(s):
            if s[pt2] in dict:
                if (pt2 - pt1) > res:
                    res = pt2 - pt1
                pt1 += 1
                pt2 = pt1
                dict = {}
            else:
                dict[s[pt2]] = True
                pt2 += 1
        if (pt2 - pt1) > res:
            res = pt2 - pt1
        return res   
```
